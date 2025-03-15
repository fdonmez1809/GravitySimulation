import pygame
import numpy as np
import scipy

# parameters and constants
G = 6.674e-11  # Gravitational constant
SCALE = 1e9  # Scale factor for visualization
WIDTH, HEIGHT = 800, 600  # parameters for pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
td = 0.0005


# functions
def _magnitude(arr):
    return np.sqrt(arr[0] ** 2 + arr[1] ** 2 + arr[2] ** 2)

def _unit_vector(arr):
    mag = _magnitude(arr)
    return np.array([[arr[0] / mag, arr[1] / mag, arr[2] / mag]])



# classes
class body:
    def __init__(self, position, mass, radius, color, thickness): # attributes
        self.position = position
        self.mass = mass
        self.velocity = np.array([0,0], dtype=float) # initial velocity
        self.acceleration = np.array([0,0], dtype=float) # initial acceleration
        self.force = np.array([0, 0], dtype=float) # initial force
        
        # drawing parameters
        self.radius = radius
        self.color = color
        self.thickness = thickness
        
    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.position[0], self.position[1]), self.radius, self.thickness)
        
    def add_velocity(self, velocity_array):
        self.velocity += np.array(velocity_array, dtype=np.float64)

    def add_force(self, force_array):
        self.force += np.array(force_array, dtype=np.float64)

    def update_pos(self):
        acceleration = self.force / self.mass # F=ma
        self.velocity += acceleration * td # euler's forward method
        self.position += self.velocity * td # euler's forward method
        pass

class gravity:
    def __init__(self):
        self.bodies = []
                
    def body_arr(self, bodies): # creates a list of numpy arrays with bodies and their index numbers
        self.body_list = [np.array([i, body]) for i, body in enumerate(bodies)]

    
        
        
        
    pass 

earth = body(position=[WIDTH // 2, HEIGHT // 2], mass=5.97e24, radius=20, color=(0, 0, 255), thickness=10)
    
    
#pygame.draw.circle(surface, color, (x, y), radius)


# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # Clear screen (black)
    earth.draw(screen)  # Draw the ball
    pygame.display.flip()  # Update display

pygame.quit()