from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Product
from webapp.forms import ProductForm


def index_view(request):
    products = Product.objects.all().exclude(remain=0).order_by('category', 'name')
    context = {'products': products}
    return render(request, 'index.html', context)


def product_detail_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product.html', context={
        'product': product
    })

def product_create_view(request):
    if request.method == 'GET':
        form = ProductForm()
        return render(request, 'create.html', context=
        {
            'form': form
        })
    elif request.method == 'POST':
        form = ProductForm(data=request.POST)
        if not form.is_valid():
            return render(request, 'create.html', context={'form': form})
        Product.objects.create(name=form.cleaned_data['name'],
                            description=form.cleaned_data['description'],
                            category=form.cleaned_data['category'],
                            remain = form.cleaned_data['remain'],
                            price = form.cleaned_data['price'])
        return redirect('index')