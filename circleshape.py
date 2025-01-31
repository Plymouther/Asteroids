import pygame

# CircleShape class is a base class for circular objects, providing basic position and radius
class CircleShape(pygame.sprite.Sprite):
    
    def __init__(self, x, y, radius):
        super().__init__()  # Initialize sprite
        self.position = pygame.Vector2(x, y)
        self.radius = radius


    def collision(self, other):
        distance = pygame.math.Vector2.distance_to(self.position, other.position)
        if distance <= self.radius + other.radius:
            return True
        else:
            return False
        

    # Placeholder draw method (not used here directly)
    def draw(self, screen):
        pass

    # Placeholder update method (to be overridden by subclasses)
    def update(self, dt):
        pass

    def update(self, dt):
        pass