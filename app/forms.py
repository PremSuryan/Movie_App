from django import forms
from .models import insert_movie,comments

class insert_form(forms.ModelForm):
    class Meta:
        model = insert_movie
        fields = '__all__'
        widgets = {'release_date' : forms.DateInput(attrs={'type':'date'}),'blog_date':forms.DateInput(attrs={'type':'date'})}

class comment_movie(forms.ModelForm):
    class Meta:
        model = comments
        exclude = ['date']