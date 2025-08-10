#!/usr/bin/env python
import os
import sys
import django
from datetime import date

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')
django.setup()

from resume.models import Resume, Experience, Education, Skill

def create_sample_data():
    """Crear datos de ejemplo para el CV"""
    
    # Obtener o crear el CV principal
    resume, created = Resume.objects.get_or_create(
        defaults={
            'name': 'Steve Cardenas Ortiz',
            'email': 'steve.cardenas@example.com',
            'title': 'Ingegnere Elettronico',
            'summary': 'Ingegnere elettronico con esperienza nello sviluppo di sistemi embedded e automazione industriale.'
        }
    )
    
    if created:
        print("✅ CV creado")
    else:
        print("✅ CV ya existe")
    
    # Crear experiencias
    experiences_data = [
        {
            'company': 'TechCorp Italia',
            'position': 'Ingegnere Elettronico Senior',
            'location': 'Milano, Italia',
            'start_date': date(2020, 1, 1),
            'end_date': date(2023, 12, 31),
            'current': False,
            'description': 'Sviluppo di sistemi embedded per automazione industriale. Progettazione di circuiti di controllo per macchine industriali e implementazione di soluzioni IoT per il monitoraggio remoto.',
            'order': 1
        },
        {
            'company': 'Automazione Roma',
            'position': 'Ingegnere Elettronico',
            'location': 'Roma, Italia',
            'start_date': date(2018, 1, 1),
            'end_date': date(2020, 12, 31),
            'current': False,
            'description': 'Progettazione di circuiti di controllo per macchine industriali. Sviluppo di sistemi di automazione per linee di produzione e implementazione di protocolli di comunicazione industriali.',
            'order': 2
        },
        {
            'company': 'Elettronica Milano',
            'position': 'Tecnico Elettronico',
            'location': 'Milano, Italia',
            'start_date': date(2016, 1, 1),
            'end_date': date(2018, 12, 31),
            'current': False,
            'description': 'Manutenzione e riparazione di sistemi elettronici. Diagnostica di problemi hardware e software, sostituzione componenti e calibrazione di strumenti di misura.',
            'order': 3
        }
    ]
    
    for exp_data in experiences_data:
        exp, created = Experience.objects.get_or_create(
            resume=resume,
            company=exp_data['company'],
            position=exp_data['position'],
            defaults=exp_data
        )
        if created:
            print(f"✅ Experiencia creada: {exp.position} presso {exp.company}")
    
    # Crear educación
    education_data = [
        {
            'institution': 'Politecnico di Milano',
            'degree': 'Laurea Magistrale in Ingegneria Elettronica',
            'location': 'Milano, Italia',
            'start_date': date(2014, 9, 1),
            'end_date': date(2016, 7, 31),
            'current': False,
            'description': 'Specializzazione in sistemi embedded e microelettronica. Tesi di laurea su "Sviluppo di sistemi di controllo per automazione industriale".',
            'order': 1
        },
        {
            'institution': 'Università di Roma',
            'degree': 'Laurea Triennale in Ingegneria Elettronica',
            'location': 'Roma, Italia',
            'start_date': date(2011, 9, 1),
            'end_date': date(2014, 7, 31),
            'current': False,
            'description': 'Formazione di base in elettronica, fisica e matematica. Progetti di laboratorio su circuiti analogici e digitali.',
            'order': 2
        }
    ]
    
    for edu_data in education_data:
        edu, created = Education.objects.get_or_create(
            resume=resume,
            institution=edu_data['institution'],
            degree=edu_data['degree'],
            defaults=edu_data
        )
        if created:
            print(f"✅ Educación creada: {edu.degree} presso {edu.institution}")
    
    # Crear habilidades
    skills_data = [
        {'name': 'C', 'category': 'programming', 'proficiency': 9, 'order': 1},
        {'name': 'C++', 'category': 'programming', 'proficiency': 8, 'order': 2},
        {'name': 'Python', 'category': 'programming', 'proficiency': 7, 'order': 3},
        {'name': 'VHDL', 'category': 'programming', 'proficiency': 8, 'order': 4},
        {'name': 'Altium Designer', 'category': 'tools', 'proficiency': 9, 'order': 1},
        {'name': 'KiCad', 'category': 'tools', 'proficiency': 8, 'order': 2},
        {'name': 'Eagle', 'category': 'tools', 'proficiency': 7, 'order': 3},
        {'name': 'Arduino', 'category': 'microcontrollers', 'proficiency': 9, 'order': 1},
        {'name': 'STM32', 'category': 'microcontrollers', 'proficiency': 8, 'order': 2},
        {'name': 'PIC', 'category': 'microcontrollers', 'proficiency': 7, 'order': 3},
        {'name': 'I2C', 'category': 'protocols', 'proficiency': 9, 'order': 1},
        {'name': 'SPI', 'category': 'protocols', 'proficiency': 8, 'order': 2},
        {'name': 'UART', 'category': 'protocols', 'proficiency': 9, 'order': 3},
        {'name': 'CAN', 'category': 'protocols', 'proficiency': 7, 'order': 4},
        {'name': 'Proteus', 'category': 'software', 'proficiency': 8, 'order': 1},
        {'name': 'Multisim', 'category': 'software', 'proficiency': 7, 'order': 2},
        {'name': 'Italiano', 'category': 'languages', 'proficiency': 10, 'order': 1},
        {'name': 'Inglese', 'category': 'languages', 'proficiency': 8, 'order': 2},
        {'name': 'Spagnolo', 'category': 'languages', 'proficiency': 6, 'order': 3},
    ]
    
    for skill_data in skills_data:
        skill, created = Skill.objects.get_or_create(
            resume=resume,
            name=skill_data['name'],
            category=skill_data['category'],
            defaults=skill_data
        )
        if created:
            print(f"✅ Habilidad creada: {skill.name} ({skill.get_category_display()})")
    
    print("\n🎉 Datos de ejemplo creados exitosamente!")
    print(f"📊 Resumen:")
    print(f"   - CV: 1")
    print(f"   - Experiencias: {Experience.objects.count()}")
    print(f"   - Educación: {Education.objects.count()}")
    print(f"   - Habilidades: {Skill.objects.count()}")

if __name__ == '__main__':
    create_sample_data() 