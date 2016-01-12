from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.login),
    url(r'^activate/(?P<secretkey>.+)/$', views.activateuser),
    url(r'^registration/', views.registration),
]