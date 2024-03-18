class ROM:
    def __init__(self, rom_bank, address_low, address_high, sprite_offset, read_length):
        self.rom_bank = rom_bank
        self.address_low = address_low
        self.address_high = address_high
        self.sprite_offset = sprite_offset
        self.read_length = read_length

    def read_hex_values(self, sprite_number):
        with open('MK2.rom', 'rb') as f:
            f.seek(self.address_low + sprite_number * self.sprite_offset)
            hex_value_1 = f.read(self.read_length).hex()
            print(hex_value_1)

            f.seek(self.address_high + sprite_number * self.sprite_offset)
            hex_value_2 = f.read(self.read_length).hex()
            print(hex_value_2)

            result = hex_value_1 + hex_value_2

        final_result = hex(int(result, 16) + 0x10 + self.rom_bank)[2:]

        return final_result

# Ensure the sprite number is within the valid range
sprite_number = int(input("Enter a sprite number (0-137): "))
if sprite_number < 0 or sprite_number > 137:
    print("Invalid sprite number. Please enter a number between 0 and 137.")
else:
    sprite_pixels = ROM(0x08000, 0x10388, 0x102FE, 1, 1)
    tile_properties = ROM(0x20000, 0x2B61E, 0x2B537, 1, 1)
    print("sprite pixels: ", sprite_pixels.read_hex_values(sprite_number))
    print("tile properties: ", tile_properties.read_hex_values(sprite_number))
