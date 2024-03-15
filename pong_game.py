import pygame
from display_config import DisplayConfig
from ball import Ball

class PongGame:
    
    def _load_items():
        ...

    @staticmethod
    def start():
        config = DisplayConfig(1280, 720, 'purple')
        screen = pygame.display.set_mode((config.width, config.heigth))
        ball = Ball(screen, 'black', [500, 500], 20)

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
            screen.fill(config.color)

            pygame.draw.circle(ball.surface, ball.color, ball.center, ball.radius)

            clock.tick(60)  # limits FPS to 60

            keys = pygame.key.get_pressed()

            # flip() the display to put your work on screen
            # need att in the end of code! 
            pygame.display.flip()