from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages

def view_contact_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if name and email and subject and message:
            contact = Contact(
                name=name,
                email=email,
                subject=subject,
                message=message,
                status='unread'  # Default status
            )
            contact.save()
            
            messages.success(request, "Your message has been sent successfully!")
            return redirect('contact_success')
        else:
            messages.error(request, "All fields are required. Please try again.")

    return render(request, 'contact/contact.html')


def contact_success(request):
    return render(request, 'contact/contact_success.html')
