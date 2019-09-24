from django.shortcuts import render, get_object_or_404
from webapp.models import Product, CATEGORY_CHOICES


def index_view(request):
    products = Product.objects.all().exclude(remain=0).order_by('category', 'name')
    context = {'products': products}
    return render(request, 'index.html', context)


def product_detail_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product.html', context={
        'product': product
    })