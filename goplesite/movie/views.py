from django.shortcuts import render

from .forms import MovieForm

def index(request):
    form = MovieForm()
    return render(request, 'movie/moviesearch.html', {'form': form})

def search(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            keyword = form.cleaned_data['keyword']
            style = form.cleaned_data['style']
    return render(request, 'movie/moviesearch.html', {'form': form})

def results(request):
    form = MovieForm()
    return render(request, 'movie/movieseares.html', {'form': form})