"""
Motor de reconocimiento y síntesis de voz
"""
import speech_recognition as sr
import pyttsx3
import threading
import queue


class VoiceEngine:
    def __init__(self, config):
        """Inicializa el motor de voz"""
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        
        # Inicializar TTS (Text-to-Speech)
        self.tts_engine = pyttsx3.init()
        self.tts_engine.setProperty('rate', config['rate'])
        self.tts_engine.setProperty('volume', config['volume'])
        
        # Configurar voz
        voices = self.tts_engine.getProperty('voices')
        if len(voices) > config['voice_index']:
            self.tts_engine.setProperty('voice', voices[config['voice_index']].id)
        
        # Cola para procesamiento asíncrono
        self.speech_queue = queue.Queue()
        self.is_speaking = False
        
        # Ajustar para ruido ambiente
        with self.microphone as source:
            print("Calibrando micrófono...")
            self.recognizer.adjust_for_ambient_noise(source, duration=2)
    
    def speak(self, text):
        """Habla el texto de forma asíncrona"""
        self.speech_queue.put(text)
        if not self.is_speaking:
            threading.Thread(target=self._process_speech_queue, daemon=True).start()
    
    def _process_speech_queue(self):
        """Procesa la cola de texto a hablar"""
        self.is_speaking = True
        while not self.speech_queue.empty():
            text = self.speech_queue.get()
            print(f"Metabee: {text}")
            self.tts_engine.say(text)
            self.tts_engine.runAndWait()
        self.is_speaking = False
    
    def listen(self, timeout=5, phrase_time_limit=5):
        """Escucha y reconoce comandos de voz"""
        try:
            with self.microphone as source:
                print("Escuchando...")
                audio = self.recognizer.listen(
                    source, 
                    timeout=timeout, 
                    phrase_time_limit=phrase_time_limit
                )
            
            print("Procesando audio...")
            # Reconocer usando Google Speech Recognition
            command = self.recognizer.recognize_google(audio, language='es-ES')
            print(f"Usuario: {command}")
            return command.lower()
        
        except sr.WaitTimeoutError:
            return None
        except sr.UnknownValueError:
            self.speak("No pude entender lo que dijiste, jefe")
            return None
        except sr.RequestError:
            self.speak("Hay un problema con el servicio de reconocimiento de voz")
            return None
        except Exception as e:
            print(f"Error en listen: {e}")
            return None