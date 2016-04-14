from django.shortcuts import render, get_object_or_404
from django.contrib import auth
from .forms import LoginForm, RegForm
from .models import SecretKey
from django.http import HttpResponse
from django.template import RequestContext


def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return render(request,'index.html')
            else:
                return HttpResponse('fail to login '+username +' '+ password)
    context = {'form': form}
    return render(request,'login.html', context)



def registration(request):
    form = RegForm()
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            email = form.cleaned_data.get('email')
            user.username = username
            user.is_active = False
            user.email = email
            user.set_password(password)
            user.save()
    context = RequestContext(request, {'form': form})
    return render(request, 'registration.html', context)


def activateuser(request, secretkey):
    sc = get_object_or_404(SecretKey, secretkey=secretkey)
    user = sc.user
    user.is_active = True
    user.save()
    sc.delete()
    return HttpResponse('Your account activated')

