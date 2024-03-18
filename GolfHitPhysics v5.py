import numpy as np
import matplotlib.pyplot as plt

class GolfBall:
    def __init__(self, mass=0.04593, radius=0.021335):
        self.mass = mass  # mass in kg
        self.radius = radius  # radius in meters

# Initial conditions
velocity = 34.0  # Impact velocity in m/s
angle = 14.0  # Impact angle in degrees
mass = .22 # Impact mass in kg

pos = np.array([0.0, 0.0])   # Ball position
vel = np.array([velocity * np.cos(angle * np.pi / 180), velocity * np.sin(angle * np.pi / 180)])   # Ball velocity in m/s

# Time step
dt = 0.1

# Number of loops
n_loops = 20

# Lists to store position data
x_positions = [0]
y_positions = [0]

# Create a golf ball object
golf_ball = GolfBall()

# Run the simulation
while pos[1] >= 0 and n_loops < 100:

    # Calculate the drag force in Newtons
    Cd = 0.27  # Drag coefficient for a sphere
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

    # Increment number of loops
    n_loops += 1

# Print the maximum height and total x distance traveled
max_height = max(y_positions)
total_x_distance = sum(np.diff(x_positions))
print(f"Maximum height: {max_height}")
print(f"Total x distance traveled: {total_x_distance}")
print(f"Total Distance: {total_x_distance / 0.9144:.2f} yards")

# Create a figure and a set of subplots
fig, ax = plt.subplots()

# Plot the position over time
ax.plot(x_positions, y_positions)

# Set labels and title
ax.set_xlabel('X Position')
ax.set_ylabel('Y Position')
ax.set_title('Position over Time')

# Show the plot
plt.show()