from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.login),
    url(r'^activate/(?P<secret_key>.+)/$', views.activateuser),
    url(r'^$', views.registration),
]