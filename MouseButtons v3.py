import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
SQUARE_SIZE = 100
BUTTON_WIDTH = 100
BUTTON_HEIGHT = 50
FONT_SIZE = 18

# Set up some colors
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the square
square_x = WIDTH // 2 - SQUARE_SIZE // 2
square_y = HEIGHT // 2 - SQUARE_SIZE // 2
draw_square = True

# Set up the buttons
buttons = [
    {"rect": pygame.Rect(10, 10, BUTTON_WIDTH, BUTTON_HEIGHT), "text": "Toggle Square", "callback": lambda: toggle_square()},
    {"rect": pygame.Rect(10, 70, BUTTON_WIDTH, BUTTON_HEIGHT), "text": "Move Left", "callback": lambda: move_square(-1, 0)},
    {"rect": pygame.Rect(10, 130, BUTTON_WIDTH, BUTTON_HEIGHT), "text": "Move Right", "callback": lambda: move_square(1, 0)},
    {"rect": pygame.Rect(10, 190, BUTTON_WIDTH, BUTTON_HEIGHT), "text": "Move Up", "callback": lambda: move_square(0, -1)},
    {"rect": pygame.Rect(10, 250, BUTTON_WIDTH, BUTTON_HEIGHT), "text": "Move Down", "callback": lambda: move_square(0, 1)}
]

# Function to toggle the square
def toggle_square():
    global draw_square
    draw_square = not draw_square

# Function to move the square
def move_square(dx, dy):
    global square_x, square_y
    square_x += dx * SQUARE_SIZE
    square_y += dy * SQUARE_SIZE

# Set up the scroll bars
scroll_x = 0
scroll_y = 0

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for button in buttons:
                if button["rect"].collidepoint(event.pos):
                    button["callback"]()

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

    screen.fill((128, 128, 128))

    if draw_square:
        pygame.draw.rect(screen, BLUE, (square_x - scroll_x, square_y - scroll_y, SQUARE_SIZE, SQUARE_SIZE))

    for button in buttons:
        pygame.draw.rect(screen, BLUE, button["rect"])
        font = pygame.font.Font(None, FONT_SIZE)
        text = font.render(button["text"], True, BLACK)
        text_rect = text.get_rect(center=button["rect"].center)
        screen.blit(text, text_rect)

    font = pygame.font.Font(None, FONT_SIZE)
    text = font.render("X: " + str(square_x) + " Y: " + str(square_y), True, BLACK)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT - 50))
    screen.blit(text, text_rect)

    pygame.display.flip()