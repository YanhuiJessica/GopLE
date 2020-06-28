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
    form = IDForm()
    return render(request, 'userhis/searchres.html', {'form': form})

def search(request):
    if request.method == 'POST':
        form = IDForm(request.POST)
        if form.is_valid():
            user_id = form.cleaned_data['user_id']
            print(user_id)
            user_ = Users.objects.filter(userId=user_id)[0]
            watchedMovies=user_.watchedMovies
            movieId=[]
            for movie in watchedMovies:
                 movieId.append(movie.movieId)
            movies=Movies.objects(movieId__in= movieId)
            # return HttpResponseRedirect(reverse('userhis:results', args=(user_id, )))
    return render(request, 'userhis/searchres.html',{ 'user':user_,'movies': zip(movies,watchedMovies)})