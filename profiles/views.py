from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order


@login_required
def profile(request):
    """
    Display and manage the user's profile.

    - Retrieves the user's profile.
    - Allows users to update their profile details via a form submission.
    - Displays the user's order history.

    If the request method is POST:
        - Validates and saves the updated profile information.
        - Displays a success or error message based on validation.

    If the request method is GET:
        - Prepopulates the profile form with existing user data.
        - Retrieves all orders associated with the user.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Renders the profile page with the profile form and order history.
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)

    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


@login_required
def order_history(request, order_number):
    """
    Display a past order's details.

    - Retrieves an order by its order number.
    - Displays an informational message to indicate that this is a past order.
    - Uses the checkout success template for displaying order details.

    Args:
        request (HttpRequest): The HTTP request object.
        order_number (str): The unique identifier of the order.

    Returns:
        HttpResponse: Renders the checkout success template with order details.
    """
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
