import tkinter as tk

# color palettes
color_palettes = [
    ['', '#000000', '#FF0000', '#FFC0CB'],  # Black, Red, Pink
    ['', '#000000', '#0000FF', '#FFFFFF'],  # Black, Blue, White
    ['', '#000000', '#00FF00', '#FFC0CB'],  # Black, Green, Pink
    ['', '#000000', '#FFFF00', '#FFFFFF']  # Black, Yellow, White
]

# Sprite Class
class Sprite:
    def __init__(self, tile_count, offset, tiles):
        self.tile_count = tile_count
        self.offset = offset
        self.tiles = tiles

# Tile Class
class Tile:
    def __init__(self, color_palette, offset, pixels):
        self.color_palette = color_palettes[color_palette]
        self.offset = offset
        self.pixels = pixels

# create the main window
root = tk.Tk()

# create a canvas
canvas = tk.Canvas(root, width=200, height=200, bg="lightgray")
canvas.grid(row=0, column=0)

# create a sprite
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

# build and draw tiles
for tile in sprite1.tiles:
    image = tk.PhotoImage(width=8*4, height=8*4)
    for i in range(64):
        color = tile.color_palette[int(tile.pixels[i])]
        image.put(color, (i%8*4, i//8*4))
    canvas.create_image(tile.offset[0]*8*4, tile.offset[1]*8*4, image=image)

# start the main loop
root.mainloop()