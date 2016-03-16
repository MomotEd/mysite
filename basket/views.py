from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from cars.models import Car

class ShowBasket(TemplateView):
    template_name = 'basket.html'

    def get(self, request, *args, **kwargs):
        return super(ShowBasket, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ShowBasket, self).get_context_data(**kwargs)
        basket = self.request.session.get('basket', {})
        context.update({'basket': basket})
        return context


class AddToBasket(TemplateView):
    template_name = 'basket.html'

    def get(self, request, *args, **kwargs):
        return super(AddToBasket, self).get(request, *args, **kwargs)

    def get_context_data(self, car_id=None, **kwargs):
        context = super(AddToBasket, self).get_context_data(**kwargs)
        basket = self.request.session.get('basket', {})
        car_id = car_id
        car =get_object_or_404(Car, pk=car_id)
        if basket.get(car) is not None:
            basket
