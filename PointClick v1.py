import pygame
import math

# Initialize Pygame
pygame.init()

# Create a window
win = pygame.display.set_mode((800, 600))

# Set object properties
object_x = 400
object_y = 300
object_speed = 0.3  # Base speed
object_size = 10
initial_size = 10  # Adjust this for the initial size

# Set target properties (initially not set)
target_x = None
target_y = None


# Scaling factor (adjust for desired scaling sensitivity)
scaling_factor = 0.02

# Top boundary limit
top_boundary = win.get_height() / 2

# Bottom boundary limit
bottom_boundary = win.get_height() * 3 / 4

# Main game loop
running = True
while running:

    # Set background color
    win.fill((100, 100, 100))
    # Create a gray rectangle for the bottom 3/4 of the screen
    pygame.draw.rect(win, (0, 0, 0), (0, bottom_boundary, win.get_width(), win.get_height() - bottom_boundary))
    # Create a sky blue rectangle for the top half of the screen
    pygame.draw.rect(win, (135, 206, 235), (0, 0, win.get_width(), win.get_height() / 2))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            target_x, target_y = event.pos
            if target_y < win.get_height() / 2:
                object_size -= 1
            else:
                object_size += 1

    # Calculate distance to target (if set)
    distance = 0
    if target_x and target_y:
        distance = math.sqrt((target_x - object_x) ** 2 + (target_y - object_y) ** 2)

    # Ensure object stays within top boundary
    object_y = max(object_y - object_size / 2, top_boundary)

    # Ensure object stays within bottom boundary
    object_y = min(object_y + object_size / 2, bottom_boundary)

    # Scale the object based on its y position
    object_size = max(1, int((object_y - top_boundary) * scaling_factor * 4))

    # Check if the object has reached its target
    if distance < object_size:
        target_x = None
        target_y = None

    # Move the object towards the target (if set)
    if target_x and target_y:
        # Adjust speed based on object size
        new_speed = object_speed * (object_size / initial_size)
        object_x += new_speed * (target_x - object_x) / distance
        object_y += new_speed * (target_y - object_y) / distance / 2

    # Draw the object
    pygame.draw.circle(win, (255, 255, 255), (int(object_x), int(object_y)), object_size)

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()