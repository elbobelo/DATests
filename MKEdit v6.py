rom_name = 'MK2.rom'
header = 0x10
properties = {
    'offset': {
        'rom_bank': 0x20000,
        'base_low': 0x2B61E,
        'base_high': 0x2B537
    },
    'pixel': {
        'rom_bank': 0x08000,
        'base_low': 0x10388,
        'base_high': 0x102FE
    }
}

def decompress_tile(group_a, group_b):
    decompressed_tile = ''
    for hex_a, hex_b in zip(group_a, group_b):
        bin_a = format(hex_a, '08b')
        bin_b = format(hex_b, '08b')
        for bit_a, bit_b in zip(bin_a, bin_b):
            decompressed_tile += ''.join(['0', '2', '1', '3'][2 * int(bit_a) + int(bit_b)])
    return decompressed_tile

def read_byte_from_address(file, address):
    file.seek(address)
    return ord(file.read(1))

def get_address(properties, sprite_number):
    try:
        low_byte = read_byte_from_address(rom_file, properties['base_low'] + sprite_number)
        high_byte = read_byte_from_address(rom_file, properties['base_high'] + sprite_number)
        address = (low_byte << 8) | high_byte
        converted_address = address + header + properties['rom_bank']
        return converted_address
    except IOError:
        print("Error: Unable to read from file.")

def load_sprite(rom_file, offset_address, pixel_address):
    # Read header information
    rom_file.seek(offset_address)
    num_tiles, sprite_hor_offset, sprite_ver_offset, unknown = rom_file.read(4)

    tiles = []
    decompressed_tiles = []

    # Read tile offsets
    for _ in range(num_tiles):
        horizontal_offset, vertical_offset = rom_file.read(2)
        # Extract the color palette information from the vertical offset
        color_palette = (vertical_offset & 0xE0) >> 5
        # Subtract the color palette value from the vertical offset to get the actual offset
        vertical_offset = vertical_offset & 0x1F
        tiles.append((horizontal_offset, vertical_offset, color_palette))

    # Read compressed tiles
    rom_file.seek(pixel_address)
    # Skip the first value
    rom_file.read(1)
    for _ in range(num_tiles):
        compressed_tile_a = [ord(rom_file.read(1)) for _ in range(8)]
        compressed_tile_b = [ord(rom_file.read(1)) for _ in range(8)]
        decompressed_tile = decompress_tile(compressed_tile_a, compressed_tile_b)
        decompressed_tiles.append(decompressed_tile)

    return num_tiles, sprite_hor_offset, sprite_ver_offset, unknown, tiles, decompressed_tiles

try:
    with open(rom_name, 'rb') as rom_file:
        # Ensure the sprite number is within the valid range
        sprite_number = int(input("Enter a sprite number (0-137): "))
        if sprite_number < 0 or sprite_number > 137:
            print("Invalid sprite number. Please enter a number between 0 and 137.")
        else:
            offset_address = get_address(properties['offset'], sprite_number)
            print(hex(offset_address))
            pixel_address = get_address(properties['pixel'], sprite_number)
            print(hex(pixel_address))

            num_tiles, sprite_hor_offset, sprite_ver_offset, unknown, tiles, decompressed_tiles = load_sprite(rom_file, offset_address, pixel_address)

            # Print the variables and their values
            print(f"Number of tiles in the sprite: {num_tiles}")
            print(f"Sprite horizontal offset: {sprite_hor_offset}")
            print(f"Sprite vertical offset: {sprite_ver_offset}")
            print(f"Unknown value: {unknown}")

            print("Tile properties:")
            for i, (horizontal_offset, vertical_offset, color_palette) in enumerate(tiles):
                print(f"Tile {i + 1} - Horizontal offset: {horizontal_offset}, "
                      f"Vertical offset: {vertical_offset}, "
                      f"Color palette: {color_palette}")
                print(f"Decompressed tile {i + 1}: {decompressed_tiles[i]}")

except FileNotFoundError:
    print("Error: File not found.")