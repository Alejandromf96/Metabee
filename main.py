"""
Metabee - Asistente de Voz Local
Punto de entrada principal
"""
import sys
from config.settings import (
    VOICE_CONFIG, APPS, YOUTUBE_CHANNELS, 
    NOTES_DIR, UI_COLORS
)
from core.voice_engine import VoiceEngine
from core.command_processor import CommandProcessor
from core.system_controller import SystemController
from commands.app_launcher import AppLauncher
from commands.browser_control import BrowserControl
from commands.system_control import SystemControl
from commands.notes_manager import NotesManager
from ui.metabee_interface import MetabeeInterface
from ui.animations import AnimationManager

def main():
    """Función principal"""
    print("=" * 60)
    print("METABEE - Asistente de Voz Local".center(60))
    print("=" * 60)
    print()
    
    try:
        # Inicializar componentes
        print("Inicializando motor de voz...")
        voice_engine = VoiceEngine(VOICE_CONFIG)
        
        print("Inicializando controladores...")
        app_launcher = AppLauncher(APPS)
        browser_control = BrowserControl(APPS, YOUTUBE_CHANNELS)
        system_control = SystemControl()
        notes_manager = NotesManager(NOTES_DIR)
        
        print("Configurando procesador de comandos...")
        command_processor = CommandProcessor(
            app_launcher,
            browser_control,
            system_control,
            notes_manager
        )
        
        print("Inicializando interfaz gráfica...")
        ui = MetabeeInterface(UI_COLORS)
        
        print("Iniciando sistema...")
        controller = SystemController(voice_engine, command_processor, ui)
        controller.start()
        
        print("\n✓ Metabee está listo!")
        print("\n📋 Comandos disponibles:")
        print("  🪟 Ventanas: Maximiza/Minimiza [Chrome/VS Code]")
        print("  📂 Carpetas: Abre [documentos/descargas/escritorio/imágenes]")
        print("  🔧 Aplicaciones: Abre [vscode/chrome/gmail]")
        print("  🔊 Audio: Sube/baja el volumen, silencia")
        print("  🔍 Búsqueda: Busca en Google [tema]")
        print("  🎬 YouTube: Reproduce [canción/video]")
        print("  📧 Gmail: Abre bandeja, correo")
        print("  📝 Notas: Anota que [contenido]")
        print("\n💡 Lee COMANDOS.md para la lista completa y ejemplos")
        print("Presiona ESC para salir o cierra la ventana\n")
        
        # Loop principal de UI
        running = True
        while running:
            running = ui.update()
            ui.render()
        
        # Cerrar limpiamente
        print("\nCerrando Metabee...")
        controller.stop()
        ui.close()
        
        print("¡Hasta luego!")
    
    except KeyboardInterrupt:
        print("\n\nInterrumpido por el usuario")
    except Exception as e:
        print(f"\n❌ Error crítico: {e}")
        import traceback
        traceback.print_exc()
    finally:
        sys.exit(0)


if __name__ == "__main__":
    main()