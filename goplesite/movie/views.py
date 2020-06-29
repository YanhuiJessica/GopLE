from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import re, json, urllib.request, urllib.error

from .forms import MovieForm
from .models import Movies

def get_imgpaths(movies):
    imgpaths = []
    for m in movies:
        try:
            data = urllib.request.urlopen('https://api.themoviedb.org/3/movie/' + str(m.movieId) + '/images?api_key=93e48491c391483da7b34d5e0e570a9a')
        except urllib.error.HTTPError as e:
            imgpaths.append('/9PCsWrw1GvrZkrd1GCxRqscgZu0.jpg')
            continue
        data = json.loads(data.read())['backdrops']
        if len(data):
            data = data[0]['file_path']
        else:
            data = '/9PCsWrw1GvrZkrd1GCxRqscgZu0.jpg'
        imgpaths.append(data)
    return imgpaths

def index(request):
    form = MovieForm()
    return render(request, 'movie/moviesearch.html', {'form': form})

def search(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            keyword = form.cleaned_data['keyword']
            style = form.cleaned_data['style']
            if keyword != '' and style == '':
                return HttpResponseRedirect(reverse('movie:key_results', args=(keyword, )))
            elif keyword == '' and style != '':
                return HttpResponseRedirect(reverse('movie:style_results', args=(style, )))
            elif keyword != '' and style != '':
                return HttpResponseRedirect(reverse('movie:results', args=(keyword, style)))
            else:
                return HttpResponseRedirect(reverse('movie:index'))
    return render(request, 'movie/movieseares.html', {'form': form})

def key_results(request, keyword):
    form = MovieForm()
    regk = ".*" + keyword + ".*"
    movies = Movies.objects(title=re.compile(regk, re.IGNORECASE)).order_by('-rating')[:30]
    return render(request, 'movie/movieseares.html', {'form': form, 'movies': zip(movies, get_imgpaths(movies))})

def style_results(request, style):
    form = MovieForm()
    regs = ".*" + style + ".*"
    movies = Movies.objects(genres=re.compile(regs, re.IGNORECASE)).order_by('-rating')[:30]
    return render(request, 'movie/movieseares.html', {'form': form, 'movies': zip(movies, get_imgpaths(movies))})

def results(request, keyword, style):
    form = MovieForm()
    regk = ".*" + keyword + ".*"
    regs = ".*" + style + ".*"
    movies = Movies.objects(title=re.compile(regk, re.IGNORECASE), genres=re.compile(regs, re.IGNORECASE)).order_by('-rating')[:30]
    return render(request, 'movie/movieseares.html', {'form': form, 'movies': zip(movies, get_imgpaths(movies))})
