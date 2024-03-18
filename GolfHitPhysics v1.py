import numpy as np

class GolfBall:
    def __init__(self, mass=0.04593, radius=0.021335):
        self.mass = mass  # mass in kg
        self.radius = radius  # radius in meters

class Club:
    def __init__(self, name, length, weight, loft_angle, max_power):
        self.name = name
        self.length = length  # in inches
        self.weight = weight  # in kg
        self.loft_angle = loft_angle  # in degrees
        self.max_power = max_power  # in percentage

    def hit(self, ball):
        # Convert weight from grams to kilograms
        weight_kg = self.weight / 1000
        # Convert length from inches to meters
        length_m = self.length * 0.0254
        # Calculate the speed in m/s using the formula
        swing_power = 100
        speed = swing_power * weight_kg * length_m
        # Convert speed from m/s to mph
        velocity = speed * 2.237

        angle = np.radians(self.loft_angle)
        vx = speed * np.cos(angle)
        vy = speed * np.sin(angle)
        g = -9.81
        t = 0
        t_max = (2 * speed * np.sin(angle)) / 9.81
        x = 0
        y = 0
        max_height = 0

        while y >= 0:
            x = speed * np.cos(angle) * t
            y = speed * np.sin(angle) * t - 0.5 * 9.81 * t ** 2
            if y > max_height:
                max_height = y
                t_max = t
            t += 0.01

        distance = x   # Convert meters to yards

        print(f"Club: {self.name}")
        print(f"Weight: {self.weight:.2f} kg")
        print(f"Loft angle: {self.loft_angle} degrees")
        print(f"Swing power: {swing_power}%")
        print(f"Maximum height: {max_height:.2f} meters")
        print(f"Distance: {distance * 1.0936:.2f} yards")
        print()

golf_ball = GolfBall()
driver = Club("Driver", 43, 198, 12, 1)
wood = Club("Wood", 41, 218, 18, .8)
iron = Club("Iron", 37, 258, 27, .6)
wedge = Club("Wedge", 35, 292, 50, .4)

clubs = [driver, wood, iron, wedge]

for club in clubs:
    club.hit(golf_ball)
