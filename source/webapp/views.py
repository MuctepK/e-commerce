from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Product
from webapp.forms import ProductForm, SearchForm,CATEGORY_CHOICES


def index_view(request):
    products = Product.objects.all().exclude(remain=0).order_by('category', 'name')
    search_form = SearchForm()
    context = {'products': products,
               'search_form': search_form,
               'categories': CATEGORY_CHOICES}

    return render(request, 'index.html', context)


def product_detail_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product.html', context={
        'product': product
    })


def product_delete_view(request, pk):
    note = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete.html', context={'note': note})
    elif request.method == 'POST':
        note.delete()
        return redirect('index')


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


def product_search_view(request):
    pattern = request.GET.get('pattern')
    products = Product.objects.all().filter(name__icontains=pattern).\
        exclude(remain=0).order_by('category', 'name')
    search_form = SearchForm()
    context = {'products': products, 'search_form': search_form, 'categories':CATEGORY_CHOICES}
    return render(request, 'index.html', context)


def product_by_category_view(request, category):
    products = Product.objects.all().exclude(remain=0).filter(category=category).order_by('name')
    search_form = SearchForm()
    choose = [cat[1] for cat in CATEGORY_CHOICES if cat[0]==category]
    context = {'products': products, 'search_form': search_form, 'category':choose[0]}
    return render(request, 'product_category.html', context)