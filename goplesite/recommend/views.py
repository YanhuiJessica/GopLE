from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import GenderForm

from .models import Users,Movies

import numpy as np

array_f = np.random.randint(50,size=20)
array_m = np.random.randint(50,size=20)

def index(request):
    movie_top = movies = Movies.objects().order_by('-rating')[:50]
    # print(type(movie_top))
    # for mov in movie_top:
    #     print(mov.title)
    #     print(mov.rating)
    if 'gender' not in request.session:
        request.session['gender'] = 'male'
    gender = request.session['gender']
    if gender == 'male':
        form = GenderForm(initial={'gender': True})
        array_m = [41,11,15,29,32,9,48,44,30,4,45,26,31,9,21,46,16,1,5,7]
        movie_m = []
        movieId = []
        i = 0
        for mov in movie_top:
            if i in array_m:
                movie_m.append(mov)
                print(mov.title)
                movieId.append(mov.movieId)
                #print(mov.rating)
            i = i + 1
        print(i)
        print(movieId)
        movie_res = Movies.objects(movieId__in=movieId)
        for m in movie_res:
            print(m.title)
    else:
        form = GenderForm(initial={'gender': False})
        array_f = [36,17,23,8,15,9,14,3,46,39,12,49,22,45,33,1,37,46,25,5]
        movie_f = []
        movieIds = []
        j = 0
        for mov in movie_top:
            if j in array_f:
                movie_f.append(mov)
                print(mov.title)
                print(mov.rating)
                movieIds.append(mov.movieId)
            j = j + 1
        print(j)
        print(movieIds)
        movie_res = Movies.objects(movieId__in=movieIds)
        for m in movie_res:
            print(m.title)
    return render(request, 'recommend/index.html', {'form': form, 'movies':movie_res})

def change_gender(request):
    if request.method == 'POST':
        form = GenderForm(request.POST)
        if form.is_valid():
            state = form.cleaned_data['gender']
            if state:
                request.session['gender'] = 'male'
            else:
                request.session['gender'] = 'female'
    return HttpResponseRedirect(reverse('recommend:index'))