from django.conf.urls import url
from views import AddToBasket,ShowBasket

urlpatterns = [
    url(r'^car-detail/(?P<car_id>\d+)/addbasket/', AddToBasket.as_view(),
        name='addbasket'),
    url(r'^basket/(?P<action>.+)',ShowBasket.as_view(), name='showbasket'),
]