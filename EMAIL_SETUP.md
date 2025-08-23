# Configuración del Sistema de Emails

## 📧 Funcionalidad Implementada

El sistema de emails ahora incluye:

1. **Envío automático al administrador** cuando alguien envía un mensaje
2. **Email de confirmación al usuario** que confirma la recepción
3. **Almacenamiento en base de datos** de todos los mensajes
4. **Manejo de errores** con mensajes informativos

## 🔧 Configuración para Desarrollo

En modo desarrollo (`DEBUG=True`), los emails se muestran en la consola del servidor. No necesitas configuración adicional.

## 🚀 Configuración para Producción

### 1. Configurar Gmail (Recomendado)

#### Paso 1: Habilitar Autenticación de 2 Factores
1. Ve a tu cuenta de Google
2. Activa la verificación en 2 pasos
3. Ve a "Contraseñas de aplicación"

#### Paso 2: Crear Contraseña de Aplicación
1. Selecciona "Otra" como tipo de aplicación
2. Dale un nombre (ej: "Portfolio Django")
3. Copia la contraseña generada (16 caracteres)

#### Paso 3: Configurar Variables de Entorno
En tu archivo `.env` o en las variables de entorno de Render:

```bash
EMAIL_HOST_USER=tu-email@gmail.com
EMAIL_HOST_PASSWORD=tu-contraseña-de-aplicación
DEFAULT_FROM_EMAIL=tu-email@gmail.com
```

### 2. Configurar Otros Proveedores

#### Outlook/Hotmail
```bash
EMAIL_HOST=smtp-mail.outlook.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
```

#### Yahoo
```bash
EMAIL_HOST=smtp.mail.yahoo.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
```

#### Proveedor Personalizado
```bash
EMAIL_HOST=tu-servidor-smtp.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=tu-usuario
EMAIL_HOST_PASSWORD=tu-contraseña
```

## 📝 Variables de Entorno Requeridas

```bash
# Configuración básica de email
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_USE_SSL=False

# Credenciales (OBLIGATORIAS para producción)
EMAIL_HOST_USER=tu-email@gmail.com
EMAIL_HOST_PASSWORD=tu-app-password
DEFAULT_FROM_EMAIL=tu-email@gmail.com

# Opcional
EMAIL_SUBJECT_PREFIX=[Portfolio]
```

## 🧪 Probar el Sistema

### En Desarrollo
1. Ejecuta el servidor: `make dev`
2. Ve a la página de contacto
3. Envía un mensaje
4. Revisa la consola del servidor para ver los emails

### En Producción
1. Configura las variables de entorno en Render
2. Haz un deploy
3. Envía un mensaje de prueba
4. Verifica que recibes los emails

## 🔍 Solución de Problemas

### Error: "SMTPAuthenticationError"
- Verifica que la contraseña de aplicación sea correcta
- Asegúrate de que la autenticación de 2 factores esté activada

### Error: "SMTPServerDisconnected"
- Verifica el puerto (587 para TLS, 465 para SSL)
- Asegúrate de que `EMAIL_USE_TLS=True` esté configurado

### Error: "Connection refused"
- Verifica que el servidor SMTP sea correcto
- Revisa si hay firewall bloqueando el puerto

## 📋 Checklist de Configuración

- [ ] Autenticación de 2 factores activada en Gmail
- [ ] Contraseña de aplicación generada
- [ ] Variables de entorno configuradas en Render
- [ ] Email de prueba enviado y recibido
- [ ] Email de confirmación funcionando

## 🎯 Funcionalidades del Sistema

### Email al Administrador
- **Asunto:** "Nuovo messaggio di contatto: [tema]"
- **Contenido:** Datos completos del mensaje
- **Destinatario:** Email configurado en `EMAIL_HOST_USER`

### Email de Confirmación al Usuario
- **Asunto:** "Conferma ricezione del tuo messaggio"
- **Contenido:** Confirmación personalizada con detalles
- **Destinatario:** Email del usuario que envió el mensaje

### Almacenamiento en Base de Datos
- Todos los mensajes se guardan automáticamente
- Incluye timestamp y estado de lectura
- Accesible desde el admin de Django
