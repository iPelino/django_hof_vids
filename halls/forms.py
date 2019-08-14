from django import forms
from .models import Video


# model Form
class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['url']
        labels = {'url': 'Youtube Url'}


# django forms
class SearchForm(forms.Form):
    search_term = forms.CharField(max_length=255, label='Search for Videos')


