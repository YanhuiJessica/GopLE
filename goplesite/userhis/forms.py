from django import forms

class IDForm(forms.Form):
    user_id = forms.IntegerField(label='', error_messages={'invalid': '用户 ID 应当为纯数字'}, widget=forms.TextInput({'placeholder':'输入用户 ID 查看观看历史…',}))