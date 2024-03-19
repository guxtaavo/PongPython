import pygame
from display_config import DisplayConfig
from ball import Ball
from player_1 import Player1
from player_2 import Player2

class PongGame:
    
    def _load_items():
        ...

    @staticmethod
    def start():
        screen = pygame.display.set_mode((DisplayConfig.WIDTH, DisplayConfig.HEIGHT))
        player_1 = Player1(DisplayConfig.WIDTH - DisplayConfig.WIDTH + 20, DisplayConfig.HEIGHT/2)
        player_2 = Player2(DisplayConfig.WIDTH - 25, DisplayConfig.HEIGHT/2)

        pygame.init()
        clock = pygame.time.Clock()
        running = True

        while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # fill the screen with a color to wipe away anything from last frame
            screen.fill(DisplayConfig.COLOR)
            player_1.draw(screen)
            player_2.draw(screen)

            clock.tick(60)  # limits FPS to 60

            # player_1.update()
            # player_2.update()

            # flip() the display to put your work on screen
            # need att in the end of code! 
            pygame.display.flip()