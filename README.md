# 🎙️ Metabee - Asistente de Voz Local

Tu asistente de voz inteligente, similar a JARVIS, que funciona completamente en local con reconocimiento y síntesis de voz en español.

## 🎯 ¿Qué es Metabee?

Metabee es un asistente de voz personal que puedes controlar completamente con comandos de voz en español. Te permite:

✅ **Hablar con tu computadora** - Metabee entiende tus comandos en voz y responde hablándote
✅ **Controlar ventanas** - Maximizar, minimizar, cerrar aplicaciones
✅ **Acceder a carpetas** - Abrir documentos, descargas, escritorio, etc.
✅ **Lanzar aplicaciones** - Chrome, VS Code, Gmail, y más
✅ **Controlar el volumen** - Subir, bajar, silenciar el audio
✅ **Buscar en Internet** - Google y YouTube desde la voz
✅ **100% Local y Privado** - No requiere servicios en la nube (salvo Google Speech Recognition)

---

## 🚀 Instalación y Configuración

### Requisitos Previos
- Python 3.8 o superior
- Micrófono conectado y funcionando
- Conexión a Internet (para Google Speech Recognition)

### Paso 1: Instalar Dependencias

```bash
# Ir a la carpeta del proyecto
cd c:\Users\aleja\Documents\Metabee

# Instalar todas las dependencias
pip install -r requirements.txt
```

### Paso 2: Verificar la Instalación (Muy Importante ⚠️)

Antes de ejecutar Metabee, prueba que el sistema de voz funciona:

```bash
python test_voice.py
```

Este script:
1. Inicializa el motor de voz
2. Comprueba que Metabee puede hablarte
3. Prueba el reconocimiento de voz
4. Te muestra la configuración actual

---

## ▶️ Uso Básico

### Iniciar Metabee

```bash
python main.py
```

La interfaz gráfica se abrirá con el estilo JARVIS. Metabee dirá un saludo y comenzará a escuchar tus comandos.

### Detener Metabee

Presiona **ESC** o cierra la ventana de la interfaz gráfica.

---

## 📚 Comandos Principales

### 🎤 Hablar (La nueva característica principal)

Metabee ahora **habla todas las respuestas** usando síntesis de voz en español. Esto incluye:
- Confirmación de comandos ejecutados
- Mensajes de error si algo no se puede hacer
- Saludos inteligentes según la hora del día

### 🪟 Ventanas

```
"Maximiza Chrome"          → Expande Chrome al tamaño completo
"Minimiza VS Code"         → Reduce VS Code a la bandeja de tareas
"Cierra navegador"         → Cierra la ventana del navegador
```

### 📂 Carpetas

```
"Abre documentos"          → Abre la carpeta Documentos
"Abre descargas"           → Abre la carpeta Descargas
"Abre escritorio"          → Abre el Escritorio
"Abre imágenes"            → Abre la carpeta Imágenes
"Abre música"              → Abre la carpeta Música
"Abre videos"              → Abre la carpeta Vídeos
```

### 🔧 Aplicaciones

```
"Abre Chrome"              → Abre Google Chrome
"Abre VS Code"             → Abre Visual Studio Code
"Abre código"              → Alias para VS Code
"Abre Gmail"               → Abre Gmail en el navegador
```

### 🔊 Audio

```
"Sube el volumen"          → Aumenta el sonido
"Baja el volumen"          → Disminuye el sonido
"Silencia"                 → Mute / Silencia todo
"Activa audio"             → Desmuete
```

### 🔍 Búsqueda

```
"Busca en Google gatos"    → Busca "gatos" en Google
"Reproduce música relajante" → Busca en YouTube
```

**Para ver la lista completa de comandos, lee [COMANDOS.md](COMANDOS.md)**

---

## ⚙️ Configuración Personalizada

### Cambiar la Velocidad y Volumen de Voz

Edita `config/settings.py`:

```python
VOICE_CONFIG = {
    "rate": 180,        # 0-300 (más alto = más rápido)
    "volume": 0.9,      # 0.0-1.0 (0.5 = 50%)
    "voice_index": 0,   # 0=masculino, 1=femenino (depende del sistema)
}
```

### Agregar Tus Propias Carpetas

En `config/settings.py`, agrega más carpetas:

```python
FOLDERS = {
    "documentos": str(HOME_DIR / "Documents"),
    "proyectos": str(HOME_DIR / "Documents/Proyectos"),  # Nueva
    "trabajo": str(HOME_DIR / "Documents/Trabajo"),      # Nueva
}
```

Luego podrás decir: "Abre proyectos" o "Abre trabajo"

---

## 🔧 Estructura del Proyecto

