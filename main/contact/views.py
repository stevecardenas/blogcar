from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .models import Contact

def contact_view(request):
    """Vista para el formulario de contacto"""
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        if name and email and subject and message:
            # Guardar el mensaje en la base de datos
            contact = Contact.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            
            try:
                # Enviar email al administrador
                admin_subject = f"Nuovo messaggio di contatto: {subject}"
                admin_message = f"""
Nuovo messaggio ricevuto dal sito web:

Nome: {name}
Email: {email}
Oggetto: {subject}

Messaggio:
{message}

---
Questo messaggio è stato inviato automaticamente dal form di contatto.
                """
                
                # Enviar email al administrador
                send_mail(
                    subject=admin_subject,
                    message=admin_message,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.EMAIL_HOST_USER],  # Email del administrador
                    fail_silently=False,
                )
                
                # Enviar email de confirmación al usuario
                user_subject = "Conferma ricezione del tuo messaggio"
                user_message = f"""
Gentile {name},

Grazie per avermi contattato! Ho ricevuto il tuo messaggio e ti risponderò al più presto.

Dettagli del messaggio:
- Oggetto: {subject}
- Data: {contact.created_at.strftime('%d/%m/%Y alle %H:%M')}

Il tuo messaggio:
{message}

Cordiali saluti,
Steve Cardenas Ortiz
Ingegnere Elettronico

---
Questo è un messaggio automatico, non rispondere a questa email.
                """
                
                send_mail(
                    subject=user_subject,
                    message=user_message,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[email],  # Email del usuario
                    fail_silently=False,
                )
                
                messages.success(request, 'Messaggio inviato con successo! Ti ho inviato una email di conferma.')
                
            except Exception as e:
                # Si hay error en el envío de email, guardar el mensaje pero mostrar error
                messages.warning(request, f'Messaggio salvato ma c\'è stato un problema con l\'invio dell\'email. Errore: {str(e)}')
            
            return redirect('contact')
        else:
            messages.error(request, 'Per favore compila tutti i campi.')
    
    context = {
        'title': 'Contatto'
    }
    return render(request, 'contact/contact.html', context) 