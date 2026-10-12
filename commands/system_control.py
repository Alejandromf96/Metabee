"""
Control del sistema (volumen, ventanas, carpetas, etc.)
"""
import pyautogui
import pygetwindow as gw
import os
import subprocess
from pathlib import Path
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


class SystemControl:
    def __init__(self):
        """Inicializa el control del sistema"""
        self._init_volume_control()
        pyautogui.FAILSAFE = False
    
    def _init_volume_control(self):
        """Inicializa el control de volumen de Windows"""
        try:
            devices = AudioUtilities.GetSpeakers()
            interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
            self.volume = cast(interface, POINTER(IAudioEndpointVolume))
        except Exception as e:
            print(f"Error inicializando control de volumen: {e}")
            self.volume = None
    
    def set_volume(self, level):
        """Establece el volumen (0-100)"""
        try:
            if self.volume is None:
                return False, "No pude acceder al control de volumen"
            
            # Convertir de 0-100 a 0.0-1.0
            volume_level = max(0.0, min(1.0, level / 100.0))
            
            # pycaw usa escala logarítmica
            min_vol = self.volume.GetVolumeRange()[0]
            max_vol = self.volume.GetVolumeRange()[1]
            
            # Convertir nivel lineal a dB
            if volume_level > 0:
                db_level = min_vol + (max_vol - min_vol) * volume_level
            else:
                db_level = min_vol
            
            self.volume.SetMasterVolumeLevel(db_level, None)
            return True, f"Volumen ajustado a {level} por ciento"
        except Exception as e:
            return False, f"Error ajustando volumen: {str(e)}"
    
    def increase_volume(self, amount=10):
        """Incrementa el volumen"""
        try:
            if self.volume is None:
                return False, "No pude acceder al control de volumen"
            
            current = self.volume.GetMasterVolumeLevelScalar() * 100
            new_level = min(100, current + amount)
            return self.set_volume(new_level)
        except Exception as e:
            return False, f"Error aumentando volumen: {str(e)}"
    
    def decrease_volume(self, amount=10):
        """Disminuye el volumen"""
        try:
            if self.volume is None:
                return False, "No pude acceder al control de volumen"
            
            current = self.volume.GetMasterVolumeLevelScalar() * 100
            new_level = max(0, current - amount)
            return self.set_volume(new_level)
        except Exception as e:
            return False, f"Error disminuyendo volumen: {str(e)}"
    
    def mute_volume(self):
        """Silencia el volumen"""
        try:
            if self.volume is None:
                return False, "No pude acceder al control de volumen"
            
            self.volume.SetMute(1, None)
            return True, "Audio silenciado, jefe"
        except Exception as e:
            return False, f"Error silenciando: {str(e)}"
    
    def unmute_volume(self):
        """Reactiva el volumen"""
        try:
            if self.volume is None:
                return False, "No pude acceder al control de volumen"
            
            self.volume.SetMute(0, None)
            return True, "Audio activado, señor"
        except Exception as e:
            return False, f"Error activando audio: {str(e)}"
    
    def maximize_window(self, window_title=None):
        """Maximiza una ventana"""
        try:
            if window_title:
                windows = gw.getWindowsWithTitle(window_title)
                if windows:
                    windows[0].maximize()
                    return True, f"Maximizando {window_title}"
                else:
                    return False, f"No encontré ninguna ventana de {window_title}"
            else:
                # Maximizar ventana activa
                active = gw.getActiveWindow()
                if active:
                    active.maximize()
                    return True, "Ventana maximizada, jefe"
                return False, "No hay ventana activa"
        except Exception as e:
            return False, f"Error maximizando ventana: {str(e)}"
    
    def minimize_window(self, window_title=None):
        """Minimiza una ventana"""
        try:
            if window_title:
                windows = gw.getWindowsWithTitle(window_title)
                if windows:
                    windows[0].minimize()
                    return True, f"Minimizando {window_title}"
                else:
                    return False, f"No encontré ninguna ventana de {window_title}"
            else:
                # Minimizar ventana activa
                active = gw.getActiveWindow()
                if active:
                    active.minimize()
                    return True, "Ventana minimizada, jefe"
                return False, "No hay ventana activa"
        except Exception as e:
            return False, f"Error minimizando ventana: {str(e)}"
    
    def close_window(self, window_title=None):
        """Cierra una ventana"""
        try:
            if window_title:
                windows = gw.getWindowsWithTitle(window_title)
                if windows:
                    windows[0].close()
                    return True, f"Ventana {window_title} cerrada"
                else:
                    return False, f"No encontré ninguna ventana de {window_title}"
            else:
                # Cerrar ventana activa
                pyautogui.hotkey('alt', 'f4')
                return True, "Cerrando ventana activa"
        except Exception as e:
            return False, f"Error cerrando ventana: {str(e)}"
    
    def open_folder(self, folder_path):
        """Abre una carpeta en el explorador de archivos"""
        try:
            if isinstance(folder_path, str):
                if not os.path.exists(folder_path):
                    return False, f"La carpeta {folder_path} no existe"
                os.startfile(folder_path)
                return True, f"Abriendo la carpeta"
            return False, "Ruta de carpeta inválida"
        except Exception as e:
            return False, f"Error abriendo carpeta: {str(e)}"
    
    def open_file(self, file_path):
        """Abre un archivo con la aplicación predeterminada"""
        try:
            if not os.path.exists(file_path):
                return False, f"El archivo {file_path} no existe"
            os.startfile(file_path)
            return True, f"Abriendo archivo"
        except Exception as e:
            return False, f"Error abriendo archivo: {str(e)}"
    
    def minimize_window(self, window_title=None):
        """Minimiza una ventana"""
        try:
            if window_title:
                windows = gw.getWindowsWithTitle(window_title)
                if windows:
                    windows[0].minimize()
                    return True, f"Ventana {window_title} minimizada"
                else:
                    return False, f"No encontré ninguna ventana con '{window_title}'"
            else:
                # Minimizar ventana activa
                active = gw.getActiveWindow()
                if active:
                    active.minimize()
                    return True, "Ventana minimizada"
                return False, "No hay ventana activa"
        except Exception as e:
            return False, f"Error minimizando ventana: {str(e)}"
    
    def close_window(self, window_title=None):
        """Cierra una ventana"""
        try:
            if window_title:
                windows = gw.getWindowsWithTitle(window_title)
                if windows:
                    windows[0].close()
                    return True, f"Ventana {window_title} cerrada"
                else:
                    return False, f"No encontré ninguna ventana con '{window_title}'"
            else:
                # Cerrar ventana activa
                pyautogui.hotkey('alt', 'f4')
                return True, "Cerrando ventana activa"
        except Exception as e:
            return False, f"Error cerrando ventana: {str(e)}"