from django import forms

class GenderForm(forms.Form):
    gender = forms.BooleanField(label='', required=False)