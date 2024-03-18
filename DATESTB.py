def calculate_result(rom_bank, address_low, address_high, sprite_number):
    with open('MK2.rom', 'rb') as f:
        f.seek(address_low + sprite_number)
        value_1 = ord(f.read(1))
        f.seek(address_high + sprite_number)
        value_2 = ord(f.read(1))
        result = (value_1 << 8) | value_2
        final_result = (result + 0x10 + rom_bank) & 0xFFFF
        return final_result
