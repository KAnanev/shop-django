from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from catalog.forms import ReviewForm
from catalog.models import Product, Category, Review


class ProductListView(ListView):
    paginate_by = 9
    context_object_name = 'products_list'

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['category_slug'])
        return Product.objects.filter(category__slug=self.category.slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context


class ProductDetail(DetailView):
    model = Product
    slug_field = 'slug'
    slug_url_kwarg = 'product_slug'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data()
        context['form'] = ReviewForm
        return context

    def post(self, request, *args, **kwargs):
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.product = super(ProductDetail, self).get_object()
            new_review.save()

            self.object = self.get_object()
            context = super(ProductDetail, self).get_context_data(**kwargs)
            context['form'] = ReviewForm
            return self.render_to_response(context=context)

        else:
            self.object = self.get_object()
            context = super(ProductDetail, self).get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response(context=context)










