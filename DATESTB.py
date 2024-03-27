from tkinter import *
import random

# Function to generate a random RGB color
def get_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"#{r:02x}{g:02x}{b:02x}"

# Main program
root = Tk()

# Create the label
label = Label(root, width=400, height=400, bg="white")
label.pack()

# Generate random colors
colors = [get_random_color() for _ in range(64)]  # Generate 64 random colors for the grid

# Calculate cell width and height
cell_width = 400 // 8
cell_height = 400 // 8

# Place colored squares in a grid on the label
for row in range(8):
    for col in range(8):
        color_index = row * 8 + col  # Calculate the index for the current cell's color
        x1 = col * cell_width
        y1 = row * cell_height
        x2 = x1 + cell_width
        y2 = y1 + cell_height
        canvas = Canvas(label, width=cell_width, height=cell_height, bg=colors[color_index], highlightthickness=0)
        canvas.place(x=x1, y=y1)

root.mainloop()