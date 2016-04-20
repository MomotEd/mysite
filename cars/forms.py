from django import forms
from .models import Comments
from django.utils.translation import ugettext_lazy as _


class SearchForm(forms.Form):
    name = forms.CharField(max_length=30, required=False, label=_("name"))
    mpg = forms.CharField(max_length=30, required=False, label=_('mpg from'))
    mpg_to = forms.CharField(max_length=30, required=False, label=_('to'))
    cylinders = forms.CharField(max_length=30, required=False, label=_('cylinders from'))
    cylinders_to = forms.CharField(max_length=30, required=False, label=_('to'))
    displacement = forms.CharField(max_length=30, required=False, label=_('displacement from'))
    displacement_to = forms.CharField(max_length=30, required=False, label=_('to'))
    horsepower = forms.CharField(max_length=30, required=False, label=_('horsepower from'))
    horsepower_to = forms.CharField(max_length=30, required=False, label=_('to'))
    weight = forms.CharField(max_length=30, required=False, label=_('weight from'))
    weight_to = forms.CharField(max_length=30, required=False, label=_('to'))
    acceleration = forms.CharField(max_length=30, required=False, label=_('acceleration from'))
    acceleration_to = forms.CharField(max_length=30, required=False, label=_('to'))
    year = forms.CharField(max_length=30, required=False, label=_('year from'))
    year_to = forms.CharField(max_length=30, required=False, label=_('to'))
    price = forms.CharField(max_length=30, required=False, label=_('price from'))
    price_to = forms.CharField(max_length=30, required=False, label=_('to'))
    origin = forms.CharField(max_length=30, required=False, label=_('origin from'))
    origin_to = forms.CharField(max_length=30, required=False, label=_('to'))


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['comment']