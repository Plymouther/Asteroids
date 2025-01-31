import pygame
from circleshape import CircleShape
from constants import *
from shot import *

# Player class inherits from CircleShape, adding rotation and movement logic
class Player(CircleShape):

    def __init__(self, x, y, shots_group):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0  # Initial rotation angle
        self.shots_group = shots_group 

    # Calculates the points for the player's triangle shape based on rotation
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]  # Return triangle points

    # Draws the player triangle on the screen
    def draw(self, screen):
        triangle_points = self.triangle()  # Get triangle points
        pygame.draw.polygon(screen, "white", triangle_points, 2)  # Draw triangle

    # Rotates the player by a specified amount
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    # Moves the player forward or backward based on the direction
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        print("Shoot method called!")  # Debug print
        new_shot = Shot(self.position.x, self.position.y)
        print(f"Shot created at position: {self.position}")  # Debug print
        new_shot.velocity = pygame.Vector2(0, -1)
        new_shot.velocity.rotate_ip(self.rotation)
        new_shot.velocity *= PLAYER_SHOOT_SPEED
        print(f"Shot velocity: {new_shot.velocity}")  # Debug print
        self.shots_group.add(new_shot)
        print(f"Shot added to group. Group size: {len(self.shots_group)}")  # Debug print



    # Updates player state based on input (rotation and movement)
    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:  # Rotate left
            self.rotate(-dt)
        if keys[pygame.K_d]:  # Rotate right
            self.rotate(dt)
        if keys[pygame.K_w]:  # Move forward
            self.move(dt)
        if keys[pygame.K_s]:  # Move backward
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
