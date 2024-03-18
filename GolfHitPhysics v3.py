import math

class GolfBall:
    def __init__(self, mass=0.04593, radius=0.021335):
        self.mass = mass  # mass in kg
        self.radius = radius  # radius in meters
class GolfClub:
    # Represents a golf club with its name, length, mass, and initial swing and loft angles.
    def __init__(self, name, length, mass, theta, alpha):
        # Initializes a GolfClub object with the given parameters.
        self.name = name
        self.length = length
        self.mass = mass
        self.theta = theta
        self.alpha = alpha

    def calculate_club_head_speed(self, r, grip, dtheta_dt, dalpha_dt, g):
        # Calculates the club head speed based on swing and club parameters.
        a = g * (dtheta_dt * grip * math.sin(math.radians(self.theta)) + dalpha_dt * self.length * math.sin(math.radians(self.alpha))) / self.mass
        v = math.sqrt(2 * a * self.length)
        Vx = v * math.cos(math.radians(self.alpha))
        return Vx

# Create golf clubs
driver = GolfClub('Driver', 1.1, 0.22, 110, 12)
wood = GolfClub('Wood', 1.0, 0.20, 105, 18)
iron = GolfClub('Iron', 0.9, 0.25, 100, 25)
wedge = GolfClub('Wedge', 0.8, 0.30, 95, 60)

# Calculate club head speed
r = .5  # radius of the golfer's swing (m)
grip = 0.30  # distance from grip (P) to center of mass (G) of the club (m)
dtheta_dt = 30  # rate of change of swing angle (rad/s)
dalpha_dt = 20  # rate of change of club angle (rad/s)
g = 9.8  # gravitational acceleration (m/s²)

for club in [driver, wood, iron, wedge]:
    Vx = club.calculate_club_head_speed(r, grip, dtheta_dt, dalpha_dt, g)
    print(f"Club: {club.name}")
    print(f"Length: {club.length} m")
    print(f"Mass: {club.mass:.2f} kg")
    print(f"Theta angle: {club.theta:.2f} degrees")
    print(f"Alpha angle: {club.alpha:.2f} degrees")
    print(f"Club Speed: {Vx:.2f} m/s")
    print()