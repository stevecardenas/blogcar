from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.conf import settings

class Command(BaseCommand):
    help = 'Testa il sistema di invio email'

    def add_arguments(self, parser):
        parser.add_argument(
            '--email',
            type=str,
            help='Email di destinazione per il test',
        )

    def handle(self, *args, **options):
        test_email = options['email'] or settings.EMAIL_HOST_USER
        
        if not test_email:
            self.stdout.write(
                self.style.ERROR('❌ Email di destinazione non configurata. Usa --email o configura EMAIL_HOST_USER')
            )
            return

        self.stdout.write('🧪 Testando il sistema di email...')
        
        try:
            # Email de prueba
            subject = 'Test Sistema Email - Portfolio'
            message = f"""
Questo è un email di test per verificare che il sistema di invio funzioni correttamente.

Configurazione attuale:
- Host: {settings.EMAIL_HOST}
- Porta: {settings.EMAIL_PORT}
- TLS: {settings.EMAIL_USE_TLS}
- SSL: {settings.EMAIL_USE_SSL}
- From: {settings.DEFAULT_FROM_EMAIL}
- To: {test_email}

Se ricevi questo email, il sistema funziona correttamente!

---
Test generato automaticamente dal comando: python manage.py test_email
            """
            
            send_mail(
                subject=subject,
                message=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[test_email],
                fail_silently=False,
            )
            
            self.stdout.write(
                self.style.SUCCESS(f'✅ Email di test inviato con successo a {test_email}')
            )
            
            if settings.DEBUG:
                self.stdout.write(
                    self.style.WARNING('⚠️  MODO SVILUPPO: Controlla la console del server per vedere l\'email')
                )
            else:
                self.stdout.write(
                    self.style.SUCCESS('📧 MODO PRODUZIONE: Email inviato realmente')
                )
                
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'❌ Errore nell\'invio dell\'email: {str(e)}')
            )
            
            # Mostrar información de debug
            self.stdout.write('\n🔍 Informazioni di debug:')
            self.stdout.write(f'EMAIL_BACKEND: {settings.EMAIL_BACKEND}')
            self.stdout.write(f'EMAIL_HOST: {settings.EMAIL_HOST}')
            self.stdout.write(f'EMAIL_PORT: {settings.EMAIL_PORT}')
            self.stdout.write(f'EMAIL_USE_TLS: {settings.EMAIL_USE_TLS}')
            self.stdout.write(f'EMAIL_HOST_USER: {settings.EMAIL_HOST_USER}')
            self.stdout.write(f'DEFAULT_FROM_EMAIL: {settings.DEFAULT_FROM_EMAIL}')
            self.stdout.write(f'DEBUG: {settings.DEBUG}')
