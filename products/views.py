from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, ProductCategory
from .forms import ProductForm


def all_products(request):
    """
    Display all products, including sorting and search functionality.

    - Supports sorting by name, category, and other attributes.
    - Filters products by selected category.
    - Implements a search feature to find products by name or description.

    Args:
        request (HttpRequest): The HTTP request containing potential
        filters or queries.

    Returns:
        HttpResponse: Renders the products page with a filtered
        and sorted list of products.
    """
    products = (
        Product.objects.all()
        .annotate(lower_name=Lower("name"))
        .order_by("lower_name")
    )
    query = None
    category_names = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sort = request.GET['sort']
            sortkey = (
                "lower_name" if sort == "name"
                else "category__name" if sort == "category"
                else sort
            )

            if sort == 'name':
                products = products.annotate(lower_name=Lower('name'))

            if (
                "direction" in request.GET
                and request.GET["direction"] == "desc"
            ):
                sortkey = f'-{sortkey}'

            products = products.order_by(sortkey)

        if 'category' in request.GET:
            category_names = request.GET['category'].split(',')
            products = products.filter(category__name__in=category_names)
            categories = ProductCategory.objects.filter(
                name__in=category_names
            )
        else:
            categories = ProductCategory.objects.all()

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request,
                    "You didn't enter any search criteria!"
                    )
                return redirect(reverse('products'))

            queries = (
                Q(name__icontains=query) |
                Q(description__icontains=query)
            )
            products = products.filter(queries)

    else:
        categories = ProductCategory.objects.all()

    # Enforce default sorting if no sorting is explicitly provided

    if not request.GET.get('sort'):
        products = products.order_by('lower_name')

    sort = request.GET.get('sort', 'name')
    direction = request.GET.get('direction', 'asc')
    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """
    Display details of a specific product.

    - Retrieves the product by its ID.
    - Selects three random products to display as related suggestions.

    Args:
        request (HttpRequest): The HTTP request object.
        product_id (int): The ID of the product to display.

    Returns:
        HttpResponse: Renders the product detail page with the product
        and related suggestions.
    """
    product = get_object_or_404(Product, pk=product_id)
    random_products = Product.objects.exclude(id=product.id).order_by('?')[:3]

    context = {
        'product': product,
        'random_products': random_products,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """
    Allow superusers to add a new product to the store.

    - Only accessible to store owners (superusers).
    - Handles form submission for new products.

    Args:
        request (HttpRequest): The HTTP request containing form data.

    Returns:
        HttpResponse: Renders the add product page or redirects to the
        product detail page on success.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                        request,
                        'Failed to add product. '
                        'Please ensure the form is valid.'
                        )
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """
    Allow superusers to edit an existing product.

    - Retrieves the product by ID.
    - Handles form submission to update the product.

    Args:
        request (HttpRequest): The HTTP request containing form data.
        product_id (int): The ID of the product to edit.

    Returns:
        HttpResponse: Renders the edit product page or redirects to the
        updated product detail page.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                "Failed to update product. Please ensure the form is valid."
            )

    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """
    Allow superusers to delete a product.

    - Retrieves the product by ID.
    - Deletes the product from the database.

    Args:
        request (HttpRequest): The HTTP request object.
        product_id (int): The ID of the product to delete.

    Returns:
        HttpResponse: Redirects to the products page with a success message.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
