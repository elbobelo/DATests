rom_name = 'MK2.rom'
header = 0x10
properties = {
    'pixel': {
        'rom_bank': 0x08000,
        'base_low': 0x10388,
        'base_high': 0x102FE
    },
    'tile': {
        'rom_bank': 0x20000,
        'base_low': 0x2B61E,
        'base_high': 0x2B537
    }
}

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

# Open the ROM file once at the start of the main program
try:
    with open(rom_name, 'rb') as rom_file:
        # Ensure the sprite number is within the valid range
        sprite_number = int(input("Enter a sprite number (0-137): "))
        if sprite_number < 0 or sprite_number > 137:
            print("Invalid sprite number. Please enter a number between 0 and 137.")
        else:
            print("tile properties: ", hex(get_address(properties['tile'], sprite_number)))
            print("sprite pixels: ", hex(get_address(properties['pixel'], sprite_number)))
except FileNotFoundError:
    print("Error: File not found.")