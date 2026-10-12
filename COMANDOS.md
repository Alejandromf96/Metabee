# 🎤 Comandos de Voz para Metabee

## ✅ Comandos Implementados

### 🔊 Comandos de Voz (TTS - El asistente te habla)

Metabee ahora **habla todas las respuestas**. El sistema usa síntesis de voz en español.

---

## 📂 Comandos para Carpetas y Documentos

```
"Abre documentos"          → Abre la carpeta de Documentos
"Abre descargas"           → Abre la carpeta de Descargas
"Abre escritorio"          → Abre el Escritorio
"Abre imágenes"            → Abre la carpeta de Imágenes
"Abre música"              → Abre la carpeta de Música
"Abre videos"              → Abre la carpeta de Vídeos
```

---

## 🪟 Comandos para Ventanas

### Maximizar Ventanas
```
"Maximiza Chrome"          → Maximiza la ventana de Chrome
"Maximiza VS Code"         → Maximiza Visual Studio Code
"Maximiza navegador"       → Maximiza cualquier navegador
"Maximiza vscode"          → Maximiza VS Code (alias)
"Maximiza código"          → Maximiza VS Code (alias)
"Maximiza esta ventana"    → Maximiza la ventana activa
```

### Minimizar Ventanas
```
"Minimiza Chrome"          → Minimiza la ventana de Chrome
"Minimiza VS Code"         → Minimiza Visual Studio Code
"Minimiza navegador"       → Minimiza cualquier navegador
"Minimiza esta ventana"    → Minimiza la ventana activa
```

### Cerrar Ventanas
```
"Cierra Chrome"            → Cierra la ventana de Chrome
"Cierra VS Code"           → Cierra Visual Studio Code
"Cierra navegador"         → Cierra cualquier navegador
```

---

## 🔧 Comandos de Aplicaciones

```
"Abre Chrome"              → Abre Google Chrome
"Abre navegador"           → Abre el navegador por defecto
"Abre VS Code"             → Abre Visual Studio Code
"Abre vscode"              → Abre VS Code (alias)
"Abre código"              → Abre VS Code (alias)
"Abre descargas"           → Abre la carpeta de Descargas
"Abre Gmail"               → Abre Gmail en el navegador
```

---

## 🔊 Comandos de Audio y Volumen

```
"Sube el volumen"          → Aumenta el volumen 15%
"Sube volumen"             → Aumenta el volumen 15%
"Baja el volumen"          → Disminuye el volumen 15%
"Baja volumen"             → Disminuye el volumen 15%
"Silencia"                 → Silencia el audio
"Silencia el audio"        → Silencia el audio
"Activa audio"             → Reactiva el audio
"Desmute"                  → Reactiva el audio
```

---

## 🔍 Comandos de Búsqueda

```
"Busca en Google [término]"    → Busca en Google
"Reproduce [canción/video]"    → Reproduce en YouTube
"Reproducir [búsqueda]"        → Reproduce en YouTube
"Busca [búsqueda]"             → Busca en Google
```

---

## 📺 Comandos de YouTube

```
"Escuela de Nada"          → Reproduce el canal "Escuela de Nada"
```

---

## 📧 Comandos de Correo

```
"Gmail"                    → Abre Gmail
"Bandeja"                  → Abre bandeja de entrada
"Correo"                   → Abre Gmail
```

---

## 🎯 Ejemplos de Uso Completo

### Ejemplo 1: Mañana de Trabajo
```
1. "Hola Metabee"          → Inicia la escucha
2. "Abre VS Code"          → Abre el editor de código
3. "Maximiza vscode"       → Maximiza la ventana
4. "Abre documentos"       → Abre la carpeta de proyectos
5. "Sube el volumen"       → Aumenta el sonido
```

### Ejemplo 2: Pausa de Trabajo
```
1. "Minimiza chrome"       → Minimiza navegador
2. "Abre YouTube"          → Abre YouTube
3. "Reproduce música relajante"  → Busca música en YouTube
```

---

## 🔧 Configuración Personalizada

Puedes modificar las siguientes opciones en `config/settings.py`:

### Velocidad de Voz
```python
VOICE_CONFIG = {
    "rate": 180,    # Velocidad: 0-300 (más alto = más rápido)
    "volume": 0.9,  # Volumen: 0.0 a 1.0
    "voice_index": 0,  # 0=masculino, 1=femenino (depende del sistema)
}
```

### Agregar Más Carpetas
En `config/settings.py`, agrega tus carpetas personalizadas:
```python
FOLDERS = {
    "documentos": str(HOME_DIR / "Documents"),
    "proyectos": str(HOME_DIR / "Documents/Proyectos"),  # Nueva carpeta
    "descarga": str(DOWNLOADS_DIR),
}
```

---

## 🐛 Solución de Problemas

### Metabee no habla
- Asegúrate de que el volumen del sistema no esté silenciado
- Verifica que `pyttsx3` esté correctamente instalado: `pip install pyttsx3`

### No reconoce comandos de voz
- Habla claro y cerca del micrófono
- Asegúrate de que Google Speech Recognition está disponible
- Verifica tu conexión a Internet

### Las ventanas no se maximizan/minimizan
- Algunos programas pueden no permitir estas operaciones
- Intenta usar los atajos de teclado de Windows: `Win+Up` para maximizar

---

## 💡 Tips y Trucos

1. **Puedes ser coloquial**: Metabee entiende variaciones como "abre las descargas" en lugar de "abre descargas"
2. **Comandos encadenados**: Puedes dar múltiples comandos seguidos
3. **Personalización de voz**: Experimenta con `VOICE_CONFIG` para encontrar la velocidad y volumen perfectos

---

## 📝 Próximas Mejoras Planeadas

- [ ] Sistema de notas inteligentes
- [ ] Control de reproducción de música (play, pause, next, previous)
- [ ] Integración con calendario y recordatorios
- [ ] Control de aplicaciones de Office (Word, Excel, PowerPoint)
- [ ] Comandos para abrir aplicaciones personalizadas
- [ ] Historial de comandos

---

¡Disfruta usando Metabee! 🚀
