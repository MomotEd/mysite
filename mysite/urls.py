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
    url(r'^search/', carviews.SearchView.as_view(),name='search'),
    url(r'^i18n/', include('django.conf.urls.i18n')),
]
