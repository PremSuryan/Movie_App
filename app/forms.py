from django import forms
from .models import insert_movie,comments
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class insert_form(forms.ModelForm):
    class Meta:
        model = insert_movie
        fields = '__all__'
        widgets = {'release_date' : forms.DateInput(attrs={'type':'date'}),'blog_date':forms.DateInput(attrs={'type':'date'})}

class comment_movie(forms.ModelForm):
    class Meta:
        model = comments
        exclude = ['date']

# class MovieForm(forms.ModelForm):
#     class Meta:
#         model = Movie  # Replace with your actual model
#         fields = ['title', 'description', 'file']  # Replace with your actual fields

#     def __init__(self, *args, **kwargs):
#         super(MovieForm, self).__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.form_method = 'post'
#         self.helper.add_input(Submit('submit', 'Submit'))        