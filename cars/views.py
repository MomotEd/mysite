from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, DetailView, ListView

from .forms import CommentForm
from .models import Car


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        car_qs = Car.objects.all()

        # Pagination
        paginator = Paginator(car_qs, 12)
        page = self.request.GET.get('page')
        try:
            cars = paginator.page(page)
        except PageNotAnInteger:
            cars = paginator.page(1)
        except EmptyPage:
            cars = paginator.page(paginator.num_pages)
        context.update({
            'cars': cars,
        })
        return context


class CarDetailView(TemplateView):
    template_name = 'Item_page.html'
    car = None

    def get(self, request, *args, **kwargs):
        car_id = kwargs.get('car_id')
        self.car = get_object_or_404(Car, pk=car_id)
        return super(CarDetailView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CarDetailView, self).get_context_data(**kwargs)
        form = CommentForm()
        car_id = kwargs.get('car_id')
        car = Car.objects.get(id=car_id)
        context.update({'form': form, 'descriptions':car})
        return context



