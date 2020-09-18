from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import GenderForm
from .models import Users, Movies

import numpy as np

array_f = np.random.randint(50,size=20)
array_m = np.random.randint(50,size=20)

def get_imgpaths(moviesId):
    import urllib.request, json

    imgpaths = []
    for mid in moviesId:
        # try:
        #     data = urllib.request.urlopen('https://api.themoviedb.org/3/movie/' + str(mid.movieId) + '/images?api_key=93e48491c391483da7b34d5e0e570a9a')
        # except urllib.error.HTTPError as e:
        #     imgpaths.append('/9PCsWrw1GvrZkrd1GCxRqscgZu0.jpg')
        #     continue
        # data = json.loads(data.read())['backdrops']
        # if len(data):
        #     data = data[0]['file_path']
        # else:
        #     data = '/9PCsWrw1GvrZkrd1GCxRqscgZu0.jpg'
        data = '/9PCsWrw1GvrZkrd1GCxRqscgZu0.jpg'
        imgpaths.append(data)
    return imgpaths

def index(request):
    if 'gender' not in request.session:
        request.session['gender'] = 'male'
    gender = request.session['gender']
    if gender == 'male':
        form = GenderForm(initial={'gender': True})
        movie_res = Movies.objects().order_by('-mavg','+movieId')[:50]
        # for m in movie_res:
        #     print(m.title)
        #     print(m.rating)
        #     print(m.mavg)
    else:
        form = GenderForm(initial={'gender': False})
        movie_res = Movies.objects().order_by('-favg','+movieId')[:50]
    return render(request, 'recommend/index.html', {'form': form, 'movies': zip(movie_res, get_imgpaths(movie_res))})

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