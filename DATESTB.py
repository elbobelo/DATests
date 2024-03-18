def calculate_result(rom_bank, address_low, address_high, sprite_number):
    with open('MK2.rom', 'rb') as f:
        f.seek(address_low + sprite_number)
        value_1 = ord(f.read(1))
        f.seek(address_high + sprite_number)
        value_2 = ord(f.read(1))
        result = (value_1 << 8) | value_2
        final_result = (result + 0x10 + rom_bank) & 0xFFFF
        return final_result

# Ensure the sprite number is within the valid range
sprite_number = int(input("Enter a sprite number (0-137): "))
if sprite_number < 0 or sprite_number > 137:
    print("Invalid sprite number. Please enter a number between 0 and 137.")
else:
    print("sprite pixels: ", hex(calculate_result(0x08000, 0x10388, 0x102FE, sprite_number)))
    print("tile properties: ", hex(calculate_result(0x20000, 0x2B61E, 0x2B537, sprite_number)))