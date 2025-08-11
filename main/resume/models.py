from django.db import models

class Resume(models.Model):
    """Modelo para el CV de Steve Cardenas Ortiz"""
    name = models.CharField(max_length=100, verbose_name="Nome")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=20, blank=True, verbose_name="Telefono")
    title = models.CharField(max_length=200, verbose_name="Titolo Professionale")
    summary = models.TextField(verbose_name="Riassunto")
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data Creazione")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Data Aggiornamento")
    
    class Meta:
        verbose_name = "Curriculum Vitae"
        verbose_name_plural = "Curriculum Vitae"
    
    def __str__(self):
        return f"CV di {self.name}"
    
    def save(self, *args, **kwargs):
        # Si es el primer CV, usar valores por defecto
        if not self.pk and Resume.objects.count() == 0:
            self.name = self.name or "Steve Cardenas Ortiz"
            self.email = self.email or "steve.cardenas@example.com"
            self.title = self.title or "Ingegnere Elettronico"
            self.summary = self.summary or "Ingegnere elettronico con esperienza nello sviluppo di sistemi embedded e automazione industriale."
        super().save(*args, **kwargs)

class Experience(models.Model):
    """Modelo para experiencias laborales"""
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='experiences', verbose_name="CV")
    company = models.CharField(max_length=200, verbose_name="Azienda")
    position = models.CharField(max_length=200, verbose_name="Posizione")
    location = models.CharField(max_length=200, verbose_name="Località")
    start_date = models.DateField(verbose_name="Data Inizio")
    end_date = models.DateField(null=True, blank=True, verbose_name="Data Fine")
    current = models.BooleanField(default=False, verbose_name="Posizione Attuale")
    description = models.TextField(verbose_name="Descrizione")
    order = models.PositiveIntegerField(default=0, verbose_name="Ordine")
    
    class Meta:
        verbose_name = "Esperienza Lavorativa"
        verbose_name_plural = "Esperienze Lavorative"
        ordering = ['-order', '-start_date']
    
    def __str__(self):
        return f"{self.position} presso {self.company}"
    
    def get_period(self):
        """Obtener el período formateado"""
        if self.current:
            return f"{self.start_date.year} - Presente"
        elif self.end_date:
            return f"{self.start_date.year} - {self.end_date.year}"
        else:
            return f"{self.start_date.year}"

class Education(models.Model):
    """Modelo para educación"""
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='educations', verbose_name="CV")
    institution = models.CharField(max_length=200, verbose_name="Istituzione")
    degree = models.CharField(max_length=200, verbose_name="Titolo di Studio")
    location = models.CharField(max_length=200, verbose_name="Località")
    start_date = models.DateField(verbose_name="Data Inizio")
    end_date = models.DateField(null=True, blank=True, verbose_name="Data Fine")
    current = models.BooleanField(default=False, verbose_name="Studi in Corso")
    description = models.TextField(verbose_name="Descrizione")
    order = models.PositiveIntegerField(default=0, verbose_name="Ordine")
    
    class Meta:
        verbose_name = "Formazione"
        verbose_name_plural = "Formazioni"
        ordering = ['-order', '-start_date']
    
    def __str__(self):
        return f"{self.degree} presso {self.institution}"
    
    def get_period(self):
        """Obtener el período formateado"""
        if self.current:
            return f"{self.start_date.year} - Presente"
        elif self.end_date:
            return f"{self.start_date.year} - {self.end_date.year}"
        else:
            return f"{self.start_date.year}"

