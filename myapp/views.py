from django.shortcuts import render
from .models import ContactMessage

def home(request):
    return render(request, 'myapp/home.html', {
        'page_title': 'Home',
        'active_page': 'home'
    })

def about(request):
    return render(request, 'myapp/about.html', {
        'page_title': 'About Me',
        'active_page': 'about'
    })

def contact(request):
    success = False
    error = None
    submitted_data = {}

    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        subject = request.POST.get('subject', 'General Inquiry').strip()
        message = request.POST.get('message', '').strip()

        submitted_data = {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message,
        }

        if not name or not email or not message:
            error = "Please fill in all required fields (Name, Email, Message)."
        else:
            try:
                ContactMessage.objects.create(
                    name=name,
                    email=email,
                    subject=subject,
                    message=message
                )
                print(f"\n=== NEW CONTACT MESSAGE ===")
                print(f"From: {name} <{email}>")
                print(f"Subject: {subject}")
                print(f"Message: {message}")
                print(f"===========================\n")
                success = True
                submitted_data = {}
            except Exception as e:
                error = f"An error occurred while saving your message: {str(e)}"

    return render(request, 'myapp/contact.html', {
        'page_title': 'Contact Me',
        'active_page': 'contact',
        'success': success,
        'error': error,
        'submitted_data': submitted_data
    })
