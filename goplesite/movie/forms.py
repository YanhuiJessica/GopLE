from django import forms

movie_styles = [('Drama', 'Drama'), ('Comedy', 'Comedy'), ('Thriller', 'Thriller'), ('Romance', 'Romance'), ('Action', 'Action'), ('Crime', 'Crime'), ('Horror', 'Horror'), ('Documentary', 'Documentary'), ('Adventure', 'Adventure'), ('Sci-Fi', 'Sci-Fi'), ('Mystery', 'Mystery'), ('Fantasy', 'Fantasy'), ('War', 'War'), ("Children's", "Children's"), ('Musical', 'Musical'), ('Animation', 'Animation'), ('Western', 'Western'), ('Film-Noir', 'Film-Noir')]

class MovieForm(forms.Form):
    keyword = forms.CharField(required=False, label='', max_length=200, widget=forms.TextInput({'placeholder':'输入关键词查找相关电影…',}))
    style = forms.ChoiceField(required=False, choices=movie_styles)