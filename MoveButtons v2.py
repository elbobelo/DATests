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

# Set up the squares
square_x = [WIDTH // 2, WIDTH // 2 + 100]
square_y = [HEIGHT // 2, HEIGHT // 2 + 100]
square_drawn = [True, True]
selected_square = None

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
            # Check if the mouse is over a square
            for i, (x, y) in enumerate(zip(square_x, square_y)):
                if (event.pos[0] >= (x - scroll_x) and event.pos[0] < (x - scroll_x) + SQUARE_SIZE and event.pos[1]
                        >= (y - scroll_y) and event.pos[1] < (y - scroll_y) + SQUARE_SIZE):
                    selected_square = i
            # Check if the mouse is over a button
            for i, x in enumerate(button_x):
                if (event.pos[0] >= x and event.pos[0] < x + BUTTON_SIZE and event.pos[1]
                        >= button_y and event.pos[1] < button_y + BUTTON_SIZE):
                    if selected_square is not None:
                        if i == 0:  # Toggle square
                            square_drawn[selected_square] = not square_drawn[selected_square]
                        elif i == 1:  # Move square left
                            square_x[selected_square] -= SQUARE_SIZE
                        elif i == 2:  # Move square right
                            square_x[selected_square] += SQUARE_SIZE
                        elif i == 3:  # Move square up
                            square_y[selected_square] -= SQUARE_SIZE
                        elif i == 4:  # Move square down
                            square_y[selected_square] += SQUARE_SIZE

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

    # Draw the squares if they're supposed to be drawn
    for i, (x, y, drawn) in enumerate(zip(square_x, square_y, square_drawn)):
        if drawn:
            pygame.draw.rect(screen, BLUE, (x - scroll_x, y - scroll_y, SQUARE_SIZE, SQUARE_SIZE))

    # Draw the buttons
    for i, x in enumerate(button_x):
        pygame.draw.rect(screen, BLACK, (x, button_y, BUTTON_SIZE, BUTTON_SIZE))
        text = font.render(["Toggle", "Left", "Right", "Up", "Down"][i], True, WHITE)
        screen.blit(text, (x + 5, button_y + 5))

    # Display the position of the selected square
    if selected_square is not None:
        position_text = font.render(
            f"Position: ({square_x[selected_square] // SQUARE_SIZE}, {square_y[selected_square] // SQUARE_SIZE})", True,
            BLACK)
        screen.blit(position_text, (10, 10))

    # Update the display
    pygame.display.flip()