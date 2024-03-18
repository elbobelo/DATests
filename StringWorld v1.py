import pygame
import random

# Initialize Pygame
pygame.init()

# Set the dimensions of the square
square_size = 60

# Create a 10x6 grid of green colors
grid = [[(0, 255, 0) for _ in range(10)] for _ in range(6)]

# Create a block that's the size of 1 square
block = [(0, 0, 0)]

# Set the initial position of the block
block_x = (10 * square_size) / 2
block_y = (6 * square_size) / 2

# Set the window dimensions
window_size = (10 * square_size, 6 * square_size)

# Create the window
screen = pygame.display.set_mode(window_size)

# Define the movement speed
speed = 1

# Create a string of random 1s and 0s
random_string = ''.join(str(random.randint(0, 1)) for _ in range(60 * 60))

# Define the offsets
MapX = 10
MapY = 10

# Create a list to hold the sections of the string
sections = []

# Split the string into sections
for i in range(6):
    section = random_string[(i * MapY) + MapX:((i + 1) * MapY) + MapX]
    sections.append(section)

# Print the sections
for i, section in enumerate(sections):
    print(f"Section {i+1}: {section}")

# Loop until the user closes the window
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Get the state of the arrow keys
    keys = pygame.key.get_pressed()

    # Move the block based on the arrow key presses
    if keys[pygame.K_LEFT]:
        block_x -= speed
    if keys[pygame.K_RIGHT]:
        block_x += speed
    if keys[pygame.K_UP]:
        block_y -= speed
    if keys[pygame.K_DOWN]:
        block_y += speed

    # Keep the block inside the window
    if block_x < 0:
        block_x = 0
    elif block_x > window_size[0] - square_size:
        block_x = window_size[0] - square_size
    if block_y < 0:
        block_y = 0
    elif block_y > window_size[1] - square_size:
        block_y = window_size[1] - square_size

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the grid
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(screen, grid[i][j], (j * square_size, i * square_size, square_size, square_size))
    # Loop through each character in the string
    for i, section in enumerate(sections):
        for j, char in enumerate(section):
            # Determine the color based on the character
            if char == '1':
                color = (0, 255, 0)  # Green
            else:
                color = (165, 129, 61)  # Brown

            # Calculate the position of the square
            x = j * square_size
            y = i * square_size

            # Draw the square
            pygame.draw.rect(screen, color, (x, y, square_size, square_size))
    # Draw the block
    pygame.draw.rect(screen, block[0], (block_x, block_y, square_size, square_size))

    # Update the display
    pygame.display.update()