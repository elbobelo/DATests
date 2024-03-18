'''
102FE = Sprite address lower
10388 = Sprite address higher
2B537 = Tile Position Lower
2B61E = Tile Position Higher
'''

def read_hex_values(sprite_number):
    # Open the 6502 ROM in binary mode
    with open('MK2.rom', 'rb') as f:
        # Seek to the position of HEX value 1
        f.seek(int('10388', 16) + sprite_number)
        # Read and convert to string
        hex_value_1 = f.read(1).hex()
        print(hex_value_1)

        # Seek to the position of HEX value 2
        f.seek(int('102FE', 16) + sprite_number)
        # Read and convert to string
        hex_value_2 = f.read(1).hex()
        print(hex_value_2)

        # Concatenate the two hexadecimal strings
        result = hex_value_1 + hex_value_2

    # Treat the result as a hexadecimal value, convert to integer, add 0x2010, and convert back to hexadecimal string
    final_result = hex(int(result, 16) + 0x8010)[2:]

    return final_result

# Ensure the sprite number is within the valid range
sprite_number = int(input("Enter a sprite number (0-137): "))
if sprite_number < 0 or sprite_number > 137:
    print("Invalid sprite number. Please enter a number between 0 and 137.")
else:
    print(read_hex_values(sprite_number))