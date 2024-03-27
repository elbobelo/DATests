import pygame
import sys
rom_name = 'MK2.rom'
header = 0x10

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

def get_address(rom_bank, base_low, base_high, sprite_number):
    try:
        rom_file.seek(base_low + sprite_number)
        low_byte = ord(rom_file.read(1))
        rom_file.seek(base_high + sprite_number)
        high_byte = ord(rom_file.read(1))
        address = (low_byte << 8) | high_byte
        return address + header + rom_bank
    except IOError:
        print("Error: Unable to read from file.")

def load_sprite(rom_file, offset_address, pixel_address):
    # get offset data
    rom_file.seek(offset_address)
    num_tiles, sprite_hor_offset, sprite_ver_offset, unknown = rom_file.read(4)
    offset_data = rom_file.read(2 * num_tiles)

    # get pixel data
    rom_file.seek(pixel_address)
    rom_file.read(1)
    pixel_data = rom_file.read(16 * num_tiles).hex()

    tiles = []

    for i in range(num_tiles):
        horizontal_offset = offset_data[i * 2]
        color_palette, vertical_offset = divmod(offset_data[i * 2 + 1] & 0x7F, 0x20)

        pixels = str(2 * int(bin(int(pixel_data[i * 32 + 16:i * 32 + 32], 16))[2:])
                     + int(bin(int(pixel_data[i * 32:i * 32 + 16], 16))[2:])).zfill(64)

        tiles.append(Tile(color_palette, [horizontal_offset, vertical_offset], pixels))

    return Sprite(num_tiles, [sprite_hor_offset, sprite_ver_offset], tiles)

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

try:
    with open(rom_name, 'rb') as rom_file:
        # Ensure the sprite number is within the valid range
        sprite_number = int(input("Enter a sprite number (0-137): "))
        if sprite_number < 0 or sprite_number > 137:
            print("Invalid sprite number. Please enter a number between 0 and 137.")
        else:
            offset_address = get_address(0x20000, 0x2B61E, 0x2B537, sprite_number)
            pixel_address = get_address(0x08000, 0x10388, 0x102FE, sprite_number)
            sprite = load_sprite(rom_file, offset_address, pixel_address)
except FileNotFoundError:
    print("Error: File not found.")

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

    draw_tile(sprite)

    # Update the screen
    pygame.display.flip()