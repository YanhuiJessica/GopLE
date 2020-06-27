from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import MovieForm
import re
import json 
from django.http import HttpResponse
from .models import Movies

def index(request):
    form = MovieForm()
    return render(request, 'movie/moviesearch.html', {'form': form})

# B：根据输入的关键词，查询电影名字里有关键词的电影；
# 这个任务大概要做个分页？
def search(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            keyword = form.cleaned_data['keyword']
            print(keyword)
            reg=".*"+keyword+".*"


            movies = Movies.objects(title=re.compile(reg, re.IGNORECASE)).order_by('-rating')[:30]


            for movie in movies:
                print(movie.title)
                print(movie.rating)
            # form.movie=movies
            
            style = form.cleaned_data['style']
    return render(request, 'movie/movieseares.html', {'form': form})

# C：查询某一风格最受欢迎的20 部电影；
# 不选择风格(默认) 则返回所有电影的Top20
def tops(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
    if form.is_valid():
        keyword = form.cleaned_data['keyword']
        print(keyword)
        reg=".*"+keyword+".*"


        movies = Movies.objects(genres=re.compile(reg, re.IGNORECASE)).order_by('-rating')[:20]
        
        
        for movie in movies:
            print(movie.title)
            print(movie.rating)
        form.movie=movies
        
        style = form.cleaned_data['style']
    return render(request, 'movie/movieseares.html', {'form': form})

def results(request):
    form = MovieForm()
    return render(request, 'movie/movieseares.html', {'form': form})