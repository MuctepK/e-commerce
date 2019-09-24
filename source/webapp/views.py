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


def product_update_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        form = ProductForm(data={'name': product.name,
                                 'description': product.description,
                                 'category': product.category,
                                 'remain': product.remain,
                                 'price': product.price})
        return render(request, 'update.html', context={'note': product,
                                                       'form': form
                                                       })
    elif request.method == 'POST':
        form = ProductForm(data=request.POST)
        if form.is_valid():
            product.name = form.cleaned_data['name']
            product.description = form.cleaned_data['description']
            product.category = form.cleaned_data['category']
            product.remain = form.cleaned_data['remain']
            product.price = form.cleaned_data['price']
            product.save()
            return redirect('index')
        else:
            return render(request, 'update.html', context={
                'form': form, 'note': product
            })