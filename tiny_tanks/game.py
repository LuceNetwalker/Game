import pygame 

from utils import load_sprite
from map import Map, CreateMap
from player import PlayerMark

map_representation =   [["grass: up", "sea: down", "street: left","grass: up", "sea: down", "street: left"],
                        ["grass: up", "sea: down", "street: left", "grass: up", "sea: down", "street: left"],
                        ["grass: up", "sea: down", "street: left"]]

class TinyTanks:
    FPS = 60
    def __init__(self) -> None:
        self._init_pygame()
        self.screen = pygame.display.set_mode((800, 600))
        self.background = load_sprite("space", False)

        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 64)
        
        self.map = CreateMap(self.FPS)
        self.playermark = PlayerMark((0, 0))
        # self.map.init_structure(map_representation)

    def main_loop(self):
        while True:
            self._handle_input()
            self._process_game_logic()
            self._draw()

    def _init_pygame(self):
        pygame.init()
        pygame.display.set_caption("Tiny Tanks")

    def _handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                quit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_w:
                self.playermark.update_position("up")
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                self.playermark.update_position("left")
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                self.playermark.update_position("down")
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                self.playermark.update_position("right")

    def _process_game_logic(self):
        pass

    def _draw(self):
        # self.screen.blit(self.background, (0, 0))
        self.map.draw(self.screen)
        self.playermark.draw(self.screen, self.map.null_pos)    

        pygame.display.flip()
        self.clock.tick(self.FPS)