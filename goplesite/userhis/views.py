from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import IDForm

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
            return HttpResponseRedirect(reverse('userhis:results', args=(user_id, )))
    return render(request, 'userhis/searchres.html', {'form': form})