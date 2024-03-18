import math
'''
This code simulates the flight of a golf ball based on the club's loft angle, mass, and speed.
The ball's horizontal and vertical position are updated at each time step.
The loop continues until the ball hits the ground (vertical position becomes negative)
or the simulation time exceeds the maximum time. The maximum height and total distance traveled
by the ball are calculated and printed out. The drag coefficient (Cd), air density (rho), and spin rate
are constants that can be adjusted to simulate different ball types and clubs.
The coefficient of restitution (COR) is also used to simulate energy loss on impact.
The distance is converted from meters to yards at the end.
'''

class GolfBall:
    def __init__(self, mass=0.04593, radius=0.021335):
        self.mass = mass  # mass in kg
        self.radius = radius  # radius in meters

class GolfClub:
    # Represents a golf club with its name, length, mass, and initial swing and loft angles.
    def __init__(self, name, length, mass, theta, alpha):
        # Initializes a GolfClub object with the given parameters.
        self.name = name  # name of the golf club
        self.length = length  # length of the golf club in meters.
        self.mass = mass  # mass of the golf club in kilograms.
        self.theta = theta  # initial swing angle of the club in degrees.
        self.alpha = alpha  # initial loft angle of the club in degrees.

    def calculate_club_head_speed(self, r, grip, dtheta_dt, dalpha_dt, g):
        # Calculates the club head speed based on swing and club parameters.
        a = g * (dtheta_dt * grip * math.sin(math.radians(self.theta)) + dalpha_dt * self.length * math.sin(
            math.radians(self.alpha))) / self.mass
        v = math.sqrt(2 * a * self.length)
        Vx = v * math.cos(math.radians(self.alpha))
        return Vx


# Create golf clubs
driver = GolfClub('Driver', 1.1, 0.22, 110, 12)
wood = GolfClub('Wood', 1.0, 0.20, 105, 18)
iron = GolfClub('Iron', 0.9, 0.25, 100, 25)
wedge = GolfClub('Wedge', 0.8, 0.30, 95, 45)

# Calculate club head speed
r = .5  # radius of the golfer's swing (m)
grip = .30  # distance from grip (P) to center of mass (G) of the club (m)
dtheta_dt = 30  # rate of change of swing angle (rad/s)
dalpha_dt = 20  # rate of change of club angle (rad/s)
g = 9.8  # gravitational acceleration (m/s²)

time_step = 0.01  # time step in seconds
max_time = 10  # max simulation time in seconds

# Air resistance constants (adjust these for different ball types)
Cd = .27  # drag coefficient
rho = 1.225  # air density (kg/m^3)

# Spin rate (adjust for different clubs and swing speeds)
spin_rate = 2600  # revolutions per minute (RPM)

# Coefficient of restitution (COR)
COR = .08

# Loop over each club
for club in [driver, wood, iron, wedge]:
    Vx = club.calculate_club_head_speed(r, grip, dtheta_dt, dalpha_dt, g)
    ball = GolfBall()
    x = 0  # horizontal position of the ball
    y = 0  # vertical position of the ball
    max_height = 0
    total_distance = 0
    time = 0
    omega = spin_rate * 2 * math.pi / 60  # convert RPM to rad/s

    # Simulate the ball's flight
    while y >= 0 and time <= max_time:
        # update horizontal position
        x += Vx * time_step

        # calculate air resistance force
        F_drag = 0.5 * Cd * rho * math.pi * ball.radius**2 * Vx**2

        # update vertical velocity (factoring in club mass, air resistance, and spin)
        vy = Vx * math.tan(math.radians(club.alpha)) - 0.5 * g * time_step + (F_drag * time_step) / ball.mass
        vy *= COR  # apply COR for energy loss
        vy += omega * ball.radius  # add lift due to spin
        y += vy * time_step

        # update max height
        max_height = max(max_height, y)

        # Update total distance (horizontal motion only)
        total_distance += Vx * time_step

        time += time_step

    print(f"Club: {club.name}")
    print(f"Length: {club.length} m")
    print(f"Mass: {club.mass:.2f} kg")
    print(f"Theta angle: {club.theta:.2f} degrees")
    print(f"Alpha angle: {club.alpha:.2f} degrees")
    print(f"Club Speed: {Vx:.2f} m/s")
    print(f"Max Height: {max_height:.2f} m")
    print(f"Total Distance: {total_distance / 0.9144:.2f} yards")
    print()