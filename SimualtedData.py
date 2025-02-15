import csv
import random

actions = ["Forward", "Left", "Right", "Stop"]

with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Angle", "Distance", "Action"])  # Headers

    for _ in range(2000):  # Generate 2000 random samples
        angle = random.choice(range(-75, 80, 15))  # Choose angles (-75 to 75)
        distance = random.randint(0, 100)  # Distance from object

        # AI Rule: If object is far, move forward. Otherwise, turn away.
        if distance > 30:  
            action = "Forward"
        elif angle < 0:  
            action = "Right"  # Obstacle on the left → Turn right
        elif angle > 0:  
            action = "Left"  # Obstacle on the right → Turn left
        else:  
            action = "Stop"  # Obstacle directly ahead

        writer.writerow([angle, distance, action])

print("✅ Simulated data.csv generated successfully!")