```
Metabee/
├── main.py                 # Punto de entrada principal
├── test_voice.py          # Script de prueba de voz ⭐ EJECUTA ESTO PRIMERO
├── requirements.txt       # Dependencias del proyecto
├── COMANDOS.md            # Lista completa de comandos
│
├── config/
│   ├── __init__.py
│   └── settings.py        # Configuración global (voz, apps, carpetas)
│
├── core/
│   ├── __init__.py
│   ├── voice_engine.py    # Motor de reconocimiento y síntesis de voz
│   ├── command_processor.py  # Procesa los comandos y decide qué hacer
│   └── system_controller.py  # Controlador principal del sistema
│
├── commands/
│   ├── __init__.py
│   ├── app_launcher.py    # Lanza aplicaciones (Chrome, VS Code, etc)
│   ├── browser_control.py # Control del navegador
│   ├── system_control.py  # Control de volumen, ventanas, carpetas ✨ NUEVO
│   └── notes_manager.py   # Gestor de notas
│
└── ui/
    ├── __init__.py
    ├── metabee_interface.py  # Interfaz gráfica estilo JARVIS
    └── animations.py         # Animaciones visuales
```

---

## 🎯 Casos de Uso

### Ejemplo 1: Mañana de Productividad
```
1. "Metabee, abre VS Code"     → Abre el editor
2. "Maximiza vscode"            → Expande la ventana
3. "Abre documentos"            → Accede a tus proyectos
4. "Reproduce música de trabajo" → YouTube para música
5. "Sube el volumen"            → Aumenta el sonido
```

### Ejemplo 2: Pausa de Descanso
```
1. "Minimiza chrome"            → Guarda las pestañas
2. "Abre documentos"            → Mira fotos personales
3. "Reproduce música relajante" → YouTube Music
4. "Baja el volumen"            → Volumen bajo
```

---

## 🐛 Solución de Problemas

### ❌ "Error: No se puede importar pyttsx3"
```bash
pip install pyttsx3
```

### ❌ "No escucho a Metabee hablando"
- ✅ Verifica que el volumen del sistema NO esté silenciado
- ✅ Sube el volumen en `VOICE_CONFIG` en `config/settings.py`
- ✅ Prueba con `python test_voice.py`

### ❌ "Metabee no entiende mis comandos"
- ✅ Habla claro y cerca del micrófono
- ✅ Verifica tu conexión a Internet
- ✅ Revisa que el micrófono esté conectado
- ✅ Intenta con comandos simples como "abre Chrome"

### ❌ "Las ventanas no se maximizan"
- ✅ Algunos programas pueden no permitirlo
- ✅ Intenta con `Win+Up` para maximizar manualmente
- ✅ Verifica que la ventana esté en enfoque

---

## 📦 Dependencias

| Paquete | Propósito |
|---------|-----------|
| **pyttsx3** | Síntesis de voz (TTS) para que Metabee hable |
| **speechrecognition** | Reconocimiento de voz (escucha comandos) |
| **pyaudio** | Acceso al micrófono del sistema |
| **pygetwindow** | Control de ventanas (maximizar, minimizar) |
| **pyautogui** | Automatización de teclado y mouse |
| **pycaw** | Control de volumen |
| **pillow** | Procesamiento de imágenes para la UI |
| **pywhatkit** | Búsqueda en Google y YouTube |

---

## ✨ Nuevas Características (Actualizadas)

### ✅ Síntesis de Voz (TTS) - NUEVO
- Metabee ahora **habla todas sus respuestas**
- Configuración personalizable de velocidad y volumen
- Voz en español natural

### ✅ Control de Ventanas - MEJORADO
- Maximizar ventanas por nombre (Chrome, VS Code, etc)
- Minimizar ventanas
- Cerrar ventanas

### ✅ Gestión de Carpetas - MEJORADO
- Abrir cualquier carpeta del sistema con voz
- Fácil de personalizar en la configuración

### 🔜 Próximas Mejoras
- Sistema de recordatorios por voz
- Control de reproductor de música
- Integración con calendario
- Control de luces y dispositivos IoT
- Comandos personalizados

---

## 🎮 Consejos Útiles

1. **Sé natural**: Metabee entiende variaciones del lenguaje
   ```
   ✅ "Abre las descargas"
   ✅ "Abre descargas"
   ✅ "Abre mi carpeta de descargas"
   ```

2. **Combina comandos**: Puedes dar varios comandos seguidos
   ```
   "Abre Chrome" → "Maximiza navegador" → "Sube el volumen"
   ```

3. **Experimenta con la configuración**: 
   - Ajusta `rate` si la voz es muy rápida o lenta
   - Prueba `voice_index` 0 y 1 para diferentes voces

4. **Usa la ayuda**: Siempre que dudes, ejecuta `python test_voice.py`

---

## 📝 Licencia

Este proyecto es de código abierto y está disponible para uso personal y educativo.

---

## 🚀 ¿Listo para Comenzar?

1. Instala las dependencias: `pip install -r requirements.txt`
2. Prueba el sistema: `python test_voice.py`
3. ¡Inicia Metabee!: `python main.py`
4. Lee [COMANDOS.md](COMANDOS.md) para explorar todas las opciones

---

**¡Disfruta usando tu asistente de voz personal! 🎉**
