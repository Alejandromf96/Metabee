"""
Animaciones para la interfaz JARVIS con Tkinter
"""
import math
import random


class AnimationManager:
    """Gestor de animaciones para Canvas de Tkinter"""
    
    def __init__(self, canvas, center, colors):
        self.canvas = canvas
        self.center = center
        self.colors = colors
        self.animations = []
        self.phase = 0
        
    def create_pulsing_orb(self, base_radius=60):
        """Crea un orbe pulsante"""
        orb = {
            'type': 'orb',
            'radius': base_radius,
            'phase': 0,
            'items': []
        }
        return orb
    
    def create_wave(self, max_radius=250):
        """Crea una onda circular expansiva"""
        wave = {
            'type': 'wave',
            'radius': 0,
            'max_radius': max_radius,
            'alpha': 255,
            'item': None
        }
        return wave
    
    def update_orb(self, orb):
        """Actualiza el orbe pulsante"""
        orb['phase'] += 0.05
        pulse = math.sin(orb['phase']) * 15
        current_radius = orb['radius'] + pulse
        
        # Limpiar elementos anteriores
        for item in orb['items']:
            self.canvas.delete(item)
        orb['items'] = []
        
        # Dibujar capas de glow
        for i in range(5, 0, -1):
            alpha = int(50 * i / 5)
            radius = current_radius + (i * 8)
            color = self._get_alpha_color(self.colors['primary'], alpha)
            item = self.canvas.create_oval(
                self.center[0] - radius, self.center[1] - radius,
                self.center[0] + radius, self.center[1] + radius,
                fill=color, outline=''
            )
            orb['items'].append(item)
        
        # Círculo principal
        item = self.canvas.create_oval(
            self.center[0] - current_radius, self.center[1] - current_radius,
            self.center[0] + current_radius, self.center[1] + current_radius,
            fill=self.colors['primary'], outline=self.colors['primary'], width=2
        )
        orb['items'].append(item)
    
    def update_wave(self, wave):
        """Actualiza una onda circular"""
        wave['radius'] += 3
        wave['alpha'] = max(0, 255 - (wave['radius'] / wave['max_radius']) * 255)
        
        if wave['item']:
            self.canvas.delete(wave['item'])
        
        if wave['alpha'] > 0:
            color = self._get_alpha_color(self.colors['primary'], int(wave['alpha']))
            wave['item'] = self.canvas.create_oval(
                self.center[0] - wave['radius'], self.center[1] - wave['radius'],
                self.center[0] + wave['radius'], self.center[1] + wave['radius'],
                outline=color, width=2, fill=''
            )
        
        return wave['radius'] < wave['max_radius']
    
    def create_particles(self, count=20):
        """Crea un sistema de partículas"""
        particles = []
        for _ in range(count):
            angle = random.uniform(0, 2 * math.pi)
            speed = random.uniform(2, 4)
            particles.append({
                'x': self.center[0],
                'y': self.center[1],
                'vx': math.cos(angle) * speed,
                'vy': math.sin(angle) * speed,
                'life': 255,
                'size': random.randint(3, 6),
                'item': None
            })
        return particles
    
    def update_particles(self, particles):
        """Actualiza sistema de partículas"""
        alive = []
        for p in particles:
            p['x'] += p['vx']
            p['y'] += p['vy']
            p['life'] -= 8
            
            if p['item']:
                self.canvas.delete(p['item'])
            
            if p['life'] > 0:
                color = self._get_alpha_color(self.colors['accent'], int(p['life']))
                p['item'] = self.canvas.create_oval(
                    p['x'] - p['size'], p['y'] - p['size'],
                    p['x'] + p['size'], p['y'] + p['size'],
                    fill=color, outline=''
                )
                alive.append(p)
        
        return alive
    
    def _get_alpha_color(self, hex_color, alpha):
        """Convierte color hex con alpha a formato Tkinter"""
        # Tkinter no soporta alpha nativamente, simulamos con colores más oscuros
        r, g, b = self._hex_to_rgb(hex_color)
        factor = alpha / 255
        r = int(r * factor)
        g = int(g * factor)
        b = int(b * factor)
        return f'#{r:02x}{g:02x}{b:02x}'
    
    def _hex_to_rgb(self, hex_color):
        """Convierte hex a RGB"""
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))