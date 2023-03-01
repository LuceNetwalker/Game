import re

from pygame.math import Vector2
from pygame.transform import scale_by

from exceptions import InvalidMapInput

from utils import load_sprite, load_sound

class Map:
    TILE_DICT = {
        "grass": "Grass",
        "sea": "Sea",
        "street": "Street",
    }
    def __init__(self, null_position=Vector2(0, 0)) -> None:
        self.map = []
        self.null_pos = null_position

    def init_structure(self, map_representation):
        for i, row in enumerate(map_representation):
            row_array = []
            for j, tile in enumerate(row):
                p = re.compile(": ")
                ini_params = p.split(tile)
                ini_params = list(map(lambda x: x.lower(), ini_params))
                position = (Tile.TILE_DIMENSION * j, Tile.TILE_DIMENSION * i)
                row_array.append(globals()[self.TILE_DICT[ini_params[0]]](position, ini_params[1]))
            
            self.map.append(row_array)

    def draw(self, surface):
        starting_x = int(self.null_pos[1] // Tile.TILE_DIMENSION)
        starting_y = int(self.null_pos[0] // Tile.TILE_DIMENSION)

        map_y = len(self.map)
        map_x = len(self.map[0])

        _, _, xwidth, ywidth = surface.get_rect()
        screen_tilewidth_x = xwidth // Tile.TILE_DIMENSION + 1 
        screen_tilewidth_y = ywidth // Tile.TILE_DIMENSION + 1 

        screen_tilewidth_x = starting_x + xwidth if starting_x + xwidth <= map_x else map_x
        screen_tilewidth_y = starting_y + ywidth if starting_y + ywidth <= map_y else map_y

        for row in self.map[starting_y:screen_tilewidth_y]:
            for tile in row[starting_x:screen_tilewidth_x]:
                tile.draw(surface, self.null_pos)
        


class Tile:
    DIRECTION_DICT: dict = {
        "up": (0, -1),
        "right": (1, 0),
        "down": (0, 1),
        "left": (-1, 0),
    }
    SCALE: int = 2
    TILE_DIMENSION: int = 22 * SCALE
    def __init__(self, position: tuple, sprite, direction="up") -> None:
        self.position = Vector2(position)
        self.sprite = scale_by(sprite, self.SCALE)
        self.radius = sprite.get_width() / 2
        try:
            self.direction = Vector2(self.DIRECTION_DICT[direction])
        except InvalidMapInput:
            print("Direction: " + direction + f"\nPosition: x({position[0]}); y({position})") 

        self.rect = sprite.get_rect()

    def draw(self, surface, null_pos):
        blit_position = self.position - null_pos
        surface.blit(self.sprite, blit_position)

class Grass(Tile):
    def __init__(self, position, direction) -> None:
        super().__init__(position, load_sprite("grass"), direction)

class Sea(Tile):
    def __init__(self, position, direction) -> None:
        super().__init__(position, load_sprite("sea"), direction)

class Street(Tile):
    def __init__(self, position, direction) -> None:
        super().__init__(position, load_sprite("street"), direction)

class CreateMap(Map):
    def __init__(self, null_position=Vector2(0, 0), grid_size=(30, 20), starting_ground="grass") -> None:
        super().__init__(null_position)
        self._init_starting_ground(grid_size, starting_ground)

    def _init_starting_ground(self, grid_size, starting_ground):
        for i in range(grid_size[1]):
            row_array = []
            for j in range(grid_size[0]):
                position = (Tile.TILE_DIMENSION * j, Tile.TILE_DIMENSION * i)
                row_array.append(globals()[self.TILE_DICT[starting_ground]](position, "up"))
            
            self.map.append(row_array)