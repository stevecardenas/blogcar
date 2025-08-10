from django.core.management.base import BaseCommand
from projects.models import Category, Project

class Command(BaseCommand):
    help = 'Crea datos de ejemplo para proyectos y categorías'

    def handle(self, *args, **options):
        # Crear categorías
        categories_data = [
            {
                'name': 'Sistemi Embedded',
                'description': 'Progetti di microcontrollori e sistemi embedded'
            },
            {
                'name': 'Automazione Industriale',
                'description': 'Sistemi di controllo e automazione per l\'industria'
            },
            {
                'name': 'IoT e Smart Home',
                'description': 'Dispositivi IoT e sistemi per casa intelligente'
            },
            {
                'name': 'Elettronica di Potenza',
                'description': 'Circuiti di potenza e conversione energetica'
            }
        ]

        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(
                name=cat_data['name'],
                defaults={'description': cat_data['description']}
            )
            if created:
                self.stdout.write(f'Categoria creata: {category.name}')

        # Crear proyectos
        projects_data = [
            {
                'title': 'Sistema di Controllo Temperatura',
                'description': 'Sistema embedded per il controllo della temperatura in serre industriali. Utilizza sensori digitali e attuatori PWM per mantenere la temperatura ottimale.',
                'technologies': 'Arduino, Sensori DS18B20, Relè SSR, LCD I2C',
                'category_name': 'Sistemi Embedded',
                'is_featured': True
            },
            {
                'title': 'PLC per Automazione Linea Produttiva',
                'description': 'Sistema PLC personalizzato per l\'automazione di una linea di produzione. Include controllo di motori, sensori di sicurezza e interfaccia HMI.',
                'technologies': 'Siemens S7-1200, TIA Portal, SCADA, Profinet',
                'category_name': 'Automazione Industriale',
                'is_featured': True
            },
            {
                'title': 'Smart Home Hub',
                'description': 'Hub centralizzato per la gestione di dispositivi smart home. Supporta protocolli Zigbee, Z-Wave e WiFi.',
                'technologies': 'ESP32, Zigbee, Z-Wave, MQTT, Node.js',
                'category_name': 'IoT e Smart Home',
                'is_featured': False
            },
            {
                'title': 'Inverter Solare 3kW',
                'description': 'Inverter per impianti fotovoltaici residenziali. Conversione DC-AC con MPPT e monitoraggio remoto.',
                'technologies': 'IGBT, DSP, MPPT, WiFi, App Mobile',
                'category_name': 'Elettronica di Potenza',
                'is_featured': True
            },
            {
                'title': 'Sistema di Monitoraggio Energia',
                'description': 'Sistema IoT per il monitoraggio del consumo energetico in tempo reale. Dashboard web e notifiche via email.',
                'technologies': 'STM32, Sensori di Corrente, ESP8266, Django',
                'category_name': 'IoT e Smart Home',
                'is_featured': False
            }
        ]

        for proj_data in projects_data:
            category = Category.objects.get(name=proj_data['category_name'])
            project, created = Project.objects.get_or_create(
                title=proj_data['title'],
                defaults={
                    'description': proj_data['description'],
                    'technologies': proj_data['technologies'],
                    'category': category,
                    'is_featured': proj_data['is_featured']
                }
            )
            if created:
                self.stdout.write(f'Progetto creato: {project.title}')

        self.stdout.write(
            self.style.SUCCESS('Dati di esempio creati con successo!')
        ) 