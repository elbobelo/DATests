'''
Hello, can you help writing a Pygame. The Pygame should first create a 1000 * 1000 string of random 1s and 0s.
That string represents a world that is 1000 blocks wide and 1000 blocks tall. I want the game to display
only 10 by 10 sections of the world at a time. The sections that make up the 10 rows should be sequences of this.
(String+offsetY * 1000) + offsetX.  The 1s should print brown squares and the 0s should be green squares.
Pressing right should increase the X offset by 1. Pressing down should increase the y offset by 1.
This should create a map of green and brown blocks that we can scroll in 4 directions.
That is close, but the whole display is moving to reveal the new sections. What I really need is  for the new
sections to appear in the display, and for the display to stay still.
'''
import pygame
import random

# Initialize Pygame
pygame.init()

# Set the dimensions of the grid
width, height = 1000, 1000

# Create a 1000x1000 grid of random 1s and 0s
grid = [[random.choice([0, 1]) for _ in range(width)] for _ in range(height)]

# Set the size of a block
block_size = 16

# Set the dimensions of the screen
screen_width, screen_height = 10 * block_size, 10 * block_size

# Create a Pygame window
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the initial offsets
offset_x, offset_y = 0, 0

# Create a surface to hold the grid
grid_surface = pygame.Surface((10 * block_size, 10 * block_size))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                offset_x -= 1
            elif event.key == pygame.K_RIGHT:
                offset_x += 1
            elif event.key == pygame.K_UP:
                offset_y -= 1
            elif event.key == pygame.K_DOWN:
                offset_y += 1

    # Clear the grid surface
    grid_surface.fill((0, 0, 0))

    # Draw the grid
    for y in range(0, 10):
        for x in range(0, 10):
            color = (165, 42, 42) if grid[y + offset_y][x + offset_x] == 1 else (0, 255, 0)
            pygame.draw.rect(grid_surface, color, (x * block_size, y * block_size, block_size, block_size))

    # Draw the grid surface onto the screen
    screen.blit(grid_surface, (0, 0))

    # Update the screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()