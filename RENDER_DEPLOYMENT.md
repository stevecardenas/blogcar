# 🚀 Guía de Despliegue en Render

## 📋 Requisitos Previos

- ✅ Cuenta en [Render.com](https://render.com) (gratuita)
- ✅ Repositorio en GitHub/GitLab
- ✅ Proyecto Django configurado

## 🔧 Archivos de Configuración Creados

### ✅ Archivos Necesarios para Render:

1. **`requirements.txt`** - Dependencias de Python
2. **`build.sh`** - Script de construcción
3. **`runtime.txt`** - Versión de Python
4. **`main/main/settings.py`** - Configurado para producción

## 🚀 Pasos para Desplegar

### **Paso 1: Subir Código a GitHub**

```bash
# Asegúrate de estar en la rama main
git add .
git commit -m "Preparar proyecto para despliegue en Render"
git push origin main
```

### **Paso 2: Crear Cuenta en Render**

1. Ve a [render.com](https://render.com)
2. Regístrate con tu cuenta de GitHub
3. Conecta tu repositorio

### **Paso 3: Crear Web Service**

1. **Dashboard de Render** → **"New +"** → **"Web Service"**
2. **Connect Repository** → Selecciona tu repositorio
3. **Configure Web Service:**

```
Name: portfolio-steve (o el nombre que prefieras)
Environment: Python 3
Region: Frankfurt (EU Central) [Recomendado]
Branch: main
Root Directory: (dejar vacío)
Build Command: ./build.sh
Start Command: gunicorn main.main.wsgi:application
```

### **Paso 4: Configurar Variables de Entorno**

En la sección **"Environment Variables"** de tu servicio:

```bash
# Django Settings
SECRET_KEY=tu-secret-key-super-segura
DEBUG=False
ALLOWED_HOSTS=tu-app.onrender.com

# Database (se configura automáticamente)
DATABASE_URL=postgresql://... (Render lo proporciona)

# Static Files
STATIC_URL=/static/
MEDIA_URL=/media/

# Email Configuration (OPCIONAL - para funcionalidad de contacto)
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=tu-email@gmail.com
EMAIL_HOST_PASSWORD=tu-app-password
DEFAULT_FROM_EMAIL=tu-email@gmail.com
EMAIL_SUBJECT_PREFIX=[Portfolio]

# Production Settings
SECURE_SSL_REDIRECT=True
SECURE_HSTS_SECONDS=31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS=True
SECURE_HSTS_PRELOAD=True
```

### **Paso 5: Crear Base de Datos PostgreSQL**

1. **Dashboard** → **"New +"** → **"PostgreSQL"**
2. **Configure Database:**
   ```
   Name: portfolio-db
   Database: portfolio_db
   User: portfolio_user
   Region: Frankfurt (EU Central)
   ```
3. **Copiar DATABASE_URL** y agregarla a las variables de entorno

### **Paso 6: Desplegar**

1. **"Create Web Service"**
2. Render comenzará el build automáticamente
3. Esperar 5-10 minutos para completar

## 🔍 Verificación del Despliegue

### **1. Verificar Build Logs**
- Revisar que no hay errores en el build
- Confirmar que las migraciones se ejecutaron

### **2. Verificar la Aplicación**
- Visitar tu URL: `https://tu-app.onrender.com`
- Verificar que la página carga correctamente

### **3. Crear Superusuario**
```bash
# En Render Dashboard → Shell
python main/manage.py createsuperuser
```

### **4. Probar Funcionalidades**
- Navegar por las páginas
- Probar el formulario de contacto
- Verificar que los archivos estáticos cargan

## 🛠️ Solución de Problemas Comunes

### **Error: "ModuleNotFoundError"**
- Verificar que todas las dependencias están en `requirements.txt`
- Revisar el build log para errores específicos

### **Error: "Database connection failed"**
- Verificar que `DATABASE_URL` está configurada correctamente
- Confirmar que la base de datos PostgreSQL está creada

### **Error: "Static files not found"**
- Verificar que `STATIC_ROOT` está configurado
- Confirmar que `collectstatic` se ejecutó en el build

### **Error: "SECRET_KEY not set"**
- Agregar `SECRET_KEY` a las variables de entorno
- Generar una nueva clave secreta

## 📊 Monitoreo y Mantenimiento

### **Logs**
- **Render Dashboard** → Tu servicio → **"Logs"**
- Revisar logs para errores y debugging

### **Variables de Entorno**
- **Render Dashboard** → Tu servicio → **"Environment"**
- Actualizar variables según sea necesario

### **Deploy Automático**
- Cada push a `main` activará un nuevo deploy
- Configurar ramas específicas si es necesario

## 🔒 Seguridad en Producción

### **Variables Sensibles**
- ✅ `SECRET_KEY` - Clave secreta única
- ✅ `DEBUG=False` - Deshabilitar modo debug
- ✅ `ALLOWED_HOSTS` - Solo dominios permitidos

### **HTTPS**
- ✅ Render proporciona HTTPS automáticamente
- ✅ `SECURE_SSL_REDIRECT=True` - Redirección forzada

### **Base de Datos**
- ✅ PostgreSQL con conexión segura
- ✅ Variables de entorno para credenciales

## 📈 Optimizaciones

### **Performance**
- ✅ WhiteNoise para archivos estáticos
- ✅ Compresión automática
- ✅ Cache configurado

### **Escalabilidad**
- ✅ Gunicorn como servidor WSGI
- ✅ Configuración para múltiples workers

## 🎯 Checklist de Despliegue

- [ ] Código subido a GitHub
- [ ] Cuenta en Render creada
- [ ] Web Service configurado
- [ ] Base de datos PostgreSQL creada
- [ ] Variables de entorno configuradas
- [ ] Build exitoso
- [ ] Aplicación accesible
- [ ] Superusuario creado
- [ ] Funcionalidades probadas
- [ ] Emails configurados (opcional)

## 🚀 URLs Importantes

- **Aplicación:** `https://tu-app.onrender.com`
- **Admin:** `https://tu-app.onrender.com/admin/`
- **Contacto:** `https://tu-app.onrender.com/contact/`

---

**¡Tu portfolio estará en línea en minutos! 🎉**
