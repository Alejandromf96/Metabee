"""
Interfaz gráfica estilo JARVIS con Tkinter - Versión Thread-Safe con Queue
"""
import tkinter as tk
from tkinter import font as tkfont
import math
import queue  # <-- Importamos la librería de colas
from .animations import AnimationManager

class MetabeeInterface:
    """Interfaz gráfica principal con Tkinter"""
    
    def __init__(self, config):
        """Inicializa la interfaz"""
        self.root = tk.Tk()
        self.root.title("METABEE - Asistente de Voz")
        
        # Configuración de ventana
        self.width = 800
        self.height = 600
        self.root.geometry(f"{self.width}x{self.height}")
        self.root.configure(bg=config["background"])
        self.root.resizable(False, False)
        
        self.colors = config
        self.center = (self.width // 2, self.height // 2)
        
        # Canvas para animaciones
        self.canvas = tk.Canvas(
            self.root, 
            width=self.width, 
            height=self.height,
            bg=config["background"],
            highlightthickness=0
        )
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        # Fuentes
        self.font_title = tkfont.Font(family="Arial", size=48, weight="bold")
        self.font_status = tkfont.Font(family="Arial", size=20)
        self.font_command = tkfont.Font(family="Consolas", size=14)
        
        self._create_text_elements()
        
        # Sistema de animaciones
        self.anim_manager = AnimationManager(self.canvas, self.center, self.colors)
        self.orb = self.anim_manager.create_pulsing_orb()
        self.waves = []
        self.particles = []
        
        self.is_listening = False
        self.is_running = True
        
        # --- SISTEMA DE COLA SEGURO ---
        self.task_queue = queue.Queue()
        
        self._draw_hex_grid()
        
        self.root.protocol("WM_DELETE_WINDOW", self._on_closing)
        self.root.bind("<Escape>", lambda e: self._on_closing())
        
        # Iniciar loops
        self._animation_loop()
        self._process_queue()  # Iniciamos el revisor de tareas

    def _create_text_elements(self):
        """Crea los elementos de texto iniciales"""
        self.title_text = self.canvas.create_text(
            self.center[0], 80, text="METABEE",
            font=self.font_title, fill=self.colors["primary"]
        )
        self.status_text = self.canvas.create_text(
            self.center[0], self.height - 100, text="Inicializando...",
            font=self.font_status, fill=self.colors["text"]
        )
        self.command_text = self.canvas.create_text(
            self.center[0], self.height - 60, text="",
            font=self.font_command, fill=self.colors["accent"]
        )
        self.listening_text = self.canvas.create_text(
            self.center[0], self.height - 140, text="",
            font=self.font_status, fill="#FF0000"
        )

    def _draw_hex_grid(self):
        """Dibuja el fondo hexagonal"""
        hex_size = 30
        hex_width = hex_size * 1.732
        hex_height = hex_size * 2
        for row in range(-2, int(self.height / hex_height) + 2):
            for col in range(-2, int(self.width / hex_width) + 2):
                x = col * hex_width + (row % 2) * (hex_width / 2)
                y = row * hex_height * 0.75
                if -hex_size < x < self.width + hex_size:
                    points = []
                    for i in range(6):
                        angle = 3.14159 / 3 * i
                        points.extend([x + hex_size * math.cos(angle), y + hex_size * math.sin(angle)])
                    self.canvas.create_polygon(points, outline=self.colors["secondary"], fill='', width=1)

    def _animation_loop(self):
        """Loop de animación (Corre siempre en el hilo principal)"""
        if not self.is_running: return
        self.anim_manager.update_orb(self.orb)
        self.waves = [w for w in self.waves if self.anim_manager.update_wave(w)]
        new_p = []
        for ps in self.particles:
            updated = self.anim_manager.update_particles(ps)
            if updated: new_p.append(updated)
        self.particles = new_p
        self.root.after(33, self._animation_loop)

    def _process_queue(self):
        """Revisa constantemente si hay tareas pendientes del hilo de voz"""
        if not self.is_running: return
        try:
            while True:
                # Saca la tarea del buzón y la ejecuta
                task = self.task_queue.get_nowait()
                task()
        except queue.Empty:
            pass  # El buzón está vacío, no pasa nada
        
        # Vuelve a revisar en 50 milisegundos
        self.root.after(50, self._process_queue)

    # --- MÉTODOS DE COMUNICACIÓN (Ponen tareas en el buzón) ---

    def set_status(self, text):
        """Envía la tarea de actualizar el estado al buzón"""
        self.task_queue.put(lambda: self.canvas.itemconfig(self.status_text, text=text))

    def set_command(self, text):
        """Envía la tarea de actualizar el comando al buzón"""
        display_text = f"> {text}" if text else ""
        self.task_queue.put(lambda: self.canvas.itemconfig(self.command_text, text=display_text))

    def set_listening(self, is_listening):
        """Envía la tarea de actualizar el indicador de escucha al buzón"""
        self.is_listening = is_listening
        def update_ui():
            if is_listening:
                self.canvas.itemconfig(self.listening_text, text="● ESCUCHANDO")
                self._internal_add_wave()
            else:
                self.canvas.itemconfig(self.listening_text, text="")
        self.task_queue.put(update_ui)

    def add_wave(self):
        """Envía la tarea de crear una onda al buzón"""
        self.task_queue.put(self._internal_add_wave)

    def _internal_add_wave(self):
        """Función interna que realmente crea la onda"""
        self.waves.append(self.anim_manager.create_wave(250))

    def add_particles(self):
        """Envía la tarea de crear partículas al buzón"""
        self.task_queue.put(self._internal_add_particles)

    def _internal_add_particles(self):
        """Función interna que realmente crea las partículas"""
        self.particles.append(self.anim_manager.create_particles(20))

    # --- MÉTODOS DEL CICLO DE VIDA ---

    def update(self):
        try:
            self.root.update()
            return self.is_running
        except: 
            return False
        
    def render(self):
        pass  # Se maneja automáticamente
        
    def _on_closing(self):
        self.is_running = False
        self.root.quit()

    def close(self):
        self.is_running = False
        try: self.root.destroy()
        except: pass