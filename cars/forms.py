from django import forms
from .models import Comments, Catalog,Car


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['comment']


class SearchForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['name', 'mpg', 'cylinders', 'displacement', 'horsepower',
                  'weight', 'acceleration', 'year', 'price', 'origin']