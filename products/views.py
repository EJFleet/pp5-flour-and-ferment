from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, ProductCategory
from .forms import ProductForm

# Create your views here.


def all_products(request):

    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    category_names = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sort = request.GET['sort']
            sortkey = 'lower_name' if sort == 'name' else 'category__name' if sort == 'category' else sort

            if sort == 'name':
                products = products.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET and request.GET['direction'] == 'desc':
                sortkey = f'-{sortkey}'

            products = products.order_by(sortkey)

        if 'category' in request.GET:
            category_names = request.GET['category'].split(',')
            products = products.filter(category__name__in=category_names)
            categories = ProductCategory.objects.filter(name__in=category_names)
        else:
            categories = ProductCategory.objects.all()

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)
        
    else:
        categories = ProductCategory.objects.all()    

    current_sorting = f'{sort}_{direction}' if sort else 'name_asc'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):

    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)
    random_products = Product.objects.exclude(id=product.id).order_by('?')[:3]


    context = {
        'product': product,
        'random_products': random_products,
    }

    return render(request, 'products/product_detail.html', context)


def add_product(request):
    """ Add a product to the store """
    form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)



