"""
Lanzador de aplicaciones del sistema
"""
import subprocess
import os
import webbrowser
from pathlib import Path


class AppLauncher:
    def __init__(self, apps_config):
        """Inicializa el lanzador con configuración de apps"""
        self.apps = apps_config
    
    def launch_vscode(self):
        """Abre Visual Studio Code"""
        try:
            if os.path.exists(self.apps["vscode"]):
                subprocess.Popen([self.apps["vscode"]], shell=True)
                return True, "Abriendo Visual Studio Code, jefe"
            else:
                return False, "No encontré Visual Studio Code en la ruta configurada"
        except Exception as e:
            return False, f"Error al abrir VS Code: {str(e)}"
    
    def open_downloads(self):
        """Abre la carpeta de descargas"""
        try:
            downloads_path = str(Path.home() / "Downloads")
            os.startfile(downloads_path)
            return True, "Abriendo carpeta de descargas"
        except Exception as e:
            return False, f"Error al abrir descargas: {str(e)}"
    
    def open_gmail(self):
        """Abre Gmail en el navegador"""
        try:
            if os.path.exists(self.apps["chrome"]):
                subprocess.Popen([self.apps["chrome"], "--new-window", self.apps["gmail"]], shell=True)
                return True, "Abriendo tu bandeja de correo, jefe"
            else:
                # Fallback a webbrowser
                webbrowser.open(self.apps["gmail"])
                return True, "Abriendo Gmail"
        except Exception as e:
            return False, f"Error al abrir Gmail: {str(e)}"
    
    def open_chrome(self, url=None):
        """Abre Google Chrome"""
        try:
            if os.path.exists(self.apps["chrome"]):
                if url:
                    subprocess.Popen([self.apps["chrome"], "--new-window", url], shell=True)
                else:
                    subprocess.Popen([self.apps["chrome"]], shell=True)
                return True, "Abriendo Chrome"
            else:
                # Fallback a navegador por defecto
                if url:
                    webbrowser.open(url)
                else:
                    webbrowser.open("http://www.google.com")
                return True, "Abriendo navegador"
        except Exception as e:
            return False, f"Error al abrir Chrome: {str(e)}"
    
    def open_folder(self, folder_path):
        """Abre una carpeta en el explorador de archivos"""
        try:
            if not os.path.exists(folder_path):
                return False, f"La carpeta no existe: {folder_path}"
            os.startfile(folder_path)
            return True, f"Carpeta abierta"
        except Exception as e:
            return False, f"Error al abrir carpeta: {str(e)}"
    
    def open_file(self, file_path):
        """Abre un archivo con su aplicación predeterminada"""
        try:
            if not os.path.exists(file_path):
                return False, f"El archivo no existe: {file_path}"
            os.startfile(file_path)
            return True, f"Archivo abierto"
        except Exception as e:
            return False, f"Error al abrir archivo: {str(e)}"
    
    def open_notepad(self):
        """Abre el Bloc de notas"""
        try:
            subprocess.Popen("notepad.exe", shell=True)
            return True, "Abriendo Bloc de notas"
        except Exception as e:
            return False, f"Error al abrir Bloc de notas: {str(e)}"
    
    def open_calculator(self):
        """Abre la Calculadora de Windows"""
        try:
            subprocess.Popen("calc.exe", shell=True)
            return True, "Abriendo Calculadora"
        except Exception as e:
            return False, f"Error al abrir Calculadora: {str(e)}"
    
    def open_youtube(self):
        """Abre YouTube en el navegador"""
        try:
            webbrowser.open(self.apps.get("youtube", "https://www.youtube.com"))
            return True, "Abriendo YouTube"
        except Exception as e:
            return False, f"Error al abrir YouTube: {str(e)}"