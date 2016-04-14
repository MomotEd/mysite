from django import forms
from .models import Comments, Catalog, Car


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['comment']


class SearchForm(forms.Form):
    name = forms.CharField(max_length=30, required=False, label='name')
    mpg = forms.CharField(max_length=30, required=False, label='mpg from')
    mpg2 = forms.CharField(max_length=30, required=False, label='to')
    cylinders = forms.CharField(max_length=30, required=False, label='cylinders from')
    cylinders2 = forms.CharField(max_length=30, required=False, label='to')
    displacement = forms.CharField(max_length=30, required=False, label='displacement from')
    displacement2 = forms.CharField(max_length=30, required=False, label='to')
    horsepower = forms.CharField(max_length=30, required=False, label='horsepower from')
    horsepower2 = forms.CharField(max_length=30, required=False, label='to')
    weight = forms.CharField(max_length=30, required=False, label='weight from')
    weight2 = forms.CharField(max_length=30, required=False, label='to')
    acceleration = forms.CharField(max_length=30, required=False, label='acceleration from')
    acceleration2 = forms.CharField(max_length=30, required=False, label='to')
    year = forms.CharField(max_length=30, required=False, label='year from')
    year2 = forms.CharField(max_length=30, required=False, label='to')
    price = forms.CharField(max_length=30, required=False, label='price from')
    price2 = forms.CharField(max_length=30, required=False, label='to')
    origin = forms.CharField(max_length=30, required=False, label='origin from')
    origin2 = forms.CharField(max_length=30, required=False, label='to')
