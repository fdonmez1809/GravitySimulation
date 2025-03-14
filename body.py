import pygame 
import numpy as np

class body:
    def __init__(self, mass, position, velocity, radius):
        self.time = np.array([0, 1, 2, 3, 4])
        self.mass = mass
        self.position = position # an erray
        self.velocity = velocity
        self.radius = radius
        self.acceleration = velocity
    
        
    
print("Simulation running...")
