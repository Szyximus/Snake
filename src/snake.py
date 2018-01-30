import pygame, random, time
from pygame.math import Vector2
from pygame.math import Vector3

class Snake(object):

    def __init__(self, game):
        self.game = game
        size = self.game.screen.get_size() #zwraca krotke x, y
        self.pos = Vector2(size[0] / 2, size[1] / 2) # polozenie
        self.vel = 16 # predkosc pixels/frame
        self.width = size[0] #szerokosc siatki
        self.height = size[1] #wysokosc
        self.map = pygame.display.set_mode((self.width, self.height))
        self.length = 2
        self.ruch = Vector2(0, - self.vel)
        self.tail =[]
        self.tail.append(Segment(self, self.pos - self.ruch))
        self.tail.append(Segment(self, self.pos - 2 * self.ruch))

    def tick(self):
        # input
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_s] and self.ruch.y != -self.vel:
            self.ruch = Vector2(0, self.vel)

        if pressed[pygame.K_w] and self.ruch.y != self.vel:
            self.ruch = Vector2(0, - self.vel)

        if pressed[pygame.K_a] and self.ruch.x != self.vel:
            self.ruch = Vector2( - self.vel, 0)

        if pressed[pygame.K_d] and self.ruch.x != -self.vel:
            self.ruch = Vector2(self.vel, 0)

        if pressed[pygame.K_SPACE]:
            self.length += 1
            self.tail.append(Segment(self, self.tail[-1].pos - self.ruch))

        for i in range(self.length - 1 , 0, -1):
            self.tail[i].pos = self.tail[i - 1].pos

        self.tail[0].pos = self.pos + Vector2(0,0)
        self.pos += self.ruch

    def draw(self):

        self.tail[self.length - 1].drawLastShade(Vector3(40,80,15) )

        for i in range(self.length - 2, -1, -1):
            self.tail[i].drawShade(Vector3(40,80,15) / self.length, i)

        self.tail[self.length - 1].drawLastLight(Vector3(40,80,15) )

        for i in range(self.length - 2, -1, -1):
            self.tail[i].drawLight(Vector3(40,80,15) / self.length, i)

        ellipse = pygame.Rect(self.pos.x - 12 + self.ruch.x / 1.5, self.pos.y - 12 + self.ruch.y / 1.5, 24, 24)
        pygame.draw.ellipse(self.game.screen, (70, 150, 20), ellipse)

        ellipse = pygame.Rect(self.pos.x - 9 + self.ruch.x / 1.5, self.pos.y - 11 + self.ruch.y / 1.5, 20, 20)
        pygame.draw.ellipse(self.game.screen, (100, 200, 25), ellipse)

        ellipse = pygame.Rect(self.pos.x -16, self.pos.y - 16, 32, 32)
        pygame.draw.ellipse(self.game.screen, (70, 150, 20), ellipse)
        ellipse = pygame.Rect(self.pos.x - 13, self.pos.y - 15, 28, 28)
        pygame.draw.ellipse(self.game.screen, (100, 200, 25), ellipse)
        ellipse = pygame.Rect(self.pos.x - 5, self.pos.y - 9, 14, 14)
        pygame.draw.ellipse(self.game.screen, (125, 210, 27), ellipse)

        if self.ruch.y == -self.vel:
            ellipse = pygame.Rect(self.pos.x - 1, self.pos.y - 19, 12, 12)
            pygame.draw.ellipse(self.game.screen, (25, 75, 0), ellipse)

            ellipse = pygame.Rect(self.pos.x - 11, self.pos.y - 19, 12, 12)
            pygame.draw.ellipse(self.game.screen, (25, 75, 0), ellipse)

            ellipse = pygame.Rect(self.pos.x + 1, self.pos.y - 17, 8, 8)
            pygame.draw.ellipse(self.game.screen, (250, 240, 125), ellipse)

            ellipse = pygame.Rect(self.pos.x - 9, self.pos.y - 17, 8, 8)
            pygame.draw.ellipse(self.game.screen, (250, 240, 125), ellipse)

            ellipse = pygame.Rect(self.pos.x + 4, self.pos.y - 16, 3, 4)
            pygame.draw.ellipse(self.game.screen, (0, 0, 0), ellipse)

            ellipse = pygame.Rect(self.pos.x - 6, self.pos.y - 16, 3, 4)
            pygame.draw.ellipse(self.game.screen, (0, 0, 0), ellipse)

            ellipse = pygame.Rect(self.pos.x - 10, self.pos.y - 14, 20, 10)
            pygame.draw.ellipse(self.game.screen, (100, 200, 25), ellipse)

        if self.ruch.y == self.vel:
            ellipse = pygame.Rect(self.pos.x - 1, self.pos.y + 5, 12, 12)
            pygame.draw.ellipse(self.game.screen, (25, 75, 0), ellipse)

            ellipse = pygame.Rect(self.pos.x - 11, self.pos.y + 5, 12, 12)
            pygame.draw.ellipse(self.game.screen, (25, 75, 0), ellipse)

            ellipse = pygame.Rect(self.pos.x + 1, self.pos.y  + 7, 8, 8)
            pygame.draw.ellipse(self.game.screen, (250, 240, 125), ellipse)

            ellipse = pygame.Rect(self.pos.x - 9, self.pos.y + 7, 8, 8)
            pygame.draw.ellipse(self.game.screen, (250, 240, 125), ellipse)

            ellipse = pygame.Rect(self.pos.x + 4, self.pos.y + 9, 3, 4)
            pygame.draw.ellipse(self.game.screen, (0, 0, 0), ellipse)

            ellipse = pygame.Rect(self.pos.x - 6, self.pos.y + 9, 3, 4)
            pygame.draw.ellipse(self.game.screen, (0, 0, 0), ellipse)

        if self.ruch.x == self.vel:
            ellipse = pygame.Rect(self.pos.x + 8, self.pos.y - 11, 12, 12)
            pygame.draw.ellipse(self.game.screen, (25, 75, 0), ellipse)

            ellipse = pygame.Rect(self.pos.x + 8, self.pos.y - 3 , 12, 12)
            pygame.draw.ellipse(self.game.screen, (25, 75, 0), ellipse)

            ellipse = pygame.Rect(self.pos.x + 10, self.pos.y  - 10, 8, 8)
            pygame.draw.ellipse(self.game.screen, (250, 240, 125), ellipse)

            ellipse = pygame.Rect(self.pos.x + 10, self.pos.y  - 2, 8, 8)
            pygame.draw.ellipse(self.game.screen, (250, 240, 125), ellipse)

            ellipse = pygame.Rect(self.pos.x + 13, self.pos.y - 7, 4, 3)
            pygame.draw.ellipse(self.game.screen, (0, 0, 0), ellipse)

            ellipse = pygame.Rect(self.pos.x + 13, self.pos.y + 1, 4, 3)
            pygame.draw.ellipse(self.game.screen, (0, 0, 0), ellipse)

            ellipse = pygame.Rect(self.pos.x + 4, self.pos.y - 11, 8, 18)
            pygame.draw.ellipse(self.game.screen, (100, 200, 25), ellipse)

        if self.ruch.x == - self.vel:
            ellipse = pygame.Rect(self.pos.x - 18, self.pos.y - 11, 12, 12)
            pygame.draw.ellipse(self.game.screen, (25, 75, 0), ellipse)

            ellipse = pygame.Rect(self.pos.x -18, self.pos.y - 3 , 12, 12)
            pygame.draw.ellipse(self.game.screen, (25, 75, 0), ellipse)

            ellipse = pygame.Rect(self.pos.x - 16, self.pos.y  - 10, 8, 8)
            pygame.draw.ellipse(self.game.screen, (250, 240, 125), ellipse)

            ellipse = pygame.Rect(self.pos.x - 16, self.pos.y  - 2, 8, 8)
            pygame.draw.ellipse(self.game.screen, (250, 240, 125), ellipse)

            ellipse = pygame.Rect(self.pos.x - 15, self.pos.y - 7, 4, 3)
            pygame.draw.ellipse(self.game.screen, (0, 0, 0), ellipse)

            ellipse = pygame.Rect(self.pos.x - 15, self.pos.y + 1, 4, 3)
            pygame.draw.ellipse(self.game.screen, (0, 0, 0), ellipse)

            ellipse = pygame.Rect(self.pos.x - 10, self.pos.y - 11, 8, 18)
            pygame.draw.ellipse(self.game.screen, (100, 200, 25), ellipse)

    def drawShadow(self):


        for i in range(self.length - 1, -1, -1):
            self.tail[i].drawShadow()

        ellipse = pygame.Rect(self.pos.x - 16 + self.ruch.x / 1.5, self.pos.y - 8 + self.ruch.y / 1.5, 24, 24)
        pygame.draw.ellipse(self.game.screen, (35, 25, 15, 128), ellipse)

        ellipse = pygame.Rect(self.pos.x -20, self.pos.y - 12, 32, 32)
        pygame.draw.ellipse(self.game.screen, (35, 25, 15, 128), ellipse)






