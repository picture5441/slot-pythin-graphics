from machine import Machine
from settings import *
import pygame, sys


class Game:
    def __init__(self):
        
        # General setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Slot Machine')
        self.clock = pygame.time.Clock()
        self.bg_image = pygame.image.load(BG_IMAGE_PATH)
        self.grid_image = pygame.image.load(GRID_IMAGE_PATH)

        # TO DO: Create machine class
        self.machine = Machine()
        self.delta_time = 0

        # Sound
        main_sound = pygame.mixer.Sound('audio/yo.mp3')
        main_sound.set_volume(0.1)
        main_sound.play(loops = -1) # To play again and again

    def run(self):


        self.start_time = pygame.time.get_ticks()

        while True:
            # Handle quit operation
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Time vars
            self.delta_time = (pygame.time.get_ticks() - self.start_time) / 1000
            self.start_time = pygame.time.get_ticks()

            pygame.display.update()
            self.screen.blits([(self.bg_image, (0, 0)),(self.grid_image, (540, 270))])
            self.machine.update(self.delta_time)
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()