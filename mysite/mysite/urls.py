"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from users import views as userviews
from cars import views as carviews


urlpatterns = [
    url(r'^user/', include('users.urls')),
    url(r'^$',  carviews.IndexView.as_view(), name='cars'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', userviews.login),
    url(r'^registration/', userviews.registration),
    url(r'^car/', include('cars.urls', namespace="cars")),
    url(r'^basket/', include('basket.urls', namespace="basket")),
    url(r'^downloadcars', carviews.catalog_add_func, name='downloadcars')
]
