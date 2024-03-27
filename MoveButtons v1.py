import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 600, 400
SQUARE_SIZE = 50
BUTTON_SIZE = 20
SCROLL_WIDTH = 10

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the square
square_x = WIDTH // 2
square_y = HEIGHT // 2
square_drawn = True

# Set up the buttons
button_x = [100, 200, 300, 400, 500]
button_y = HEIGHT - BUTTON_SIZE - 10

# Set up the colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Set up the font
font = pygame.font.Font(None, 36)

# Set up the scroll bars
scroll_x = 0
scroll_y = 0

# Define the size of the content
content_width = 2000
content_height = 2000

# Update the scroll bars
scroll_x = (scroll_x / content_width) * WIDTH
scroll_y = (scroll_y / content_height) * HEIGHT

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the mouse is over a button
            for i, x in enumerate(button_x):
                if event.pos[0] >= x and event.pos[0] < x + BUTTON_SIZE:
                    if i == 0:  # Toggle square
                        square_drawn = not square_drawn
                    elif i == 1:  # Move square left
                        square_x -= SQUARE_SIZE
                    elif i == 2:  # Move square right
                        square_x += SQUARE_SIZE
                    elif i == 3:  # Move square up
                        square_y -= SQUARE_SIZE
                    elif i == 4:  # Move square down
                        square_y += SQUARE_SIZE

    # Handle scrolling
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        scroll_y -= 1
    if keys[pygame.K_DOWN]:
        scroll_y += 1
    if keys[pygame.K_LEFT]:
        scroll_x -= 1
    if keys[pygame.K_RIGHT]:
        scroll_x += 1

    # Draw the screen
    screen.fill((128, 128, 128))

    # Draw the square if it's supposed to be drawn
    if square_drawn:
        pygame.draw.rect(screen, BLUE, (square_x - scroll_x, square_y - scroll_y, SQUARE_SIZE, SQUARE_SIZE))

    # Draw the buttons
    for i, x in enumerate(button_x):
        pygame.draw.rect(screen, BLACK, (x, button_y, BUTTON_SIZE, BUTTON_SIZE))
        text = font.render(["Toggle", "Left", "Right", "Up", "Down"][i], True, WHITE)
        screen.blit(text, (x + 5, button_y + 5))




    # Draw the scroll bars
    pygame.draw.rect(screen, BLACK, (0, scroll_y, SCROLL_WIDTH, BUTTON_SIZE))
    pygame.draw.rect(screen, BLACK, (WIDTH - SCROLL_WIDTH, scroll_x, SCROLL_WIDTH, BUTTON_SIZE))

    # Display the position of the square
    position_text = font.render(f"Position: ({square_x // SQUARE_SIZE}, {square_y // SQUARE_SIZE})", True, BLACK)
    screen.blit(position_text, (10, 10))

    # Update the display
    pygame.display.flip()