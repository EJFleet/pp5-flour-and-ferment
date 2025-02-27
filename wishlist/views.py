from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from products.models import Product
from .models import Wishlist, WishlistItem


@login_required
def view_wishlist(request):
    """
    Display the user's wishlist.

    - Retrieves or creates a wishlist for the authenticated user.
    - Fetches all wishlist items associated with the wishlist.
    - Renders the wishlist template with the retrieved items.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Renders the wishlist page with the user's wishlist items.
    """
    wishlist, _ = Wishlist.objects.get_or_create(user=request.user)
    wishlist_items = wishlist.wishlist_items.all()
    
    context = {
        'wishlist_items': wishlist_items
    }
    
    return render(request, 'wishlist/wishlist.html', context)


@login_required
def add_to_wishlist(request, item_id):
    """
    Add a product to the user's wishlist.

    - Retrieves the product by its ID.
    - Gets or creates a wishlist for the authenticated user.
    - Checks if the product is already in the wishlist:
        - If not, adds it and displays a success message.
        - If already present, displays an info message.

    Args:
        request (HttpRequest): The HTTP request object containing the redirect URL.
        item_id (int): The ID of the product to be added.

    Returns:
        HttpResponseRedirect: Redirects to the previous page or the wishlist page.
    """
    product = get_object_or_404(Product, pk=item_id)
    wishlist, _ = Wishlist.objects.get_or_create(user=request.user)

    _, created = WishlistItem.objects.get_or_create(
        wishlist=wishlist, product=product
    )

    if created:
        messages.success(request, f'{product.name} has been added to your wishlist.')
    else:
        messages.info(request, f'{product.name} is already in your wishlist.')

    return redirect(request.POST.get('redirect_url', 'view_wishlist'))


@login_required
def remove_from_wishlist(request, item_id):
    """
    Remove a product from the user's wishlist.

    - Retrieves the user's wishlist.
    - Attempts to delete the wishlist item by its product ID.
    - Displays a success message if the item was removed.
    - Displays a warning message if the item was not found.

    Args:
        request (HttpRequest): The HTTP request object.
        item_id (int): The ID of the product to be removed.

    Returns:
        HttpResponseRedirect: Redirects to the wishlist page.
    """
    wishlist, _ = Wishlist.objects.get_or_create(user=request.user)

    # Try to delete the wishlist item
    deleted, _ = WishlistItem.objects.filter(wishlist=wishlist, product_id=item_id).delete()

    if deleted:
        messages.success(request, 'The item has been removed from your wishlist.')
    else:
        messages.warning(request, 'The item was not found in your wishlist.')

    return redirect(reverse('wishlist'))
