from django.shortcuts import render
from .models import Faq

# Create your views here.


def faq(request):
    """
    Display the FAQ page.

    Retrieves all FAQ entries from the database and passes them
    to the template for rendering.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Renders the FAQ template with all FAQs.
    """

    context = {
        'faqs': Faq.objects.all(),
    }

    return render(request, 'faq/faq.html', context)
