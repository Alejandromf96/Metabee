"""
Control del navegador, YouTube y Google - Versión Mejorada
"""
import subprocess
import webbrowser
import urllib.parse
import os
import pywhatkit  # RECUERDA: pip install pywhatkit

class BrowserControl:
    def __init__(self, apps_config, youtube_channels):
        """Inicializa el control del navegador"""
        self.chrome_path = apps_config.get("chrome", "")
        self.youtube_url = apps_config.get("youtube", "https://www.youtube.com")
        self.channels = youtube_channels
    
    def _open_url(self, url):
        """Método privado para decidir cómo abrir una URL"""
        try:
            if self.chrome_path and os.path.exists(self.chrome_path):
                subprocess.Popen([self.chrome_path, "--new-window", url], shell=True)
            else:
                webbrowser.open(url)
            return True
        except:
            webbrowser.open(url) # Fallback final
            return True

    def open_youtube(self):
        """Abre la página principal de YouTube"""
        self._open_url(self.youtube_url)
        return True, "Abriendo YouTube, jefe."

    def open_youtube_channel(self, channel_name):
        """Abre un canal específico configurado en settings.py"""
        channel_name = channel_name.lower()
        for key, url in self.channels.items():
            if key in channel_name:
                self._open_url(url)
                return True, f"Abriendo el canal de {key}."
        
        # Si no está en la lista, lo buscamos en YouTube directamente
        return self.search_youtube_video(channel_name)

    def search_youtube_video(self, query):
        """Busca y REPRODUCE automáticamente el video"""
        try:
            # pywhatkit abre el navegador y le da play al primer resultado
            pywhatkit.playonyt(query)
            return True, f"Reproduciendo {query} en YouTube."
        except Exception as e:
            # Si falla pywhatkit, usamos tu método original de búsqueda
            search_query = urllib.parse.quote(query)
            url = f"https://www.youtube.com/results?search_query={search_query}"
            self._open_url(url)
            return True, f"Buscando {query} en YouTube."

    def google_search(self, query):
        """Realiza una búsqueda general en Google"""
        try:
            pywhatkit.search(query)
            return True, f"He encontrado esto en Google sobre {query}."
        except:
            search_query = urllib.parse.quote(query)
            url = f"https://www.google.com/search?q={search_query}"
            self._open_url(url)
            return True, "Aquí tiene los resultados de búsqueda."

    def open_gmail(self):
        """Abre directamente la bandeja de entrada"""
        self._open_url("https://mail.google.com")
        return True, "Abriendo su correo electrónico, señor."