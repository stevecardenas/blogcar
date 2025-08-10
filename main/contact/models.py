from django.db import models

class Contact(models.Model):
    """Modelo para mensajes de contacto"""
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = "Messaggio"
        verbose_name_plural = "Messaggi"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Messaggio da {self.name} - {self.subject}" 