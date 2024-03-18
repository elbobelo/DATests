import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Set the dimensions of the screen
screen_width, screen_height = 300, 600
# Set the size of a block
block_size = 1
# Set the dimensions of the grid
width, height = 1000, 1000

# Create a Pygame window
screen = pygame.display.set_mode((screen_width, screen_height))

# Create a 1000x1000 grid of random 1s and 0s
grid = [[random.choice([0, 1]) for _ in range(width)] for _ in range(height)]

# Set the initial offsets
offset_x, offset_y = 0, 0

# Create a surface to hold the grid
grid_surface = pygame.Surface((screen_width, screen_height))

# Game loop
running = True
last_update = pygame.time.get_ticks()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    current_time = pygame.time.get_ticks()
    if current_time - last_update >= 1000 / 30:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            offset_x -= 1
        if keys[pygame.K_RIGHT]:
            offset_x += 1
        if keys[pygame.K_UP]:
            offset_y -= 1
        if keys[pygame.K_DOWN]:
            offset_y += 1

        last_update = current_time

    # Clear the grid surface
    grid_surface.fill((0, 0, 0))

    # Draw the grid
    for y in range(screen_height // block_size):
        for x in range(screen_width // (block_size + y) + 1):
            color = (14, 135, 204) if grid[y + offset_y][x + offset_x] == 1 else (14, 235, 204)
            pygame.draw.rect(grid_surface, color,
                             (x * (block_size + y), y * (block_size + y), block_size + y, block_size + y*2 +1))

    # Draw the grid surface onto the screen
    screen.blit(grid_surface, (0, 0))

    # Update the screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()