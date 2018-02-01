import pygame, random, time
from pygame.math import Vector2
from pygame.math import Vector3


class AppleManager:
    def __init__(self, game, interval):
        self.game = game
        self.apples = []
        self.timer = interval
        self.appleColor = Vector3(200, 30, 25)
        self.shadeColor = Vector3(130, 25, 20)
        self.highlightColor = Vector3(240, 50, 30)
        self.brown = Vector3(50, 25, 5)
        self.leafColor = Vector3(60, 100, 40)

        self.counter = 0

    def tick(self):
        # input
        pressed = pygame.key.get_pressed()
        if len(self.apples) == 0 or pressed[pygame.K_p] or self.counter == 100:
            self.apples.append(Apple(self))
            self.counter = 0

        self.counter += 1

    def draw(self):

        for i in range(len(self.apples) - 1, -1, -1):
            self.apples[i].draw()

    def drawShadow(self, shadowColor):

        for i in range(len(self.apples) - 1, -1, -1):
            self.apples[i].drawShadow(shadowColor)


class Apple(object):
    def __init__(self, manager):
        self.pos = Vector2(random.randint(2, 39) * 16, random.randint(2, 39) * 16)
        self.manager = manager

    def draw(self):
        ellipse = pygame.Rect(self.pos.x - 12, self.pos.y - 10, 20, 20)
        pygame.draw.ellipse(self.manager.game.screen, self.manager.shadeColor, ellipse)
        ellipse = pygame.Rect(self.pos.x - 8, self.pos.y - 10, 20, 20)
        pygame.draw.ellipse(self.manager.game.screen, self.manager.shadeColor, ellipse)

        ellipse = pygame.Rect(self.pos.x - 10, self.pos.y - 9, 18, 14)
        pygame.draw.ellipse(self.manager.game.screen, self.manager.appleColor, ellipse)
        ellipse = pygame.Rect(self.pos.x - 7, self.pos.y - 9, 18, 14)
        pygame.draw.ellipse(self.manager.game.screen, self.manager.appleColor, ellipse)

        ellipse = pygame.Rect(self.pos.x - 2, self.pos.y - 7, 6, 4)
        pygame.draw.ellipse(self.manager.game.screen, self.manager.shadeColor, ellipse)

        ellipse = pygame.Rect(self.pos.x + 4, self.pos.y - 5, 6, 4)
        pygame.draw.ellipse(self.manager.game.screen, self.manager.highlightColor, ellipse)

        ellipse = pygame.Rect(self.pos.x, self.pos.y - 11, 2, 7)
        pygame.draw.ellipse(self.manager.game.screen, self.manager.brown, ellipse)

        ellipse = pygame.Rect(self.pos.x, self.pos.y - 11, 7, 4)
        pygame.draw.ellipse(self.manager.game.screen, self.manager.leafColor, ellipse)

    def drawShadow(self, shadowColor):
        ellipse = pygame.Rect(self.pos.x - 16, self.pos.y - 6, 20, 20)
        pygame.draw.ellipse(self.manager.game.screen, shadowColor, ellipse)
        ellipse = pygame.Rect(self.pos.x - 12, self.pos.y - 6, 20, 20)
        pygame.draw.ellipse(self.manager.game.screen, shadowColor, ellipse)
