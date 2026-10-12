"""
Script de diagnóstico para Metabee
"""
import os
import sys

def check_file_exists(filepath):
    """Verifica si un archivo existe"""
    exists = os.path.exists(filepath)
    status = "✓" if exists else "✗"
    print(f"{status} {filepath}")
    return exists

def check_import(module_path, class_name):
    """Verifica si se puede importar una clase"""
    try:
        module = __import__(module_path, fromlist=[class_name])
        getattr(module, class_name)
        print(f"✓ {module_path}.{class_name}")
        return True
    except Exception as e:
        print(f"✗ {module_path}.{class_name}: {e}")
        return False

print("=" * 60)
print("DIAGNÓSTICO DE METABEE".center(60))
print("=" * 60)

print("\n1. Verificando estructura de archivos:")
print("-" * 60)

files = [
    "main.py",
    "requirements.txt",
    "config/__init__.py",
    "config/settings.py",
    "core/__init__.py",
    "core/voice_engine.py",
    "core/command_processor.py",
    "core/system_controller.py",
    "commands/__init__.py",
    "commands/app_launcher.py",
    "commands/browser_control.py",
    "commands/system_control.py",
    "commands/notes_manager.py",
    "ui/__init__.py",
    "ui/jarvis_interface.py",
    "ui/animations.py",
]

all_exist = all(check_file_exists(f) for f in files)

print("\n2. Verificando imports:")
print("-" * 60)

imports = [
    ("core.voice_engine", "VoiceEngine"),
    ("core.command_processor", "CommandProcessor"),
    ("core.system_controller", "SystemController"),
    ("commands.app_launcher", "AppLauncher"),
    ("commands.browser_control", "BrowserControl"),
    ("commands.system_control", "SystemControl"),
    ("commands.notes_manager", "NotesManager"),
    ("ui.jarvis_interface", "JarvisInterface"),
]

all_imported = all(check_import(module, cls) for module, cls in imports)

print("\n" + "=" * 60)
if all_exist and all_imported:
    print("✓ TODO CORRECTO - Metabee está listo para ejecutar".center(60))
    print("=" * 60)
    print("\nEjecuta: python main.py")
else:
    print("✗ HAY PROBLEMAS - Revisa los errores arriba".center(60))
    print("=" * 60)