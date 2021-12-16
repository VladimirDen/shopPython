from django.shortcuts import render
from django.views.generic import DetailView
from .models import Boiler, Pomp



def createPage(request):
    return render(request, 'mainchop/index.html', {})


class ProductDetailView(DetailView):

    CT_MODEL_MODEL_CLASS = {
        'boiler': Boiler,
        'pomp': Pomp
    }

    def dispatch(self, request, *args, **kwargs):
        self.model = self.CT_MODEL_MODEL_CLASS[kwargs['ct_model']]
        self.queryset = self.model._base_manager.all()
        return super().dispatch(request, *args, **kwargs)

    context_object_name = 'product'
    template_name = 'mainchop/product_detail.html'
    slug_url_kwarg = 'slug'
