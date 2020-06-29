from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import re
from .forms import IDForm
from .models import Users, Movies

def index(request):
    form = IDForm()
    return render(request, 'userhis/searchis.html', {'form': form})

def results(request, usrid):
    import urllib.request, json

    form = IDForm()
    user_ = Users.objects.filter(userId=usrid)[0]
    watchedMovies = user_.watchedMovies
    movieId = []
    for movie in watchedMovies:
            movieId.append(movie.movieId)
    movies = Movies.objects(movieId__in = movieId)
    imgpaths = []
    for id_ in movieId:
        try:
            data = urllib.request.urlopen('https://api.themoviedb.org/3/movie/' + str(id_) + '/images?api_key=93e48491c391483da7b34d5e0e570a9a')
        except urllib.error.HTTPError as e:
            imgpaths.append('/9PCsWrw1GvrZkrd1GCxRqscgZu0.jpg')
            continue
        data = json.loads(data.read())['backdrops']
        if len(data):
            data = data[0]['file_path']
        else:
            data = '/9PCsWrw1GvrZkrd1GCxRqscgZu0.jpg'
        imgpaths.append(data)
    return render(request, 'userhis/searchres.html', {'form': form, 'user': user_, 'movies': zip(movies, watchedMovies, imgpaths)})

def search(request):
    if request.method == 'POST':
        form = IDForm(request.POST)
        if form.is_valid():
            user_id = form.cleaned_data['user_id']
            return HttpResponseRedirect(reverse('userhis:results', args=(user_id, )))
    return render(request, 'userhis/searchres.html', {'form': form})