from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import GenderForm

def index(request):
    if 'gender' not in request.session:
        request.session['gender'] = 'male'
    gender = request.session['gender']
    if gender == 'male':
        form = GenderForm(initial={'gender': True})
    else:
        form = GenderForm(initial={'gender': False})
    return render(request, 'recommend/index.html', {'form': form, 'gender': gender})

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