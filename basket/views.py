from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse
from cars.models import Car
from django.shortcuts import get_object_or_404
from utils import get_mongo_database


class ShowBasket(TemplateView):
    template_name = 'basket.html'

    def get_context_data(self, **kwargs):
        context = super(ShowBasket, self).get_context_data(**kwargs)
        action = kwargs.get('action')
        if self.request.session.get('basket'):
            basket = self.request.session.get('basket')
            car_list = []
            total = 0
            for i in basket:
                car_id = basket[int(i)-1]
                car = get_object_or_404(Car, pk=car_id)
                car_list.append(car)
                total += int(car.price)
            context.update({'carlist': car_list, 'total': total})
        else:
            self.request.session.update({'basket': []})
        if action == "clear":
            self.request.session.update({'basket': []})
            context.update({'carlist': [], 'total': 0})
        if action == "buy":
            car_id = kwargs.get('car_id')
            car = get_object_or_404(Car, pk=car_id)
            car.delete()
            db = get_mongo_database()
            mongocars = db.cars
            mongocars.remove({"sql_id": car_id})
            self.request.session.update({'basket': []})
            context.update({'carlist': [], 'total': 0})
        return context


class AddToBasket(TemplateView):
    template_name = 'basket.html'

    def get(self, request, *args, **kwargs):
        car_id = kwargs.get('car_id')
        context = super(AddToBasket, self).get_context_data(**kwargs)
        if request.session.get('basket'):
            if not car_id in request.session['basket']:
                request.session['basket'].append(car_id)
            else:
                context.update({'status': 'already added'})
        else:
            request.session.update({'basket': []})
            request.session['basket'].append(car_id)
        url_to_redirect = reverse('cars:car_detail', kwargs={'car_id': car_id})
        return redirect(url_to_redirect)