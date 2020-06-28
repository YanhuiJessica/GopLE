from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import MovieForm
import re, json
from .models import Movies

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
    for movie in movies:
        print(movie.title)
    return render(request, 'movie/movieseares.html', {'form': form, 'movies': movies})

def style_results(request, style):
    form = MovieForm()
    regs = ".*" + style + ".*"
    movies = Movies.objects(genres=re.compile(regs, re.IGNORECASE)).order_by('-rating')[:30]
    for movie in movies:
        print(movie.title)
    return render(request, 'movie/movieseares.html', {'form': form, 'movies': movies})

def results(request, keyword, style):
    form = MovieForm()
    regk = ".*" + keyword + ".*"
    regs = ".*" + style + ".*"
    movies = Movies.objects(title=re.compile(regk, re.IGNORECASE), genres=re.compile(regs, re.IGNORECASE)).order_by('-rating')[:30]
    return render(request, 'movie/movieseares.html', {'form': form, 'movies': movies})
