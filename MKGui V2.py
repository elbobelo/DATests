import pygame
import sys

class Sprite:
    def __init__(self, tile_number, offset, tiles):
        self.tile_number = tile_number
        self.offset = offset
        self.tiles = tiles

class Tile:
    def __init__(self, pixels, color_palette, offset):
        self.pixels = pixels
        self.color_palette = color_palette
        self.offset = offset

def draw_tile(tile):
    surface = pygame.Surface((8 * pixel_size, 8 * pixel_size), pygame.SRCALPHA)
    color = color_palettes[tile.color_palette]
    for j, value in enumerate(map(int, tile.pixels)):
        if value != 0:
            pygame.draw.rect(surface, color[value - 1],
                                 ((j % 8) * pixel_size, (j // 8) * pixel_size, pixel_size, pixel_size))
    pygame.draw.rect(surface, (0, 255, 0), (0, 0, 8 * pixel_size, 8 * pixel_size), 1)
    screen.blit(surface, ((tile.offset[0] - Sprite.offset[0]) * pixel_size + (screen_size[0] // 2),
                          (tile.offset[1] - Sprite.offset[1]) * pixel_size + (screen_size[1] // 2)))

# Create instances of the Tile class and add them to the tiles list
Sprite.tile_number = 8
Sprite.offset = (14, 19)
Sprite.tiles = [
    Tile('0001122200122222011112221222212201111112001031310110313101333131', 0, (8, 3)),
    Tile('0000000001110000122211002222221012222221212222211112222131312221', 0, (12, 1)),
    Tile('0100010001111000011110000011000010002100200001101100011111001331', 1, (14, 8)),
    Tile('0313111133131111133331133331222011102222222112222221122122211213', 0, (11, 9)),
]

# Initialize Pygame
pygame.init()

# Create the game window
screen_size = (300, 300)
screen = pygame.display.set_mode(screen_size)
screen.fill((105, 105, 105))

# Set the title of the window
pygame.display.set_caption("Tile Viewer")

# The color palettes
color_palettes = [
    [(0, 0, 0), (255, 0, 0), (255, 105, 180)],  # Black, Red, Pink
    [(0, 0, 0), (0, 0, 255), (255, 255, 255)],  # Black, Blue, White
    [(0, 0, 0), (0, 255, 0), (255, 105, 180)],  # Black, Green, Pink
    [(0, 0, 0), (255, 255, 0), (255, 255, 255)]  # Black, Yellow, White
]

pixel_size = 8

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Create and draw the tiles in a single loop
    for tile in Sprite.tiles:
        draw_tile(tile)

    # Update the screen
    pygame.display.flip()