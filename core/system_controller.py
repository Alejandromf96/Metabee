"""
Controlador principal del sistema Metabee
"""
import threading
import time
from datetime import datetime


class SystemController:
    """Controlador principal que coordina todos los componentes"""
    
    def __init__(self, voice_engine, command_processor, ui):
        """Inicializa el controlador del sistema"""
        self.voice = voice_engine
        self.processor = command_processor
        self.ui = ui
        self.is_running = False
        self.listen_thread = None
    
    def start(self):
        """Inicia el sistema Metabee"""
        self.is_running = True
        
        # Saludo inicial
        greeting = self._get_greeting()
        self.voice.speak(greeting)
        self.ui.set_status(greeting)
        self.ui.add_particles()
        
        # Iniciar thread de escucha
        self.listen_thread = threading.Thread(target=self._listen_loop, daemon=True)
        self.listen_thread.start()
    
    def _get_greeting(self):
        """Genera saludo según la hora del día"""
        hour = datetime.now().hour
        
        if 5 <= hour < 12:
            return "Buenos días, jefe. ¿Qué vamos a hacer hoy?"
        elif 12 <= hour < 19:
            return "Buenas tardes, jefe. Estoy listo para asistirte"
        else:
            return "Buenas noches, jefe. ¿En qué puedo ayudarte?"
    
    def _listen_loop(self):
        """Loop principal de escucha"""
        while self.is_running:
            try:
                self.ui.set_status("Esperando comando...")
                self.ui.set_listening(True)
                
                command = self.voice.listen(timeout=10)
                
                self.ui.set_listening(False)
                
                if command:
                    self.ui.set_command(command)
                    self.ui.add_wave()
                    
                    self.ui.set_status("Procesando...")
                    # El procesador ahora devuelve el mensaje que Metabee debe decir
                    success, response = self.processor.process(command)
                    
                    # 1. Metabee habla la respuesta
                    self.voice.speak(response)
                    
                    # 2. Actualizar UI con el texto de la respuesta
                    self.ui.set_status(response)
                    
                    if success:
                        self.ui.add_particles()
                    
                    # Esperar un poco para que el usuario lea la respuesta en pantalla
                    time.sleep(3)
                    self.ui.set_command("")
                
                else:
                    time.sleep(0.5)
            
            except Exception as e:
                # Si hay un error, lo imprimimos pero no detenemos el hilo
                print(f"Error en listen_loop: {e}")
                time.sleep(1)
    
    def stop(self):
        """Detiene el sistema"""
        self.is_running = False
        self.voice.speak("Hasta luego, jefe")
        time.sleep(2)