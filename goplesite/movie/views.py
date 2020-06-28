from django.http import HttpResponseRedirect, HttpResponse
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
            regk = ".*" + keyword + ".*"
            style = form.cleaned_data['style']
            regs = ".*" + style + ".*"
            movies = Movies.objects(title=re.compile(regk, re.IGNORECASE), genres=re.compile(regs, re.IGNORECASE)).order_by('-rating')[:30]

            for movie in movies:
                print(movie.title)
                print(movie.rating)
            # return HttpResponseRedirect(reverse('movie:results'))
            print(movies)
    return render(request, 'movie/movieseares.html', {'movies': movies})

def results(request):
    form = MovieForm()
    return render(request, 'movie/movieseares.html', {'movies': movies})