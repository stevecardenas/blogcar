from django.db import models

# Create your models here.

class Terms(models.Model):
    """Modello per i termini e condizioni"""
    title = models.CharField(max_length=200, verbose_name="Titolo")
    content = models.TextField(verbose_name="Contenuto")
    is_active = models.BooleanField(default=True, verbose_name="Attivo")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data di creazione")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Data di aggiornamento")

    class Meta:
        verbose_name = "Termini e Condizioni"
        verbose_name_plural = "Termini e Condizioni"
        ordering = ['-updated_at']

    def __str__(self):
        return self.title

class Privacy(models.Model):
    """Modello per l'informativa sulla privacy"""
    title = models.CharField(max_length=200, verbose_name="Titolo")
    content = models.TextField(verbose_name="Contenuto")
    is_active = models.BooleanField(default=True, verbose_name="Attivo")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data di creazione")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Data di aggiornamento")

    class Meta:
        verbose_name = "Informativa sulla Privacy"
        verbose_name_plural = "Informativa sulla Privacy"
        ordering = ['-updated_at']

    def __str__(self):
        return self.title

class Cookies(models.Model):
    """Modello per l'informativa sui cookie"""
    title = models.CharField(max_length=200, verbose_name="Titolo")
    content = models.TextField(verbose_name="Contenuto")
    is_active = models.BooleanField(default=True, verbose_name="Attivo")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data di creazione")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Data di aggiornamento")

    class Meta:
        verbose_name = "Informativa sui Cookie"
        verbose_name_plural = "Informativa sui Cookie"
        ordering = ['-updated_at']

    def __str__(self):
        return self.title
