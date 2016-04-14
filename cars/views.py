from django.shortcuts import HttpResponse, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from .forms import CommentForm, SearchForm
from .models import Car
import pymongo
from utils import get_mongo_database, get_params_from_request


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
        context.update({'form': form, 'descriptions': car})
        return context


class SearchView(TemplateView):
    template_name = 'search.html'

    def get(self, request, *args, **kwargs):
        db = get_mongo_database()
        mongocars = db.cars
        print(request.GET)
        form = SearchForm(request.GET)
        res = []
        context = {'form': form}
        if request.method == 'GET':
            if len(request.GET) > 0:
                searching_parametr = get_params_from_request(request.GET)
                print(searching_parametr)
                a = {'mpg': {'$gt': '10', '$lt': '20'}}
                print(a)
                for car in mongocars.find(searching_parametr):
                    car_result = Car.objects.get(id=car.get('sql_id'))
                    res.append(car_result)
                # Pagination
        paginator = Paginator(res, 10)
        page = self.request.GET.get('page')
        try:
            cars = paginator.page(page)
        except PageNotAnInteger:
            cars = paginator.page(1)
        except EmptyPage:
            cars = paginator.page(paginator.num_pages)
        context.update({
            'search_res': cars,
        })
        return render(request, 'search.html', context)
