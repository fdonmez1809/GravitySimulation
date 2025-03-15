from vpython import *
import numpy as np

# Prevent VPython from running in notebook mode
import vpython


class Body:
    def __init__(self, mass, initial_positions, radius, dt=100, color=color.white):
        # Object parameters
        self.mass = mass
        self.radius = radius
        self.color = color
        self.dt = dt

        # Motion parameters
        self.positions = [np.array(initial_positions, dtype=float)]
        self.velocity = np.array([0, 0, 0], dtype=float)  # Initial velocity
        self.acceleration = np.array([0, 0, 0], dtype=float)  # Initial acceleration

        # VPython sphere representation
        self.sphere = sphere(pos=vector(*initial_positions), radius=radius, color=color, make_trail=True)

    def apply_force(self, force):
        """ Update acceleration using Newton's Second Law (F = ma) """
        self.acceleration = force / self.mass

    def update(self):
        """ Update velocity and position using simple Euler integration """
        self.velocity += self.acceleration * self.dt
        new_position = self.positions[-1] + self.velocity * self.dt
        self.positions.append(new_position)
        self.sphere.pos = vector(*new_position)  # Update VPython sphere

def gravitational_force(body1, body2):
    """ Compute gravitational force between two bodies using Newton's Law of Universal Gravitation """
    G = 6.674e-11
    r = body2.positions[-1] - body1.positions[-1]
    r_magnitude = np.linalg.norm(r)
    
    if r_magnitude < 1e3:  # Avoid division by zero
        return np.array([0, 0, 0])

    F = G * body1.mass * body2.mass / (r_magnitude ** 2)
    F_vector = (r / r_magnitude) * F  # Normalize direction
    return F_vector

# VPython Scene
scene = canvas(title="3D Gravity Simulation", width=800, height=600, background=color.black)

# 🌍 Define celestial bodies (Scaled for VPython)
earth = Body(5.972e24, [0, 0, 0], radius=6.3e6 * 100, color=color.blue)
moon = Body(7.348e22, [384314400 , 2145253313, 2034500 ], radius=1.7e6 * 100, color=color.white)
bodies = [earth, moon]

# 🚀 Set Initial Velocities for Orbiting (Scaled)
earth.velocity = np.array([0, 0, 0], dtype=float)
moon.velocity = np.array([0, 2000, 0], dtype=float)  # Increased speed for visibility

# 🔄 Simulation Loop
while True:
    rate(100)  # Controls simulation speed
    for body1 in bodies:
        total_force = np.array([0, 0, 0], dtype=float)
        for body2 in bodies:
            if body1 != body2:
                total_force += gravitational_force(body1, body2)
        body1.apply_force(total_force)  # Apply force
        body1.update()  # Update physics
