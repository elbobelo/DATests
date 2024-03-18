import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 640, 480
# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the value names, add addition names as needed.
test_names = [
    {'name': '1: ', 'start': 1, 'increment': 1},
    {'name': '2: ', 'start': 2, 'increment': 2},
    {'name': '3: ', 'start': 3.0, 'increment': .5},
]
test = [d['start'] for d in test_names]
test_chosen = 0
def test_code():
    global test_chosen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_i, pygame.K_k):
                test_chosen = (
                        (test_chosen + (1 if event.key == pygame.K_k else -1)) % len(test))
            elif event.key in (pygame.K_j, pygame.K_l):
                test[test_chosen] += (
                    test_names[test_chosen]['increment'] if event.key == pygame.K_l
                    else -test_names[test_chosen]['increment'])

    list(map(lambda i: screen.blit(pygame.font.Font(
        None, 30 - (i - test_chosen) % len(test) * 5).render(test_names[i]['name'] + str(test[i]),
        True,
        (0xFF, 0x00, 0X00)),
        (10, 10 + (i - test_chosen) % len(test) * 20)), range(len(test))))

# Main Game loop
while True:
    # Clear the screen
    screen.fill((0xFF, 0xFF, 0xFF))

    test_code() #TEST_CODE

    # Update the display
    pygame.display.flip()