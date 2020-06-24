from django import forms

class IDForm(forms.Form):
    user_id = forms.IntegerField(label='', widget=forms.TextInput({'placeholder':'输入用户 ID 查看观看历史…',}))