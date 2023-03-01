from pygame import Color
from pygame.image import load
from pygame.math import Vector2
from pygame.mixer import Sound
from pydoc import locate

def load_sprite(name, with_alpha=True):
    path = f"assets/sprites/{name}.png"
    loaded_sprite = load(path)

    if with_alpha:
        return loaded_sprite.convert_alpha()
    else:
        return loaded_sprite.convert()

def load_sound(name):
    path = f"assets/sounds/{name}.wav"
    return Sound(path)

def print_text(surface, text, font, color=Color("tomato")):
    text_surface = font.render(text, True, color)

    rect = text_surface.get_rect()
    rect.center = Vector2(surface.get_size()) / 2

    surface.blit(text_surface, rect)
