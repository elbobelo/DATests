import pygame
import numpy as np
import sys
# Initialize Pygame
pygame.init()
# Create a display window
scree_width, screen_height = 800, 600
screen = pygame.display.set_mode((scree_width, screen_height))
# Set up the value names, add addition names as needed.
test_names = [
    {'name': 'Velocity: ', 'start': 34, 'increment': 1},
    {'name': 'Angel: ', 'start': 14, 'increment': 2},
    {'name': 'Drag: ', 'start': 0.02, 'increment': .01},
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


def run_simulation():
    global test_chosen

    class GolfBall:
        def __init__(self, mass=0.04593, radius=0.021335):
            self.mass = mass  # mass in kg
            self.radius = radius  # radius in meters

    # Initial conditions
    velocity = test[0] # Impact velocity in m/s
    angle = test[1]  # Impact angle in degrees
    mass = .22 # Impact mass in kg

    pos = np.array([0.0, 0.0])   # Ball position
    vel = np.array([velocity * np.cos(angle * np.pi / 180), velocity * np.sin(angle * np.pi / 180)])   # Ball velocity in m/s

    # Time step
    dt = 0.1

    # Number of loops
    n_loops = 200

    # Lists to store position data
    x_positions = [0]
    y_positions = [0]

    # Create a golf ball object
    golf_ball = GolfBall()

    # Define ball's color, size, and initial position
    ball_color = (255, 255, 255)  # White
    ball_radius = 2  # Pixels
    ball_pos = (400, 300)  # Initial position

    # Set the frame rate to 60 FPS
    clock = pygame.time.Clock()

    while pos[1] >= 0 and pos[0] >= 0 and pos[0] <= scree_width and n_loops < 1000:
        # Calculate the drag force in Newtons
        Cd = test[2]# Drag coefficient for a sphere
        rho = 1.225  # Air density at sea level (kg/m^3)
        A = np.pi * golf_ball.radius ** 2  # Frontal area of the ball in m^2
        drag_force = 0.5 * Cd * rho * np.linalg.norm(vel) ** 2 * A

        # Update acceleration in m/s^2
        acc = np.array([-drag_force / golf_ball.mass, -9.8])

        # Update velocity in m/s
        vel += acc * dt

        # Update position in meters
        pos = pos + vel * dt + 0.5 * acc * dt ** 2

        # Append current position to lists
        x_positions.append(pos[0])
        y_positions.append(pos[1])


        # Clear the display window
        screen.fill((0, 0, 0))
        test_code() #TEST_CODE
        # Draw the ball at the updated position
        pygame.draw.circle(screen, ball_color, (int(pos[0]*4), int(screen_height - pos[1]*4)), ball_radius)
        # Update the display
        pygame.display.flip()

        # Limit the frame rate to 60 FPS
        clock.tick(60)

        # Increment number of loops
        n_loops += 1

    # Print the maximum height and total x distance traveled
    max_height = max(y_positions)
    total_x_distance = sum(np.diff(x_positions))
    print(f"Maximum height: {max_height}")
    print(f"Total x distance traveled: {total_x_distance}")
    print(f"Total Distance: {total_x_distance / 0.9144:.2f} yards")


# Run the simulation 5 times
for _ in range(50000):
    run_simulation()

# Quit Pygame
pygame.quit()
