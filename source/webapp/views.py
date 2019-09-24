from django.shortcuts import render
from webapp.models import Product, CATEGORY_CHOICES


def index_view(request):
    products = Product.objects.all().exclude(remain=0).order_by('category', 'name')
    context = {'products': products}
    return render(request, 'index.html', context)
