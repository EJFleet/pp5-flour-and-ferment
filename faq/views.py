from django.shortcuts import render
from .models import Faq

# Create your views here.


def faq(request):

    """ A view to return the faq page """
    
    context = {
        'faqs': Faq.objects.all(),
    }

    return render(request, 'faq/faq.html', context)

