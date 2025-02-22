from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_contact_page, name='contact'),
    path('contact-success/', views.contact_success, name='contact_success'),
]