class Segment(object):

    def __init__(self, head, pos):
        self.pos = pos # polozenie
        self.head = head

    def drawShade(self, colour, i):
        ellipse = pygame.Rect(self.pos.x - 12, self.pos.y - 12, 24, 24)
        pygame.draw.ellipse(self.head.game.screen, (50, 120, 20) - colour * i, ellipse)

    def drawShadow(self):
        ellipse = pygame.Rect(self.pos.x - 15, self.pos.y - 9, 24, 24)
        pygame.draw.ellipse(self.head.game.screen, (35, 25, 15, 128), ellipse)

    def drawLight(self, colour, i):
        ellipse = pygame.Rect(self.pos.x - 9, self.pos.y - 11, 20, 20)
        pygame.draw.ellipse(self.head.game.screen, (100, 200, 25) - colour * i, ellipse)

    def drawLastShade(self, colour):
        ellipse = pygame.Rect(self.pos.x - 10, self.pos.y - 10, 20, 20)
        pygame.draw.ellipse(self.head.game.screen, (50, 120, 20) - colour, ellipse)

    def drawLastLight(self, colour):
        ellipse = pygame.Rect(self.pos.x - 8, self.pos.y - 8, 16, 16)
        pygame.draw.ellipse(self.head.game.screen, (100, 200, 25) - colour, ellipse)


