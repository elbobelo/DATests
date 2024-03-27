import tkinter as tk

# Your string of pixel colors
pixels = '0001122200122222011112221222212201111112001031310110313101333131'

# Create a new Tkinter window
window = tk.Tk()

# Create a new 8x8 canvas
canvas = tk.Canvas(window, width=8, height=8)
canvas.pack()

# Define the colors to use for each pixel value
colors = {
    '0': 'red',
    '1': 'green',
    '2': 'blue',
    '3': 'yellow'
}

# Loop over each character in the string
for i, pixel in enumerate(pixels):
    # Calculate the row and column of the current pixel
    row = i // 8
    col = i % 8

    # Draw a small rectangle on the canvas at the current position, using the color corresponding to the current pixel value
    canvas.create_rectangle(col, row, col+1, row+1, fill=colors[pixel])

# Start the Tkinter event loop
window.mainloop()