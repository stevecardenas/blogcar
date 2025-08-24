#!/usr/bin/env bash
# exit on error
set -o errexit

echo "=== INICIANDO BUILD EN RENDER ==="

# Instalar dependencias
echo "Instalando dependencias..."
pip install -r requirements.txt

# Verificar que Django funciona
echo "Verificando Django..."
cd main
python manage.py check

# Mostrar migraciones pendientes
echo "Mostrando migraciones..."
python manage.py showmigrations

# Ejecutar migraciones
echo "Aplicando migraciones..."
python manage.py migrate

# Verificar migraciones aplicadas
echo "Verificando migraciones aplicadas..."
python manage.py showmigrations

# Crear superusuario automáticamente
echo "Creando superusuario..."
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'admin123456') if not User.objects.filter(username='admin').exists() else None" | python manage.py shell

# Verificar que el superusuario se creó
echo "Verificando superusuario..."
python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); print('Superusuarios:', User.objects.filter(is_superuser=True).count())"

# Recolectar archivos estáticos
echo "Recolectando archivos estáticos..."
python manage.py collectstatic --no-input

echo "=== BUILD COMPLETADO ==="
