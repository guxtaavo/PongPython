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
        config = DisplayConfig(1280, 720, 'purple')
        screen = pygame.display.set_mode((config.width, config.heigth))
        ball = Ball(screen, 'black', [500, 500], 20)
        rect_1 = pygame.Rect((config.width - config.width + 30), (config.heigth/2 + 10), 4, 15)
        rect_2 = pygame.Rect((config.width - 30), (config.heigth/2 + 10), 4, 15)
        player_1 = Player1(rect_1)
        player_2 = Player2(rect_2)

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
            pygame.draw.rect(screen, 'black', player_1.rect)
            pygame.draw.rect(screen, 'white', player_2.rect)

            clock.tick(60)  # limits FPS to 60

            keys = pygame.key.get_pressed()

            # flip() the display to put your work on screen
            # need att in the end of code! 
            pygame.display.flip()