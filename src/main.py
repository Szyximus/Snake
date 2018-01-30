import pygame, sys ,os, random
from src.snake import Snake
from src.appleManager import AppleManager


shadowColor = pygame.math.Vector3(40,30,15)
class Game(object):

    def __init__(self):
        self.tps_max = 4.0

        # initialization
        pygame.init()
        self.screen = pygame.display.set_mode((640, 640))
        self.tps_clock = pygame.time.Clock()
        self.tps_delta = 0.0

        pygame.display.set_caption('Snake')

        self.background = pygame.image.load('./graphics/background.png')
        self.shadowmap = pygame.Surface((640, 640))
        self.shadowmap.set_alpha(128)

        self.player = Snake(self)
        self.apples = AppleManager(self, 10)

        while True:
            # handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
            # ticking
            self.tps_delta += self.tps_clock.tick() / 1000.0
            while self.tps_delta > 1 / self.tps_max:
                self.tick()
                self.tps_delta -= 1 / self.tps_max

            # drawing
            self.screen.fill((0, 0, 0))  # czyszczenie ekranu, aby obiekt przesuwal sie ze zniknieciem sladu
            self.draw()

            pygame.display.flip() # obracanie obrazu

    def tick(self): # to co ma sie wykonywac z zadana czestotliwoscia
        self.player.tick()
        self.apples.tick()

    def draw(self): # to co ma sie wykonywac najszybciej jak sie da
        self.screen.blit(self.background,(0,0))
        self.apples.drawShadow(shadowColor)
        self.player.drawShadow(shadowColor)
        self.player.draw()
        self.apples.draw()

if __name__ == "__main__":
    Game()





