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

        print(str(int(bin(int(pixel_data[i * 32 + 16:i * 32 + 32], 16))[2:])).zfill(64))
        print(str(int(bin(int(pixel_data[i * 32:i * 32 + 16], 16))[2:])).zfill(64))
        pixels = str(2 * int(bin(int(pixel_data[i * 32 + 16:i * 32 + 32], 16))[2:])
                     + int(bin(int(pixel_data[i * 32:i * 32 + 16], 16))[2:])).zfill(64)

        tiles.append(Tile(color_palette, [horizontal_offset, vertical_offset], pixels))

    return Sprite(num_tiles, [sprite_hor_offset, sprite_ver_offset], tiles)

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

            # Print the variables and their values
            print(f"Number of tiles in the sprite: {sprite.tile_number}")
            print(f"Sprite offset: {sprite.offset}")
            print(f"Tile properties:")
            for i, tile in enumerate(sprite.tiles):
                print(f"Tile {i + 1} - Color palette: {tile.color_palette}, "
                      f"Tile offset: {tile.offset}")
                print(f"Decompressed tile {i + 1}: {tile.pixels}")

except FileNotFoundError:
    print("Error: File not found.")