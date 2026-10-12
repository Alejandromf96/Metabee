
import re
import webbrowser
import pywhatkit
from pathlib import Path


class CommandProcessor:
    def __init__(self, app_launcher, browser_control, system_control, notes_manager):
        self.app_launcher = app_launcher
        self.browser_control = browser_control
        self.system_control = system_control
        self.notes_manager = notes_manager
    
    def process(self, command):
        if not command:
            return False, "No recibí ningún comando"
        
        command = command.lower().strip()
        
        # --- COMANDOS DE VENTANAS (PRIORIDAD ALTA) ---
        if any(word in command for word in ["maximizar", "maximiza", "ampliar", "amplía"]):
            return self._handle_maximize_command(command)
        
        if any(word in command for word in ["minimizar", "minimiza", "empequeñecer"]):
            return self._handle_minimize_command(command)
        
        if any(word in command for word in ["cerrar"]):
            return self._handle_close_command(command)
        
        # --- COMANDOS DE CARPETAS Y DOCUMENTOS ---
        if any(word in command for word in ["abre", "abrir"]) and any(word in command for word in ["carpeta", "folder", "documentos", "descargas", "escritorio", "imágenes", "música", "videos"]):
            return self._handle_open_folder_command(command)
        
        # --- COMANDOS ESPECIALES PRIORITARIOS ---
        
        # YouTube: Escuela de Nada
        if "escuela de nada" in command:
            pywhatkit.playonyt("Escuela de Nada")
            return True, "Entendido jefe, poniendo Escuela de Nada en YouTube."

        # Google: Gmail / Bandeja
        if any(word in command for word in ["gmail", "bandeja", "correo"]):
            webbrowser.open("https://mail.google.com")
            return True, "Abriendo su bandeja de entrada, señor."

        # Búsqueda directa en Google
        if "busca en google" in command:
            query = command.replace("busca en google", "").strip()
            if query:
                pywhatkit.search(query)
                return True, f"Buscando {query} en Google."
            return False, "Dígame qué desea buscar en Google, jefe."

        # --- MANEJO POR CATEGORÍAS ---
        
        if any(word in command for word in ["abre", "abrir"]):
            return self._handle_open_command(command)
        
        if any(word in command for word in ["reproduce", "reproducir", "busca", "buscar"]):
            return self._handle_search_command(command)
            
        if any(word in command for word in ["volumen", "audio", "sonido", "silencia", "sube", "baja"]):
            return self._handle_volume_command(command)

        if any(word in command for word in ["nota", "anota"]):
            return self._handle_note_command(command)
        
        return False, "No entendí ese comando, jefe. ¿Podría repetirlo?"

    def _handle_maximize_command(self, command):
        """Maneja comandos de maximizar ventanas"""
        # Buscar nombre de aplicación en el comando
        app_names = ["chrome", "navegador", "vscode", "código", "vs code", "edge", "firefox", "word", "excel", "powerpoint"]
        
        for app in app_names:
            if app in command:
                # Maximizar ventana específica
                success, msg = self.system_control.maximize_window(app)
                if success:
                    return True, f"He maximizado {app} para usted."
                else:
                    return False, f"No encontré una ventana de {app}"
        
        # Si no especificó app, maximiza la ventana activa
        success, msg = self.system_control.maximize_window()
        return success, msg if success else "No hay ventana activa para maximizar"

    def _handle_minimize_command(self, command):
        """Maneja comandos de minimizar ventanas"""
        app_names = ["chrome", "navegador", "vscode", "código", "vs code", "edge", "firefox", "word", "excel", "powerpoint"]
        
        for app in app_names:
            if app in command:
                success, msg = self.system_control.minimize_window(app)
                if success:
                    return True, f"He minimizado {app}."
                else:
                    return False, f"No encontré una ventana de {app}"
        
        success, msg = self.system_control.minimize_window()
        return success, msg if success else "No hay ventana activa para minimizar"

    def _handle_close_command(self, command):
        """Maneja comandos de cerrar ventanas"""
        app_names = ["chrome", "navegador", "vscode", "código", "vs code", "edge", "firefox", "word", "excel", "powerpoint"]
        
        for app in app_names:
            if app in command:
                success, msg = self.system_control.close_window(app)
                if success:
                    return True, f"He cerrado {app}."
                else:
                    return False, f"No encontré una ventana de {app}"
        
        return False, "¿Cuál ventana desea cerrar, jefe?"

    def _handle_open_folder_command(self, command):
        """Maneja comandos para abrir carpetas y documentos"""
        folder_map = {
            "documentos": str(Path.home() / "Documents"),
            "descargas": str(Path.home() / "Downloads"),
            "escritorio": str(Path.home() / "Desktop"),
            "imágenes": str(Path.home() / "Pictures"),
            "música": str(Path.home() / "Music"),
            "videos": str(Path.home() / "Videos"),
        }
        
        for folder_name, folder_path in folder_map.items():
            if folder_name in command:
                success, msg = self.system_control.open_folder(folder_path)
                if success:
                    return True, f"Abriendo la carpeta de {folder_name}."
                else:
                    return False, msg
        
        return False, "No especificó qué carpeta abrir, jefe."

    def _handle_search_command(self, command):
        """Maneja comandos de búsqueda y reproducción"""
        query = re.sub(r'reproduce|reproducir|busca|buscar|play|en youtube', '', command).strip()
        if query:
            if "reproduce" in command or "play" in command:
                pywhatkit.playonyt(query)
                return True, f"Reproduciendo {query} en YouTube."
            else:
                pywhatkit.search(query)
                return True, f"He encontrado esto sobre {query}."
        return False, "No supe qué buscar."

    def _handle_volume_command(self, command):
        """Maneja comandos de volumen y audio"""
        # Silenciar
        if any(word in command for word in ["silencia", "mute", "mudo"]):
            success, msg = self.system_control.mute_volume()
            return success, msg
        
        # Bajar volumen
        if any(word in command for word in ["baja", "baja el volumen", "reduce"]):
            success, msg = self.system_control.decrease_volume(15)
            return success, "He bajado el volumen" if success else msg
        
        # Subir volumen
        if any(word in command for word in ["sube", "sube el volumen", "aumenta", "más volumen"]):
            success, msg = self.system_control.increase_volume(15)
            return success, "He subido el volumen" if success else msg
        
        # Activar audio
        if any(word in command for word in ["activa", "actívalo", "desmute", "desmuto"]):
            success, msg = self.system_control.unmute_volume()
            return success, msg
        
        return False, "No entendí el comando de audio, jefe."

    def _handle_open_command(self, command):
        """Maneja comandos genéricos de abrir aplicaciones"""
        if "gmail" in command:
            return True, "Abriendo Gmail en el navegador."
        
        if "chrome" in command or "navegador" in command:
            self.app_launcher.open_chrome()
            return True, "Abriendo Chrome."
        
        if "vscode" in command or "código" in command or "vs code" in command:
            self.app_launcher.launch_vscode()
            return True, "Abriendo Visual Studio Code."
        
        if "descargas" in command or "downloads" in command:
            self.app_launcher.open_downloads()
            return True, "Abriendo la carpeta de descargas."
        
        return False, "No sé cómo abrir esa aplicación, jefe."

    def _handle_note_command(self, command):
        """Maneja comandos de notas"""
        # Por ahora, solo retorna un mensaje genérico
        return False, "El sistema de notas aún está en desarrollo, señor."