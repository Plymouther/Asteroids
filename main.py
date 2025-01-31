import pygame
from gameover import *
from constants import *
from player import *
from circleshape import *
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    #Putting player in group instead of looping through Player itself in the loop
    pygame.init()
    pygame.font.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Initialize player 
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, shots)

    # Initialize the screen and clock
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0  # Time delta for frame-rate independent updates
    
    #initialize asteroidfield
    asteroid_field = AsteroidField()

    # Set up containers
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)

    # Puts player and asteroids in the the groups
    updatable.add(player, asteroid_field)
    drawable.add(player)
    game_over = GameOver()

    # Game loop
    run = True
    while run:
        screen.fill((0, 0, 0))  # Clear the screen with black

        # Draw and update player
        for sprite in updatable:
            sprite.update(dt)
        for sprite in drawable:
            sprite.draw(screen)

        for shot in shots:
            shot.update(dt)
            shot.draw(screen)

        pygame.display.flip()  # Update the display
       
       # Collission detector
        for asteroid in asteroids:
            if player.collision(asteroid) == True:
                game_over.show(screen)
                run = False

        for shot in shots:
            for asteroid in asteroids:
                if shot.collision(asteroid): 
                    asteroid.split()
                    shot.kill()
                

        # Handle quitting the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Calculate delta time for smooth movement  
        dt = clock.tick(60) / 1000  # 60 FPS, dt is in seconds


if __name__ == "__main__":
    main()