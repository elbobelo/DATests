import math

class GolfBall:
    def __init__(self):
        self.gravity = 9.81  # m/s^2
        self.initial_velocity = 0
        self.angle = 0
        self.distance = 0
        self.max_height = 0

    def calculate_trajectory(self, club_name, club_length, club_weight, loft_angle, swing_power):
        # Calculate the initial velocity based on club weight and swing power
        self.initial_velocity = math.sqrt(club_weight * swing_power)
        # Calculate the launch angle based on the loft angle and club length
        self.angle = math.radians(loft_angle + (club_length / 10))
        # Calculate the total time of flight
        time_of_flight = (self.initial_velocity * math.sin(self.angle)) / self.gravity
        # Calculate the distance covered
        self.distance = (self.initial_velocity * math.cos(self.angle)) * time_of_flight
        # Calculate the maximum height
        self.max_height = (self.initial_velocity * math.sin(self.angle))**2 / (2 * self.gravity)

        print(f"Club Name: {club_name}")
        print(f"Club Length: {club_length} inches")
        print(f"Club Weight: {club_weight} grams")
        print(f"Club Angle: {loft_angle} degrees")
        print(f"Maximum Height: {self.max_height} yards")
        print(f"Distance Covered: {self.distance} yards")
        print ("")

driver = GolfBall()
driver.calculate_trajectory("Driver", 43, 198, 12, 100)

wood = GolfBall()
wood.calculate_trajectory("Wood", 41, 218, 18, 80)

iron = GolfBall()
iron.calculate_trajectory("Iron", 37, 258, 27, 60)

wedge = GolfBall()
wedge.calculate_trajectory("Wedge", 35, 292, 50, 40)