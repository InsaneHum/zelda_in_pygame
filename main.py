import pygame, sys
from settings import *


class Game:
    def __init__(self):

        # general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()

    def run(self):
        # event loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # update the screen
            self.screen.fill('black')
            pygame.display.update()
            self.clock.tick(FPS)  # FPS determines how many times the game updates itself


if __name__ == '__main__':
    game = Game()
    game.run()