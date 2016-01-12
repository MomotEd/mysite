from django import forms
from models import User

class LoginForm(forms.Form):

    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError('No user with such username')
        user = User.objects.get(username=username)
        if not user.is_active:
            raise forms.ValidationError('User is not active')
        return username



class RegForm(forms.ModelForm):

   class Meta:
       model = User
       fields = ['username', 'email', 'password']