class Skill(models.Model):
    """Modelo para habilidades"""
    SKILL_CATEGORIES = [
        ('programming', 'Linguaggi di Programmazione'),
        ('tools', 'Strumenti CAD'),
        ('microcontrollers', 'Microcontrollori'),
        ('protocols', 'Protocolli di Comunicazione'),
        ('software', 'Software di Simulazione'),
        ('languages', 'Lingue'),
        ('other', 'Altro'),
    ]
    
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='skills', verbose_name="CV")
    name = models.CharField(max_length=200, verbose_name="Nome Competenza")
    category = models.CharField(max_length=20, choices=SKILL_CATEGORIES, verbose_name="Categoria")
    description = models.TextField(blank=True, verbose_name="Descrizione")
    proficiency = models.PositiveIntegerField(default=5, verbose_name="Livello di Competenza (1-10)")
    order = models.PositiveIntegerField(default=0, verbose_name="Ordine")
    icon = models.CharField(max_length=50, blank=True, verbose_name="Icona Bootstrap", 
                           help_text="Classe CSS dell'icona Bootstrap (es: bi-code-slash, bi-cpu, bi-wifi)")
    
    class Meta:
        verbose_name = "Competenza"
        verbose_name_plural = "Competenze"
        ordering = ['category', 'order', 'name']
    
    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"
    
    def get_proficiency_display(self):
        """Obtener el nivel de competencia como texto"""
        if self.proficiency >= 9:
            return "Eccellente"
        elif self.proficiency >= 7:
            return "Avanzato"
        elif self.proficiency >= 5:
            return "Intermedio"
        elif self.proficiency >= 3:
            return "Base"
        else:
            return "Principiante"
    
    def get_icon(self):
        """Obtener el icono apropiado para la habilidad"""
        # Si hay un icono personalizado, usarlo
        if self.icon:
            return self.icon
        
        # Iconos automáticos basados en el nombre y categoría
        name_lower = self.name.lower()
        
        if self.category == 'programming':
            if 'python' in name_lower:
                return 'bi-filetype-py'
            elif 'c++' in name_lower or 'cpp' in name_lower:
                return 'bi-filetype-cpp'
            elif 'c#' in name_lower or 'csharp' in name_lower:
                return 'bi-filetype-cs'
            elif 'java' in name_lower:
                return 'bi-filetype-java'
            elif 'javascript' in name_lower or 'js' in name_lower:
                return 'bi-filetype-js'
            elif 'html' in name_lower:
                return 'bi-filetype-html'
            elif 'css' in name_lower:
                return 'bi-filetype-css'
            elif 'php' in name_lower:
                return 'bi-filetype-php'
            elif 'sql' in name_lower:
                return 'bi-database'
            elif 'vhdl' in name_lower or 'verilog' in name_lower:
                return 'bi-diagram-3'
            else:
                return 'bi-code-slash'
        
        elif self.category == 'microcontrollers':
            if 'arduino' in name_lower:
                return 'bi-cpu'
            elif 'stm32' in name_lower:
                return 'bi-cpu'
            elif 'pic' in name_lower:
                return 'bi-cpu'
            elif 'raspberry' in name_lower or 'pi' in name_lower:
                return 'bi-cpu'
            elif 'esp32' in name_lower or 'esp8266' in name_lower:
                return 'bi-wifi'
            else:
                return 'bi-cpu'
        
        elif self.category == 'protocols':
            if 'i2c' in name_lower or 'spi' in name_lower or 'can' in name_lower:
                return 'bi-diagram-2'
            elif 'uart' in name_lower or 'serial' in name_lower:
                return 'bi-usb'
            elif 'ethernet' in name_lower:
                return 'bi-hdd-network'
            elif 'bluetooth' in name_lower:
                return 'bi-bluetooth'
            elif 'wifi' in name_lower or 'wireless' in name_lower:
                return 'bi-wifi'
            else:
                return 'bi-wifi'
        
        elif self.category == 'languages':
            if any(lang in name_lower for lang in ['italiano', 'italian', 'inglese', 'english', 'español', 'spanish', 'français', 'french', 'deutsch', 'german']):
                return 'bi-flag'
            else:
                return 'bi-globe'
        
        elif self.category == 'tools':
            if any(tool in name_lower for tool in ['altium', 'kicad', 'eagle', 'proteus', 'multisim']):
                return 'bi-layers'
            elif any(tool in name_lower for tool in ['oscilloscope', 'oscilloscopio', 'multimeter', 'multimetro']):
                return 'bi-speedometer'
            elif 'soldering' in name_lower or 'saldatura' in name_lower:
                return 'bi-tools'
            else:
                return 'bi-tools'
        
        elif self.category == 'software':
            if 'matlab' in name_lower or 'labview' in name_lower:
                return 'bi-graph-up'
            elif 'simulink' in name_lower:
                return 'bi-diagram-3'
            elif 'autocad' in name_lower:
                return 'bi-layers'
            elif 'solidworks' in name_lower or 'fusion' in name_lower:
                return 'bi-box'
            elif 'excel' in name_lower:
                return 'bi-table'
            elif 'word' in name_lower:
                return 'bi-file-text'
            elif 'powerpoint' in name_lower:
                return 'bi-easel'
            elif 'photoshop' in name_lower or 'illustrator' in name_lower:
                return 'bi-palette'
            else:
                return 'bi-laptop'
        
        else:
            return 'bi-gear' 