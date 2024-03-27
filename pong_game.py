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
        ball = Ball(DisplayConfig.WIDTH/2, DisplayConfig.HEIGHT/2)

        pygame.init()
        clock = pygame.time.Clock()
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        
            screen.fill(DisplayConfig.COLOR)
            player_1.draw(screen)
            player_2.draw(screen)
            ball.draw(screen)

            clock.tick(DisplayConfig.FPS)  # limits FPS to 60
            

            # FAZER A MOVIMENTAÇÃO DOS JOGADORES AGORA
            player_1.update()
            player_2.update()

            # flip() the display to put your work on screen
            # need att in the end of code! 
            pygame.display.flip()