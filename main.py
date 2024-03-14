import pygame
from config import Config

def main():
    config = Config(1280, 720)
    pygame.init()
    screen = pygame.display.set_mode((config.width, config.heigth))
    clock = pygame.time.Clock()
    running = True

    while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill('purple')

        clock.tick(60)  # limits FPS to 60

        pygame.draw.circle(screen, 'red', (config.x, config.y), (20))
        # pygame.quit()

        keys = pygame.key.get_pressed()

        # flip() the display to put your work on screen
        # need att in the end of code! 
        pygame.display.flip()

if __name__ == '__main__':
    main()