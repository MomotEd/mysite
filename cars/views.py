from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, DetailView, ListView

from .forms import CommentForm
from .models import Car, Comments


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


# def index(request):
#     cars = Car.objects.all()
#     paginator = Paginator(cars, 12)
#     page = request.GET.get('page')
#     try:
#         Cars = paginator.page(page)
#     except PageNotAnInteger:
#         Cars = paginator.page(1)
#     except EmptyPage:
#         Cars = paginator.page(paginator.num_pages)
#
#     return render(request,'index.html', {'Cars':Cars,'Categories':Categories})



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
        context.update({'form': form, 'Descriptions':car})
        return context


#def item(request,CarId):
#
#    categories = Category.objects.order_by('name')
#    caritem = Car.objects.get(id=CarId)
#    itemCategories=CategoryList.objects.filter(Car=caritem)
#    list = []
#    for cat in itemCategories:
#        string = str(cat.Category)+': ' + str(cat.Value)
#        list.append(string)
#
#    form = CommentForm()
#    if request.method == 'POST':
#        form = CommentForm(request.POST)
#        if form.is_valid():
#            text = form.cleaned_data.get('Comment')
#            Comments.objects.create_comment(text,caritem)
#
#   comments=Comments.objects.filter(Car=caritem)
#    context = RequestContext(request, {'Categories':categories,'Descriptions':list,'Comments':comments, 'form': form})
#    return render(request, 'Item_page.html',context)


# def add_product_to_basket(request,CarId):
#
#    page = request.META['HTTP_REFERER ']
#    caritem = Car.objects.get(id=CarId)
#    item = {'car':caritem}
#    basket = request.session.get('basket', {})
#    if basket:
#       basket.update([item])
#    else:
#       request.session['basket'] = {'item':item}
#    return redirect(page)



