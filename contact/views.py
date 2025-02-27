from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages

def view_contact_page(request):
    """
    Handle displaying and processing the contact form.

    - If the request method is POST:
        - Retrieves form data (name, email, subject, message).
        - Validates that all fields are filled.
        - Saves the message as a Contact object with the default status of 'unread'.
        - Displays a success message and redirects to the success page.
        - If any field is missing, an error message is shown.

    - If the request method is GET:
        - Displays the contact form.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Renders the contact form template or redirects to the success page upon form submission.
    """
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
