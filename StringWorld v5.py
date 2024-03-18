import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Set the dimensions of the screen
screen_width, screen_height = 600, 600
# Set the size of a block
block_size = 1
# Set the dimensions of the grid
width, height = 1000, 1000
# Set up the color scheme
color_zero = (14, 235, 204)
color_one = (14, 135, 204)
# Create a Pygame window
screen = pygame.display.set_mode((screen_width, screen_height))

# Create a 1000x1000 grid of random 1s and 0s
grid = [[random.choice([0, 1]) for _ in range(width)] for _ in range(height)]

# Set the initial offsets
offset_x, offset_y = 0, 0
TEST1 = 1

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
    if current_time - last_update >= 1000 / 60:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            offset_x -= 1
        if keys[pygame.K_RIGHT]:
            offset_x += 1
        if keys[pygame.K_UP]:
            offset_y -= 1
        if keys[pygame.K_DOWN]:
            offset_y += 1
        if keys[pygame.K_z]:
            TEST1 -= 1
        if keys[pygame.K_x]:
            TEST1 += 1

        last_update = current_time

    # Clear the grid surface
    grid_surface.fill((0, 0, 0))

    # Draw the grid
    for y in range(1, 20):
        for x in range(1, screen_width // (block_size + y) + 2):
            # Calculate the grid coordinates
            grid_x = (x + offset_x - (screen_width // ((block_size + y)) // 2)) % len(grid[0])
            grid_y = (y + offset_y) % len(grid)
            color = color_one if grid[grid_y][grid_x] == 1 else color_zero
            pygame.draw.rect(grid_surface, color,
                             (x * (block_size + y) - (block_size + y) + (screen_width % (block_size + y)) // 2, 300 + y * (block_size + y) // 2, block_size + y,
                              block_size + y))



    # Draw the grid surface onto the screen
    screen.blit(grid_surface, (0, 0))
    # Draw the coordinates
    font = pygame.font.Font(None, 36)
    coordinates = font.render("X: " + str(offset_x) + " Y: " + str(offset_y) + " TEST1: " + str(TEST1), True, (255, 255, 255))
    screen.blit(coordinates, (10, 10))
    # Display grid_x and grid_y
    grid_coordinates = font.render("grid_x: " + str(grid_x) + " grid_y: " + str(grid_y), True, (255, 255, 255))
    screen.blit(grid_coordinates, (10, 50))
    # Update the screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()