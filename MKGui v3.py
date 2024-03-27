import pygame
import sys

class Sprite:
    def __init__(self, tile_number, offset, tiles):
        self.tile_number = tile_number
        self.offset = offset
        self.tiles = tiles

class Tile:
    def __init__(self, color_palette, offset, pixels):
        self.color_palette = color_palette
        self.offset = offset
        self.pixels = pixels

def draw_tile(sprite):
    for tile in sprite.tiles:
        surface = pygame.Surface((8 * pixel_size, 8 * pixel_size), pygame.SRCALPHA)
        color = color_palettes[tile.color_palette]
        for j, value in enumerate(map(int, tile.pixels)):
            if value != 0:
                pygame.draw.rect(surface, color[value - 1],
                                     ((j % 8) * pixel_size, (j // 8) * pixel_size, pixel_size, pixel_size))
        pygame.draw.rect(surface, (0, 255, 0), (0, 0, 8 * pixel_size, 8 * pixel_size), 1)
        screen.blit(surface, ((tile.offset[0] - sprite.offset[0]) * pixel_size + (screen_size[0] // 2),
                              (tile.offset[1] - sprite.offset[1]) * pixel_size + (screen_size[1] // 2)))

sprite1 = Sprite(8, [14, 19], [
    Tile(0, (8, 3), '0001122200122222011112221222212201111112001031310110313101333131'),
    Tile(0, (12, 1), '0000000001110000122211002222221012222221212222211112222131312221'),
    Tile(1, (14, 8), '0100010001111000011110000011000010002100200001101100011111001331'),
    Tile(0, (11, 9), '0313111133131111133331133331222011102222222112222221122122211213'),
    Tile(0, (4, 15), '0000022200001222000301120112200110022111131211111011111101111111'),
    Tile(1, (8, 16), '1000001121101111022021110111111101111000331113111133101100110111'),
    Tile(3, (16, 16), '0132221013221111111133001333001101003311113300111100110010110000'),
    Tile(1, (8, 8), '0013010101130101010001010011000000100010000111203110001130000011')
])

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

    draw_tile(sprite1)

    # Update the screen
    pygame.display.flip()