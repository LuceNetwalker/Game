from pygame.math import Vector2

from map import Tile
from utils import load_sprite

class PlayerMark(Tile):
    def __init__(self, position, direction="up") -> None:
        super().__init__(position, load_sprite("player_mark", True), direction)
        self.blink = False
        # self.clock

    def update_position(self, walk_direction):
        self.position += Vector2(self.DIRECTION_DICT[walk_direction]) * self.TILE_DIMENSION

    def set_blink(self):
        self.blink = True

    def unset_blink(self):
        self.blink = False

    def animate(self, fps):
        


    # def draw(self, surface, null_pos):
    #     if self.blink:
    #     super().draw(surface, null_pos)