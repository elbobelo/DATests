def read_byte_from_address(file, address):
    file.seek(address)
    return ord(file.read(1))

def get_address(rom_bank, base_low, base_high, sprite_number):
    try:
        low_byte = read_byte_from_address(rom_file, base_low + sprite_number)
        high_byte = read_byte_from_address(rom_file, base_high + sprite_number)
        address = (low_byte << 8) | high_byte
        converted_address = address + 0x10 + rom_bank
        return converted_address
    except IOError:
        print("Error: Unable to read from file.")

# Open the ROM file once at the start of the main program
try:
    with open('MK2.rom', 'rb') as rom_file:
        # Ensure the sprite number is within the valid range
        sprite_number = int(input("Enter a sprite number (0-137): "))
        if sprite_number < 0 or sprite_number > 137:
            print("Invalid sprite number. Please enter a number between 0 and 137.")
        else:
            print("sprite pixels: ", hex(get_address(0x08000, 0x10388, 0x102FE, sprite_number)))
            print("tile properties: ", hex(get_address(0x20000, 0x2B61E, 0x2B537, sprite_number)))
except FileNotFoundError:
    print("Error: File not found.")