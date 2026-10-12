"""
Gestor de notas
"""
from datetime import datetime
from pathlib import Path
import os


class NotesManager:
    def __init__(self, notes_dir):
        """Inicializa el gestor de notas"""
        self.notes_dir = Path(notes_dir)
        self.notes_dir.mkdir(parents=True, exist_ok=True)
    
    def create_note(self, content, title=None):
        """Crea una nueva nota"""
        try:
            # Generar nombre de archivo
            if title:
                # Limpiar título para nombre de archivo
                safe_title = "".join(c for c in title if c.isalnum() or c in (' ', '-', '_')).strip()
                filename = f"{safe_title}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            else:
                filename = f"nota_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            
            filepath = self.notes_dir / filename
            
            # Escribir nota
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"{'='*50}\n\n")
                f.write(content)
            
            return True, f"Nota guardada como {filename}"
        except Exception as e:
            return False, f"Error creando nota: {str(e)}"
    
    def open_notes_folder(self):
        """Abre la carpeta de notas"""
        try:
            os.startfile(str(self.notes_dir))
            return True, "Abriendo carpeta de notas"
        except Exception as e:
            return False, f"Error abriendo carpeta: {str(e)}"
    
    def list_notes(self):
        """Lista todas las notas"""
        try:
            notes = list(self.notes_dir.glob("*.txt"))
            if notes:
                note_names = [note.stem for note in sorted(notes)[-5:]]  # Últimas 5
                return True, f"Últimas notas: {', '.join(note_names)}"
            else:
                return True, "No hay notas guardadas aún"
        except Exception as e:
            return False, f"Error listando notas: {str(e)}"