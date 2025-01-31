import pygame

# GameOver class that handles displaying the Game Over screen
class GameOver:
    def __init__(self):
        # Initialize the font and render text for Game Over and instructions
        pygame.font.init()
        self.font = pygame.font.SysFont(None, 55)
        self.game_over_text = self.font.render('Game Over!', True, (255, 0, 0))  # Red color
        self.quit_text = self.font.render('Press Space to Quit', True, (255, 255, 255))  # White color

    def show(self, screen):
        # Calculate the position to center the text on the screen
        game_over_rect = self.game_over_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
        quit_rect = self.quit_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 60))

        # Blit the text onto the screen
        screen.blit(self.game_over_text, game_over_rect)
        screen.blit(self.quit_text, quit_rect)

        # Update the display to show the text
        pygame.display.flip()

        # Wait for the player to press space to continue
        waiting_for_input = True
        while waiting_for_input:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    waiting_for_input = False  # Exit the loop if space is pressed
