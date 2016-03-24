from django import forms
from .models import Comments, Catalog


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['comment']
