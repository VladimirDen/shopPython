from django.shortcuts import render
from django.views.generic import DetailView, View
from .models import Boiler, Pomp, Category, LatestProducts
from .mixins import CategoryDetailMixin


class BaseView(View):

    def get(self, request, *args, **kwargs):
        categories = Category.objects.get_categories_for_left_sidebar()
        products = LatestProducts.objects.get_products_for_main_page(
            'boiler', 'pomp', with_respect_to='boiler'
        )
        context = {
            'categories': categories,
            'products': products
        }
        return render(request, 'index.html', context)


class ProductDetailView(CategoryDetailMixin, DetailView):
    CT_MODEL_MODEL_CLASS = {
        'boiler': Boiler,
        'pomp': Pomp
    }

    def dispatch(self, request, *args, **kwargs):
        self.model = self.CT_MODEL_MODEL_CLASS[kwargs['ct_model']]
        self.queryset = self.model._base_manager.all()
        return super().dispatch(request, *args, **kwargs)

    context_object_name = 'product'
    template_name = 'product_detail.html'
    slug_url_kwarg = 'slug'


class CategoryDetailView(CategoryDetailMixin, DetailView):
    model = Category
    queryset = Category.objects.all()
    context_object_name = 'category'
    template_name = 'category_detail.html'
    slug_url_kwarg = 'slug'
