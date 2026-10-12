"""
Configuración global de Metabee
"""
import os
from pathlib import Path

# Rutas del sistema
HOME_DIR = Path.home()
DOWNLOADS_DIR = HOME_DIR / "Downloads"
NOTES_DIR = HOME_DIR / "Documents" / "Metabee_Notes"

# Crear directorio de notas si no existe
NOTES_DIR.mkdir(parents=True, exist_ok=True)

# Aplicaciones (rutas comunes en Windows)
APPS = {
    "vscode": r"C:\Users\aleja\AppData\Local\Programs\Microsoft VS Code\Code.exe".format(os.getlogin()),
    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "gmail": "https://mail.google.com",
    "youtube": "https://www.youtube.com/@escueladenada",
}

# Carpetas frecuentes - puedes agregar más según necesites
FOLDERS = {
    "documentos": str(HOME_DIR / "Documents"),
    "descargas": str(DOWNLOADS_DIR),
    "escritorio": str(HOME_DIR / "Desktop"),
    "imágenes": str(HOME_DIR / "Pictures"),
    "música": str(HOME_DIR / "Music"),
    "videos": str(HOME_DIR / "Videos"),
}

# Aplicaciones con alias para comandos de voz
APP_ALIASES = {
    "vscode": "vscode",
    "vs code": "vscode",
    "código": "vscode",
    "chrome": "chrome",
    "navegador": "chrome",
    "navegador web": "chrome",
}

# Canales de YouTube favoritos
YOUTUBE_CHANNELS = {
    "escuela de nada": "https://www.youtube.com/@escueladenada",
    "escuela nada": "https://www.youtube.com/@escueladenada",
}

# Configuración de voz
VOICE_CONFIG = {
    "rate": 180,  # Velocidad de habla
    "volume": 0.9,  # Volumen (0.0 a 1.0)
    "voice_index": 0,  # Índice de voz (0 = masculino, 1 = femenino generalmente)
}

# Palabras de activación
WAKE_WORDS = ["metabee", "meta", "bee"]

# Colores de la interfaz (estilo JARVIS)
UI_COLORS = {
    "primary": "#00D9FF",      # Cyan brillante
    "secondary": "#0088AA",    # Cyan oscuro
    "background": "#000814",   # Negro azulado
    "accent": "#FFD60A",       # Amarillo
    "text": "#FFFFFF",         # Blanco
    "glow": "#00F0FF",         # Glow cyan
}