import pygame, random, time
from pygame.math import Vector2
from pygame.math import Vector3

class AppleManager:

    def __init__(self, game, interval):
        self.game = game
        self.apples = []
        self.timer = interval

    def tick(self):
        # input
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_p]:
            self.apples.append(Apple(self))


    def draw(self):

        for i in range(len(self.apples) - 1, -1, -1):
            self.apples[i].draw()

    def drawShadow(self):

        for i in range(len(self.apples) - 1, -1, -1):
            self.apples[i].drawShadow()

class Apple(object):

    def __init__(self, manager):
        self.pos = Vector2(random.randint(2,39) * 16, random.randint(2,39) * 16)
        self.manager = manager

    def draw(self):
        ellipse = pygame.Rect(self.pos.x - 12, self.pos.y - 10, 20, 20)
        pygame.draw.ellipse(self.manager.game.screen, (100, 0, 0), ellipse)
        ellipse = pygame.Rect(self.pos.x - 8, self.pos.y - 10, 20, 20)
        pygame.draw.ellipse(self.manager.game.screen, (100, 0, 0), ellipse)

        ellipse = pygame.Rect(self.pos.x - 10, self.pos.y - 9, 18, 14)
        pygame.draw.ellipse(self.manager.game.screen, (150, 0, 0), ellipse)
        ellipse = pygame.Rect(self.pos.x - 7, self.pos.y - 9, 18, 14)
        pygame.draw.ellipse(self.manager.game.screen, (150, 0, 0), ellipse)

        ellipse = pygame.Rect(self.pos.x - 2, self.pos.y - 7, 6, 4)
        pygame.draw.ellipse(self.manager.game.screen, (100, 0, 0), ellipse)

        ellipse = pygame.Rect(self.pos.x + 4, self.pos.y - 5, 6, 4)
        pygame.draw.ellipse(self.manager.game.screen, (200, 25, 10), ellipse)

        ellipse = pygame.Rect(self.pos.x , self.pos.y - 10, 2, 6)
        pygame.draw.ellipse(self.manager.game.screen, (50, 25, 5), ellipse)

    def drawShadow(self):
        ellipse = pygame.Rect(self.pos.x - 16, self.pos.y - 6, 20, 20)
        pygame.draw.ellipse(self.manager.game.screen, (35, 25, 15), ellipse)
        ellipse = pygame.Rect(self.pos.x - 12, self.pos.y - 6, 20, 20)
        pygame.draw.ellipse(self.manager.game.screen, (35, 25, 15), ellipse)
