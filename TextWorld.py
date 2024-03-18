import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 640, 480
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the font
font = pygame.font.Font(None, 36)

# Set up the game world
game_world = [
    ['#', '#', '#', '#', '#'],
    ['#', ' ', ' ', ' ', '#'],
    ['#', ' ', ' ', ' ', '#'],
    ['#', ' ', ' ', ' ', '#'],
    ['#', '#', '#', '#', '#']
]

# Set up the player position
player_position = [1, 1]

# Set up the available tiles
available_tiles = [' ', '#', 'D', 'W']

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and player_position[0] > 0:
                game_world[player_position[0]][player_position[1]] = ' '
                player_position[0] -= 1
                game_world[player_position[0]][player_position[1]] = 'P'
            elif event.key == pygame.K_DOWN and player_position[0] < len(game_world) - 1:
                game_world[player_position[0]][player_position[1]] = ' '
                player_position[0] += 1
                game_world[player_position[0]][player_position[1]] = 'P'
            elif event.key == pygame.K_LEFT and player_position[1] > 0:
                game_world[player_position[0]][player_position[1]] = ' '
                player_position[1] -= 1
                game_world[player_position[0]][player_position[1]] = 'P'
            elif event.key == pygame.K_RIGHT and player_position[1] < len(game_world[0]) - 1:
                game_world[player_position[0]][player_position[1]] = ' '
                player_position[1] += 1
                game_world[player_position[0]][player_position[1]] = 'P'
            elif event.key == pygame.K_SPACE:
                tile = input('Which tile do you want to place? (space/hash/D/W): ')
                if tile in available_tiles:
                    game_world[player_position[0]][player_position[1]] = tile

    # Draw the game world
    screen.fill(BLACK)
    for row in range(len(game_world)):
        for col in range(len(game_world[0])):
            text = font.render(game_world[row][col], True, WHITE)
            screen.blit(text, (col * 50, row * 50))

    # Update the display
    pygame.display.flip()