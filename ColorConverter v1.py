def convert_8bit_color_to_pygame(color):
    # Convert the 8-bit color value to a decimal value
    decimal_color = int(color, 16)

    # Calculate the RGB values based on the decimal value
    red = (decimal_color & 0x0F) * 32
    green = ((decimal_color & 0xF0) >> 4) * 32
    blue = ((decimal_color & 0x0F00) >> 8) * 32

    # Create a Pygame color object with the calculated RGB values
    pygame_color = pygame.Color(red, green, blue)

    return pygame_color

def convert_8bit_to_rgb(color_value):
    # Extract the color index (0-12)
    color_index = color_value & 0x0F

    # Extract the shade (0-3)
    shade = (color_value >> 4) & 0x03

    # Define the rainbow colors from blue to cyan
    rainbow_colors = [
        (0, 0, 255),  # Blue
        (0, 255, 0),  # Green
        (255, 255, 0),  # Yellow
        (255, 0, 0),  # Red
        (255, 0, 255),  # Magenta
        (0, 255, 255),  # Cyan
    ]

    # Calculate the RGB values based on the color index and shade
    r, g, b = rainbow_colors[color_index % 7]
    r = r * (shade + 1) // 4
    g = g * (shade + 1) // 4
    b = b * (shade + 1) // 4

    return r, g, b

color = 0X31

print(convert_8bit_to_rgb(color))