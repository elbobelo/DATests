import tkinter as tk

# Define the Sprite class
class Sprite:
    def __init__(self, tile_count, offset, tiles):
        self.tile_count = tile_count
        self.offset = offset
        self.tiles = tiles

# Define the Tile class
class Tile:
    def __init__(self, color_palette, offset, pixels):
        self.color_palette = color_palette
        self.offset = offset
        self.pixels = pixels

# Define the color palettes
color_palettes = [
    ['', '#000000', '#FF0000', '#FFC0CB'],  # Black, Red, Pink
    ['', '#000000', '#0000FF', '#FFFFFF'],  # Black, Blue, White
    ['', '#000000', '#00FF00', '#FFC0CB'],  # Black, Green, Pink
    ['', '#000000', '#FFFF00', '#FFFFFF']  # Black, Yellow, White
]

# Create a list of tiles
sprite1 = Sprite(8, [14, 19], [
    Tile(0, (8, 3), '0001122200122222011112221222212201111112001031310110313101333131'),
    Tile(0, (12, 1), '0000000001110000122211002222221012222221212222211112222131312221'),
    Tile(1, (14, 8), '0100010001111000011110000011000010002100200001101100011111001331'),
    Tile(0, (11, 9), '0313111133131111133331133331222011102222222112222221122122211213'),
    Tile(0, (4, 15), '0000022200001222000301120112200110022111131211111011111101111111'),
    Tile(1, (8, 16), '1000001121101111022021110111111101111000331113111133101100110111'),
    Tile(3, (16, 16), '0132221013221111111133001333001101003311113300111100110010110000'),
    Tile(1, (8, 8), '0013010101130101010001010011000000100010000111203110001130000011')
])

def draw_tile(tile, pixel_size):
    tile_x = (tile.offset[0] - sprite1.offset[0]) * pixel_size + scroll_offset[0]
    tile_y = (tile.offset[1] - sprite1.offset[1]) * pixel_size + scroll_offset[1]
    for i in range(8):
        for j in range(8):
            color = color_palettes[tile.color_palette][int(tile.pixels[i*8+j])]
            canvas.create_rectangle(j * pixel_size + tile_x, i * pixel_size + tile_y,
                                    (1 + j) * pixel_size + tile_x, (1 + i) * pixel_size + tile_y,
                                    fill=color, outline='black')
    # Draw a blue rectangle around the tile
    canvas.create_rectangle(tile_x, tile_y,
                            8 * pixel_size + tile_x, 8 * pixel_size + tile_y,
                            outline='cyan')

# Function to update the selected tile
def update_selected_tile(event):
    global selected_tile
    x = event.x
    y = event.y
    for i, tile in enumerate(sprite1.tiles):
        tile_x = (tile.offset[0] - sprite1.offset[0]) * pixel_size + scroll_offset[0]
        tile_y = (tile.offset[1] - sprite1.offset[1]) * pixel_size + scroll_offset[1]
        if (tile_x <= x < 8 * pixel_size + tile_x
                and tile_y <= y < 8 * pixel_size + tile_y) :
            selected_tile = i
            selected_tile_label.config(text=f'Selected Tile: {selected_tile}')
            break

# Define the pixel size
pixel_size = 8
scroll_offset = (200, 200)

# Create the main window
root = tk.Tk()

# Create a canvas
canvas = tk.Canvas(root, width=(400), height=(400), highlightthickness=0)
canvas.config(bg='gray')
canvas.pack(side=tk.LEFT)

# Create a frame for the menu
menu_frame = tk.Frame(root)
menu_frame.pack(side=tk.RIGHT, fill=tk.Y)

# Create a label to display the selected tile
selected_tile_label = tk.Label(menu_frame, text='Selected Tile: None')
selected_tile_label.pack()

# Initialize the selected tile variable
selected_tile = None

# Bind the left mouse click to the update_selected_tile function
canvas.bind('<Button-1>', update_selected_tile)

for tile in sprite1.tiles:
    draw_tile(tile, pixel_size)

# Start the main loop
root.mainloop()