from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from products.models import Product
from .models import Wishlist, WishlistItem
# Create your views here.


def view_wishlist(request):

    """ A view to return the wishlist page """

    wishlist, _ = Wishlist.objects.get_or_create(user=request.user)
    wishlist_items = wishlist.wishlist_items.all()
    context = {
        'wishlist_items': wishlist_items
        }
    
    return render(request, 'wishlist/wishlist.html', context)


def add_to_wishlist(request, item_id):

    """ Add a product to the wishlist """

    product = get_object_or_404(Product, pk=item_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)

    _, created = WishlistItem.objects.get_or_create(
        wishlist=wishlist, product=product
    )

    if created:
        messages.success(request, f'{product.name} has been added to your wishlist.')
    else:
        messages.info(request, f'{product.name} is already in your wishlist.')

    return redirect(request.POST.get('redirect_url', 'view_wishlist'))


def remove_from_wishlist(request, item_id):
    """Remove a product from the wishlist."""
    wishlist, _ = Wishlist.objects.get_or_create(user=request.user)

    # Try to delete the wishlist item
    deleted, _ = WishlistItem.objects.filter(wishlist=wishlist, product_id=item_id).delete()

    if deleted:
        messages.success(request, 'The item has been removed from your wishlist.')
    else:
        messages.warning(request, 'The item was not found in your wishlist.')

    return redirect(reverse('view_wishlist'))