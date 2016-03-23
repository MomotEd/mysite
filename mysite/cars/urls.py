from django.conf.urls import url

from .views import CarDetailView
from basket.views import AddToBasket


urlpatterns = [
    url(r'^car-detail/(?P<car_id>\d+)/$', CarDetailView.as_view(),
        name='car_detail'),
    url(r'^car-detail/(?P<car_id>\d+)/addbasket/', AddToBasket.as_view(),
        name='addbasket'),
]