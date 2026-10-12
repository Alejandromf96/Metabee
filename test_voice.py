"""
Script de prueba para verificar que el sistema de voz funciona correctamente
Ejecuta este script antes de usar Metabee para asegurarte de que todo está configurado
"""

import sys
from pathlib import Path

# Agregar el directorio actual al path para importar módulos
sys.path.insert(0, str(Path(__file__).parent))

from config.settings import VOICE_CONFIG
from core.voice_engine import VoiceEngine

def test_voice_engine():
    """Prueba el motor de voz"""
    print("=" * 60)
    print("PRUEBA DEL MOTOR DE VOZ - METABEE")
    print("=" * 60)
    print()
    
    try:
        print("1️⃣ Inicializando motor de voz...")
        voice = VoiceEngine(VOICE_CONFIG)
        print("   ✅ Motor de voz inicializado correctamente")
        
        print("\n2️⃣ Probando síntesis de voz (TTS)...")
        print("   📢 Metabee dirá: 'Hola, soy Metabee. El sistema de voz funciona correctamente.'")
        voice.speak("Hola, soy Metabee. El sistema de voz funciona correctamente.")
        
        print("\n3️⃣ Probando reconocimiento de voz...")
        print("   🎤 Escuchando durante 5 segundos...")
        print("   💡 Intenta decir: 'Abre Chrome' o 'Maximiza VS Code'")
        
        command = voice.listen(timeout=5, phrase_time_limit=5)
        
        if command:
            print(f"\n   ✅ Escuché: '{command}'")
        else:
            print("\n   ⚠️ No se escuchó ningún comando. Verifica el micrófono.")
        
        print("\n4️⃣ Prueba de respuesta:")
        if command:
            voice.speak(f"Recibí tu comando: {command}")
        else:
            voice.speak("El reconocimiento de voz parece no estar funcionando. Verifica tu micrófono y conexión a Internet.")
        
        print("\n" + "=" * 60)
        print("✅ PRUEBA COMPLETADA")
        print("=" * 60)
        print("\nConfiguración actual:")
        print(f"  • Velocidad de voz: {VOICE_CONFIG['rate']} (0-300)")
        print(f"  • Volumen: {VOICE_CONFIG['volume'] * 100}%")
        print(f"  • Índice de voz: {VOICE_CONFIG['voice_index']} (0=masculino, 1=femenino)")
        
        print("\n💡 Tips:")
        print("  - Si la voz es muy rápida, reduce 'rate' en config/settings.py")
        print("  - Si la voz es muy lenta, aumenta 'rate'")
        print("  - Si el volumen es bajo, aumenta 'volume'")
        print("  - Para cambiar a voz femenina, cambia 'voice_index' a 1")
        
        print("\n✨ ¡Todo listo! Ahora puedes ejecutar: python main.py")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\nSolución de problemas:")
        print("  1. Verifica que tengas instalados los requisitos: pip install -r requirements.txt")
        print("  2. Asegúrate de que tu micrófono esté conectado y funcione")
        print("  3. Verifica que tengas conexión a Internet (necesaria para Google Speech Recognition)")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_voice_engine()
