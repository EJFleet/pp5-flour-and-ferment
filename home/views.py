from django.shortcuts import render

# Create your views here.


def index(request):
    """
    Display the homepage.

    This view renders the main landing page of the website.

    """
    return render(request, 'home/index.html')


def about(request):
    """
    Display the About page.

    This view renders the page that provides information about
    the company.

    """
    return render(request, 'home/about.html')
