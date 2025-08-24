# 🚀 Guía de Despliegue en Render (SQLite GRATIS)

## 📋 Requisitos Previos

- ✅ Cuenta en [Render.com](https://render.com) (gratuita)
- ✅ Repositorio en GitHub/GitLab
- ✅ Proyecto Django configurado

## 🔧 Archivos de Configuración Creados

### ✅ Archivos Necesarios para Render:

1. **`requirements.txt`** - Dependencias de Python
2. **`build.sh`** - Script de construcción
3. **`runtime.txt`** - Versión de Python
4. **`main/main/settings.py`** - Configurado para producción con SQLite

## 🚀 Pasos para Desplegar

### **Paso 1: Subir Código a GitHub**

```bash
# Asegúrate de estar en la rama main
git add .
git commit -m "Preparar proyecto para despliegue en Render con SQLite"
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
Start Command: ./start.sh
```

**Si el comando anterior no funciona, prueba estas alternativas:**

**Opción 2 (Recomendada si la primera falla):**
```
Start Command: ./start_simple.sh
```

**Opción 3 (Comando directo):**
```
Start Command: cd /opt/render/project/src/main && gunicorn main.wsgi:application --bind 0.0.0.0:$PORT
```

**Opción 4 (Comando con PYTHONPATH):**
```
Start Command: cd /opt/render/project/src && PYTHONPATH=/opt/render/project/src gunicorn main.main.wsgi:application --bind 0.0.0.0:$PORT
```

### **Paso 4: Configurar Variables de Entorno (SOLO 3 variables)**

En la sección **"Environment Variables"** de tu servicio:

```bash
# Django Settings (OBLIGATORIAS)
SECRET_KEY=w=16hGTv^tV5LAlSN^v&CnPMzOa1d3R8Mr8-%Qy%JZBycDL*EL
DEBUG=False
ALLOWED_HOSTS=tu-app.onrender.com

# NOTA: NO necesitas DATABASE_URL - se usa SQLite automáticamente
```

### **Paso 5: Desplegar**

1. **"Create Web Service"**
2. Render comenzará el build automáticamente
3. Esperar 5-10 minutos para completar

## 🔍 Verificación del Despliegue

### **1. Verificar Build Logs**
- Revisar que no hay errores en el build
- Confirmar que las migraciones se ejecutaron
- Verificar que SQLite se configuró correctamente

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
- Probar el formulario de contacto (guardará en SQLite)
- Verificar que los archivos estáticos cargan

## 🛠️ Solución de Problemas Comunes

### **Error: "ModuleNotFoundError"**
- Verificar que todas las dependencias están en `requirements.txt`
- Revisar el build log para errores específicos

### **Error: "Static files not found"**
- Verificar que `STATIC_ROOT` está configurado
- Confirmar que `collectstatic` se ejecutó en el build

### **Error: "SECRET_KEY not set"**
- Agregar `SECRET_KEY` a las variables de entorno
- Usar la clave generada: `w=16hGTv^tV5LAlSN^v&CnPMzOa1d3R8Mr8-%Qy%JZBycDL*EL`

### **Error: "Database connection failed"**
- Con SQLite, esto no debería ocurrir
- Verificar que no hay variables `DATABASE_URL` configuradas

## 📊 Monitoreo y Mantenimiento

### **Logs**
- **Render Dashboard** → Tu servicio → **"Logs"**
- Revisar logs para errores y debugging

### **Variables de Entorno**
- **Render Dashboard** → Tu servicio → **"Environment"**
- Actualizar variables según sea necesario

### **Deploy Automático**
- Cada push a `main` activará un nuevo deploy
- Los datos de SQLite se reinician en cada deploy (normal para portfolios)

## 🔒 Seguridad en Producción

### **Variables Sensibles**
- ✅ `SECRET_KEY` - Clave secreta única
- ✅ `DEBUG=False` - Deshabilitar modo debug
- ✅ `ALLOWED_HOSTS` - Solo dominios permitidos

### **HTTPS**
- ✅ Render proporciona HTTPS automáticamente
- ✅ `SECURE_SSL_REDIRECT=True` - Redirección forzada

### **Base de Datos**
- ✅ SQLite para desarrollo y portfolios
- ✅ No requiere configuración adicional
- ✅ Completamente gratuito

## 📈 Optimizaciones

### **Performance**
- ✅ WhiteNoise para archivos estáticos
- ✅ Compresión automática
- ✅ Cache configurado

### **Escalabilidad**
- ✅ Gunicorn como servidor WSGI
- ✅ Configuración para múltiples workers

## 🎯 Configuración de Emails (OPCIONAL)

Si quieres que funcione el formulario de contacto, agrega estas variables:

```bash
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=tu-email@gmail.com
EMAIL_HOST_PASSWORD=tu-app-password
DEFAULT_FROM_EMAIL=tu-email@gmail.com
EMAIL_SUBJECT_PREFIX=[Portfolio]
```

## 📋 Checklist de Despliegue

- [ ] Código subido a GitHub
- [ ] Cuenta en Render creada
- [ ] Web Service configurado
- [ ] Variables de entorno configuradas (3 variables)
- [ ] Build exitoso
- [ ] Aplicación accesible
- [ ] Superusuario creado
- [ ] Funcionalidades probadas
- [ ] Emails configurados (opcional)

## 🚀 URLs Importantes

- **Aplicación:** `https://tu-app.onrender.com`
- **Admin:** `https://tu-app.onrender.com/admin/`
- **Contacto:** `https://tu-app.onrender.com/contact/`

## 💰 Costos

- ✅ **Web Service:** GRATIS (hasta 750 horas/mes)
- ✅ **Base de Datos:** GRATIS (SQLite incluido)
- ✅ **HTTPS:** GRATIS
- ✅ **Dominio:** GRATIS (tu-app.onrender.com)

## ⚠️ Limitaciones de SQLite

- Los datos se reinician en cada deploy
- No es ideal para aplicaciones con muchos usuarios
- Perfecto para portfolios personales
- El formulario de contacto guarda temporalmente

## 🎯 Ventajas de esta Configuración

- ✅ **Completamente GRATIS**
- ✅ **Configuración simple**
- ✅ **Deploy rápido**
- ✅ **Perfecto para portfolios**
- ✅ **No requiere gestión de base de datos**

---

**¡Tu portfolio estará en línea GRATIS en minutos! 🎉**
