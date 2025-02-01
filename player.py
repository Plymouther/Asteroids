import pygame
from circleshape import CircleShape
from constants import *
from shot import *
import time

class Player(CircleShape):

    def __init__(self, x, y, shots_group):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0  # Initial rotation angle
        self.shots_group = shots_group
        self.velocity = pygame.Vector2(0, 0)  # Initial velocity
        self.last_shot_time = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        triangle_points = self.triangle()
        pygame.draw.polygon(screen, "white", triangle_points, 2)

    def rotate(self, dt, direction):
        self.rotation += direction * PLAYER_TURN_SPEED * dt

    def accelerate(self, dt, direction):
        forward = pygame.Vector2(0, 1).rotate(self.rotation) * direction
        self.velocity += forward * PLAYER_SPEED * dt

    def apply_friction(self, dt):
        self.velocity *= 1 - (PLAYER_FRICTION * dt)  # Slow down over time

    def move(self, dt):
        self.position += self.velocity * dt

    def shoot(self):
        current_time = time.time()
        if current_time - self.last_shot_time >= 0.35:  #Shot Cd cooldown
            new_shot = Shot(self.position.x, self.position.y)
            new_shot.velocity = pygame.Vector2(0, -1)
            new_shot.velocity.rotate_ip(self.rotation)
            new_shot.velocity *= PLAYER_SHOOT_SPEED
            self.shots_group.add(new_shot)
            self.last_shot_time = current_time  # Update last shot time

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:  # Rotate left
            self.rotate(dt, -1)
        if keys[pygame.K_d]:  # Rotate right
            self.rotate(dt, 1)
        if keys[pygame.K_w]:  # Accelerate forward
            self.accelerate(dt, 1)
        if keys[pygame.K_s]:  # Accelerate backward
            self.accelerate(dt, -0.5)  # Reverse at half speed
        if keys[pygame.K_SPACE]:  # Shoot
            self.shoot()

        self.apply_friction(dt)  # Apply friction to slow down
        self.move(dt)  # Update position based on velocity
