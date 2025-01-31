import pygame
from circleshape import CircleShape
import random
from constants import *

class Asteroid(CircleShape):
    containers = ()

    def __init__(self, x, y, radius, vx, vy):
        super().__init__(x, y, radius)  # Initialize position and radius from CircleShape
        
        # Initialize velocity vector (vx, vy)
        self.velocity = pygame.Vector2(vx, vy)

        # Add the asteroid to the appropriate containers
        self.add(*self.containers)

    def draw(self, screen):
        # Use position.x and position.y to get the asteroid's centroid coordinates
        pygame.draw.circle(
            screen,  # The screen surface
            (255, 255, 255),  # The color (white)
            (int(self.position.x), int(self.position.y)),  # Centroid coordinates
            self.radius,  # Radius of the asteroid
            2  # Outline width (only the edge drawn)
        )

    def update(self, dt):
        # Update position based on velocity and delta time (dt)
        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        # Generate random angle between 20 and 50 degrees
        random_angle = random.uniform(20, 50)
        
        # Create new velocity vectors
        new_velocity1 = self.velocity.rotate(random_angle)
        new_velocity2 = self.velocity.rotate(-random_angle)
        
        # Calculate new radius
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        # Create two new asteroids...
        Asteroid(
            self.position.x,  
            self.position.y,  
            new_radius,
            new_velocity1.x*1.2,  
            new_velocity1.y*1.2   
        )
        Asteroid(
            self.position.x,  
            self.position.y,  
            new_radius,
            new_velocity2.x*1.2,  
            new_velocity2.y*1.2   
        )

