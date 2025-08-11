from django.db import models

# Create your models here.

class SocialMedia(models.Model):
    """Modelo para almacenar las redes sociales de forma dinámica"""
    name = models.CharField(max_length=50, verbose_name="Nombre")
    url = models.URLField(verbose_name="URL del perfil")
    icon = models.CharField(max_length=50, verbose_name="Icono (Bootstrap Icons)")
    order = models.PositiveIntegerField(default=0, verbose_name="Orden")
    is_active = models.BooleanField(default=True, verbose_name="Activo")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Social Media"
        verbose_name_plural = "Social Media"
        ordering = ['order', 'name']
        indexes = [
            models.Index(fields=['is_active', 'order']),
        ]

    def __str__(self):
        return self.name

class HomeContent(models.Model):
    """Modelo para el contenido dinámico de la página de inicio"""
    
    # Sección Header
    header_badge = models.CharField(max_length=200, default="Sistemi Embedded · Automazione · IoT", verbose_name="Badge del header")
    header_subtitle = models.CharField(max_length=200, default="Posso aiutare la tua azienda a", verbose_name="Subtítulo del header")
    header_title = models.CharField(max_length=200, default="Crescere e innovare", verbose_name="Título principal")
    
    # Sección About
    about_title = models.CharField(max_length=200, default="Chi Sono", verbose_name="Título de la sección")
    about_subtitle = models.CharField(max_length=200, default="Mi chiamo Steve Cardenas Ortiz e aiuto le aziende a crescere.", verbose_name="Subtítulo de la sección")
    about_description = models.TextField(default="Ingegnere elettronico specializzato in sistemi embedded, automazione industriale e IoT. Con oltre 8 anni di esperienza nello sviluppo di soluzioni elettroniche innovative per diverse industrie.", verbose_name="Descripción completa")
    
    # Botones
    resume_button_text = models.CharField(max_length=50, default="Resume", verbose_name="Texto del botón Resume")
    projects_button_text = models.CharField(max_length=50, default="Projects", verbose_name="Texto del botón Projects")
    
    # Configuración
    is_active = models.BooleanField(default=True, verbose_name="¿Está activo?")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Última actualización")
    
    class Meta:
        verbose_name = "Contenuto della Pagina Iniziale"
        verbose_name_plural = "Contenuti della Pagina Iniziale"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Contenido de inicio - {self.created_at.strftime('%d/%m/%Y')}"
    
    @classmethod
    def get_active_content(cls):
        """Obtiene el contenido activo más reciente"""
        return cls.objects.filter(is_active=True).first()

class SiteSettings(models.Model):
    """Modelo para configuraciones generales del sitio"""
    site_name = models.CharField(max_length=100, default="Steve Cardenas Ortiz", verbose_name="Nombre del sitio")
    site_title = models.CharField(max_length=200, default="Steve Cardenas Ortiz - Ingegnere Elettronico", verbose_name="Título del sitio")
    site_description = models.TextField(
        default="Steve Cardenas Ortiz - Ingegnere Elettronico specializzato in sistemi embedded, automazione industriale e IoT. Portfolio professionale con progetti e competenze.",
        verbose_name="Descripción del sitio"
    )
    profession = models.CharField(max_length=100, default="Ingegnere Elettronico", verbose_name="Profesión")
    copyright_text = models.CharField(max_length=200, default="Copyright © Steve Cardenas Ortiz 2024", verbose_name="Texto de copyright")
    is_active = models.BooleanField(default=True, verbose_name="¿Está activo?")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Última actualización")

    class Meta:
        verbose_name = "Impostazioni del Sito"
        verbose_name_plural = "Impostazioni del Sito"
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['is_active']),
        ]

    def __str__(self):
        return f"Configuración del sitio - {self.created_at.strftime('%d/%m/%Y')}"

    @classmethod
    def get_active_settings(cls):
        """Obtiene la configuración activa"""
        return cls.objects.filter(is_active=True).first()

class Navigation(models.Model):
    """Modelo para enlaces de navegación dinámicos"""
    name = models.CharField(max_length=50, verbose_name="Nombre del enlace")
    url_name = models.CharField(max_length=50, verbose_name="Nombre de la URL (Django)")
    display_name = models.CharField(max_length=50, verbose_name="Nombre a mostrar")
    order = models.PositiveIntegerField(default=0, verbose_name="Orden")
    is_active = models.BooleanField(default=True, verbose_name="¿Está activo?")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Última actualización")

    class Meta:
        verbose_name = "Elemento di Navigazione"
        verbose_name_plural = "Elementi di Navigazione"
        ordering = ['order', 'name']
        indexes = [
            models.Index(fields=['is_active', 'order']),
        ]

    def __str__(self):
        return self.display_name

    @classmethod
    def get_active_navigation(cls):
        """Obtiene los enlaces de navegación activos"""
        return cls.objects.filter(is_active=True).order_by('order')
