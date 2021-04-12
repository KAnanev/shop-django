from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from catalog.models import Product, Category


class ProductListView(ListView):
    paginate_by = 2
    context_object_name = 'products_list'

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['category'])
        return Product.objects.filter(category__slug=self.category.slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context









