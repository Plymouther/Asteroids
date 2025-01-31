from circleshape import CircleShape
import pygame

SHOT_RADIUS = 5

# Creating the shot
class Shot(CircleShape): 
    def __init__(self, x, y):  
        super().__init__(x, y, SHOT_RADIUS) # in the mother, we have x, y, and radius. These are the ones we use here
        self.velocity = pygame.Vector2(0, 0)

    def draw(self, screen):

        # Use position.x and position.y to get the shot's centroid coordinates
        pygame.draw.circle(
            screen,  # The screen surface
            (255, 100, 0),  # The color (orange-ish)
            (int(self.position.x), int(self.position.y)),  # Centroid coordinates
            self.radius,  # Radius of the bullet
            0  # Outline width (0 = filled circle)
            )
    def update(self, dt):
        self.position -= self.velocity * dt