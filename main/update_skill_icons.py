#!/usr/bin/env python
import os
import sys
import django
from datetime import date

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')
django.setup()

from resume.models import Skill

def update_skill_icons():
    """Actualizar iconos de habilidades existentes con iconos más específicos"""
    
    # Mapeo de habilidades específicas con iconos personalizados
    icon_mapping = {
        # Lenguajes de programación
        'Python': 'bi-filetype-py',
        'C++': 'bi-filetype-cpp',
        'C#': 'bi-filetype-cs',
        'Java': 'bi-filetype-java',
        'JavaScript': 'bi-filetype-js',
        'HTML': 'bi-filetype-html',
        'CSS': 'bi-filetype-css',
        'PHP': 'bi-filetype-php',
        'SQL': 'bi-database',
        'VHDL': 'bi-diagram-3',
        'Verilog': 'bi-diagram-3',
        
        # Microcontroladores
        'Arduino': 'bi-cpu',
        'STM32': 'bi-cpu',
        'PIC': 'bi-cpu',
        'Raspberry Pi': 'bi-cpu',
        'ESP32': 'bi-wifi',
        'ESP8266': 'bi-wifi',
        
        # Protocolos de comunicación
        'I2C': 'bi-diagram-2',
        'SPI': 'bi-diagram-2',
        'UART': 'bi-usb',
        'CAN': 'bi-diagram-2',
        'Ethernet': 'bi-hdd-network',
        'Bluetooth': 'bi-bluetooth',
        'WiFi': 'bi-wifi',
        
        # Herramientas CAD
        'Altium Designer': 'bi-layers',
        'KiCad': 'bi-layers',
        'Eagle': 'bi-layers',
        'Proteus': 'bi-layers',
        'Multisim': 'bi-layers',
        
        # Instrumentos de medición
        'Oscilloscope': 'bi-speedometer',
        'Multimeter': 'bi-speedometer',
        'Oscilloscopio': 'bi-speedometer',
        'Multimetro': 'bi-speedometer',
        
        # Software de simulación
        'MATLAB': 'bi-graph-up',
        'Simulink': 'bi-diagram-3',
        'LabVIEW': 'bi-graph-up',
        
        # Software CAD 3D
        'AutoCAD': 'bi-layers',
        'SolidWorks': 'bi-box',
        'Fusion 360': 'bi-box',
        
        # Software de oficina
        'Excel': 'bi-table',
        'Word': 'bi-file-text',
        'PowerPoint': 'bi-easel',
        
        # Software de diseño gráfico
        'Photoshop': 'bi-palette',
        'Illustrator': 'bi-palette',
        
        # Idiomas
        'Italiano': 'bi-flag',
        'Inglese': 'bi-flag',
        'Español': 'bi-flag',
        'English': 'bi-flag',
        'Spanish': 'bi-flag',
        
        # Soldadura
        'Soldering': 'bi-tools',
        'Saldatura': 'bi-tools',
    }
    
    updated_count = 0
    
    for skill in Skill.objects.all():
        # Buscar coincidencia exacta en el mapeo
        if skill.name in icon_mapping:
            skill.icon = icon_mapping[skill.name]
            skill.save()
            print(f"✅ Actualizado: {skill.name} -> {skill.icon}")
            updated_count += 1
        else:
            # Usar el icono automático del modelo
            auto_icon = skill.get_icon()
            if auto_icon != 'bi-gear':  # Solo actualizar si no es el icono por defecto
                skill.icon = auto_icon
                skill.save()
                print(f"✅ Auto-actualizado: {skill.name} -> {skill.icon}")
                updated_count += 1
    
    print(f"\n🎉 Actualización completada!")
    print(f"📊 Total de habilidades actualizadas: {updated_count}")
    print(f"📊 Total de habilidades en la base de datos: {Skill.objects.count()}")

if __name__ == '__main__':
    update_skill_icons() 