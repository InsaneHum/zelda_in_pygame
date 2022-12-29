import pygame
import sys

from settings import *
# from debug import debug


class Game:
    def __init__(self):

        # general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()

        # set window title and icon
        pygame.display.set_caption('Zelda?')
        ICON = pygame.image.load('img/icon.jpg')
        pygame.display.set_icon(ICON)
        
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
