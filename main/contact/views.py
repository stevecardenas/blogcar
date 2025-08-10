from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact

def contact_view(request):
    """Vista para el formulario de contacto"""
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        if name and email and subject and message:
            Contact.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            messages.success(request, 'Messaggio inviato con successo!')
            return redirect('contact')
        else:
            messages.error(request, 'Per favore compila tutti i campi.')
    
    context = {
        'title': 'Contatto'
    }
    return render(request, 'contact/contact.html', context) 