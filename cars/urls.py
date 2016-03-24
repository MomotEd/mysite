from django.conf.urls import url

from .views import CarDetailView


urlpatterns = [
    url(r'^car-detail/(?P<car_id>\d+)/$', CarDetailView.as_view(),
        name='car_detail'),
]