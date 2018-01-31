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
        self.length = 3
        self.ruch = Vector2(0, - self.vel)
        self.tail =[]
        self.tail.append(Segment(self, self.pos - self.ruch))
        self.tail.append(Segment(self, self.pos - 2 * self.ruch))
        self.tail.append(Segment(self, self.pos - 3 * self.ruch))

        self.subtractColor = Vector3(30,70,10)
        self.shadeColor = Vector3(80, 120, 20)
        self.snakeColor = Vector3(120, 180, 25)
        self.highlightColor = Vector3(150, 190, 30)
        self.eyesColor = Vector3(255, 250, 125)
        self.eyeShadeColor = Vector3(30, 60, 5)
        self.black = Vector3(0, 0, 0)
        self.white = Vector3(255, 255, 255)

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

        for i in range(self.length - 1 , 0, -1):
            self.tail[i].pos = self.tail[i - 1].pos

        self.tail[0].pos = self.pos + Vector2(0,0)
        self.pos += self.ruch

        for apple in self.game.apples.apples:
            if self.pos + self.ruch == apple.pos or self.pos == apple.pos:
                self.eatApple(apple)

        for segment in self.tail:
            if self.pos == segment.pos:
                self.die()

        if self.pos.x == 0 or self.pos.y == 0 or self.pos.x == self.width or self.pos.y == self.height:
            self.die()

    def die(self):

        self.game.sounds.deathSound.play()
        if random.randint(0,5) == 5:
            self.game.sounds.deathSound2.play()

        size = self.game.screen.get_size()  # zwraca krotke x, y
        self.pos = Vector2(size[0] / 2, size[1] / 2)  # polozenie
        self.vel = 16 # predkosc pixels/frame

        self.length = 3
        self.ruch = Vector2(0, - self.vel)
        self.tail = []
        self.tail.append(Segment(self, self.pos - self.ruch))
        self.tail.append(Segment(self, self.pos - 2 * self.ruch))
        self.tail.append(Segment(self, self.pos - 3 * self.ruch))

        self.game.apples.apples = []
        self.game.apples.counter = 0

        pygame.time.wait(250)

    def eatApple(self, apple):

        self.game.sounds.eatSound.play()
        self.length += 1
        self.tail.append(Segment(self, self.tail[-1].pos))
        self.game.apples.apples.remove(apple)

        pygame.time.wait(100)

    def draw(self):

        self.tail[self.length - 1].drawLastShade(self.subtractColor)

        for i in range(self.length - 2, -1, -1):
            self.tail[i].drawShade(self.subtractColor / self.length, i)

        self.tail[self.length - 1].drawLastLight(self.subtractColor)

        for i in range(self.length - 2, -1, -1):
            self.tail[i].drawLight(self.subtractColor / self.length, i)

        ellipse = pygame.Rect(self.pos.x - 12 + self.ruch.x / 1.5, self.pos.y - 12 + self.ruch.y / 1.5, 24, 24)
        pygame.draw.ellipse(self.game.screen, self.shadeColor, ellipse)

        ellipse = pygame.Rect(self.pos.x - 9 + self.ruch.x / 1.5, self.pos.y - 11 + self.ruch.y / 1.5, 20, 20)
        pygame.draw.ellipse(self.game.screen, self.snakeColor, ellipse)

        ellipse = pygame.Rect(self.pos.x -16, self.pos.y - 16, 32, 32)
        pygame.draw.ellipse(self.game.screen, self.shadeColor, ellipse)
        ellipse = pygame.Rect(self.pos.x - 13, self.pos.y - 15, 28, 28)
        pygame.draw.ellipse(self.game.screen, self.snakeColor, ellipse)


        if self.ruch.y == -self.vel:
            ellipse = pygame.Rect(self.pos.x - 1, self.pos.y - 19, 12, 12)
            pygame.draw.ellipse(self.game.screen, self.eyeShadeColor, ellipse)

            ellipse = pygame.Rect(self.pos.x - 11, self.pos.y - 19, 12, 12)
            pygame.draw.ellipse(self.game.screen, self.eyeShadeColor, ellipse)

            ellipse = pygame.Rect(self.pos.x + 1, self.pos.y - 17, 8, 8)
            pygame.draw.ellipse(self.game.screen, self.eyesColor, ellipse)

            ellipse = pygame.Rect(self.pos.x - 9, self.pos.y - 17, 8, 8)
            pygame.draw.ellipse(self.game.screen, self.eyesColor, ellipse)

            ellipse = pygame.Rect(self.pos.x + 3, self.pos.y - 16, 4, 6)
            pygame.draw.ellipse(self.game.screen, self.black, ellipse)

            ellipse = pygame.Rect(self.pos.x - 7, self.pos.y - 16, 4, 6)
            pygame.draw.ellipse(self.game.screen, self.black, ellipse)

            ellipse = pygame.Rect(self.pos.x - 10, self.pos.y - 14, 20, 10)
            pygame.draw.ellipse(self.game.screen, self.snakeColor, ellipse)

        if self.ruch.y == self.vel:
            ellipse = pygame.Rect(self.pos.x - 1, self.pos.y + 5, 12, 12)
            pygame.draw.ellipse(self.game.screen, self.eyeShadeColor, ellipse)

            ellipse = pygame.Rect(self.pos.x - 11, self.pos.y + 5, 12, 12)
            pygame.draw.ellipse(self.game.screen, self.eyeShadeColor, ellipse)

            ellipse = pygame.Rect(self.pos.x + 1, self.pos.y  + 7, 8, 8)
            pygame.draw.ellipse(self.game.screen, self.eyesColor, ellipse)

            ellipse = pygame.Rect(self.pos.x - 9, self.pos.y + 7, 8, 8)
            pygame.draw.ellipse(self.game.screen, self.eyesColor, ellipse)

            ellipse = pygame.Rect(self.pos.x + 3, self.pos.y + 8, 4, 6)
            pygame.draw.ellipse(self.game.screen, self.black, ellipse)

            ellipse = pygame.Rect(self.pos.x - 7, self.pos.y + 8, 4, 6)
            pygame.draw.ellipse(self.game.screen, self.black, ellipse)

            ellipse = pygame.Rect(self.pos.x - 4, self.pos.y + 8, 2, 2)
            pygame.draw.ellipse(self.game.screen, self.white, ellipse)

            ellipse = pygame.Rect(self.pos.x + 6, self.pos.y + 8, 2, 2)
            pygame.draw.ellipse(self.game.screen, self.white, ellipse)

        if self.ruch.x == self.vel:
            ellipse = pygame.Rect(self.pos.x + 8, self.pos.y - 11, 12, 12)
            pygame.draw.ellipse(self.game.screen, self.eyeShadeColor, ellipse)

            ellipse = pygame.Rect(self.pos.x + 8, self.pos.y - 3 , 12, 12)
            pygame.draw.ellipse(self.game.screen, self.eyeShadeColor, ellipse)

            ellipse = pygame.Rect(self.pos.x + 10, self.pos.y - 10, 8, 8)
            pygame.draw.ellipse(self.game.screen, self.eyesColor, ellipse)

            ellipse = pygame.Rect(self.pos.x + 10, self.pos.y - 2, 8, 8)
            pygame.draw.ellipse(self.game.screen, self.eyesColor, ellipse)

            ellipse = pygame.Rect(self.pos.x + 11, self.pos.y - 8, 6, 4)
            pygame.draw.ellipse(self.game.screen, self.black, ellipse)

            ellipse = pygame.Rect(self.pos.x + 11, self.pos.y , 6, 4)
            pygame.draw.ellipse(self.game.screen, self.black, ellipse)

            ellipse = pygame.Rect(self.pos.x + 4, self.pos.y - 11, 8, 18)
            pygame.draw.ellipse(self.game.screen, self.snakeColor, ellipse)

        if self.ruch.x == - self.vel:
            ellipse = pygame.Rect(self.pos.x - 18, self.pos.y - 11, 12, 12)
            pygame.draw.ellipse(self.game.screen, self.eyeShadeColor, ellipse)

            ellipse = pygame.Rect(self.pos.x -18, self.pos.y - 3 , 12, 12)
            pygame.draw.ellipse(self.game.screen, self.eyeShadeColor, ellipse)

            ellipse = pygame.Rect(self.pos.x - 16, self.pos.y  - 10, 8, 8)
            pygame.draw.ellipse(self.game.screen, self.eyesColor, ellipse)

            ellipse = pygame.Rect(self.pos.x - 16, self.pos.y  - 2, 8, 8)
            pygame.draw.ellipse(self.game.screen, self.eyesColor, ellipse)

            ellipse = pygame.Rect(self.pos.x - 15, self.pos.y - 8, 6, 4)
            pygame.draw.ellipse(self.game.screen, self.black, ellipse)

            ellipse = pygame.Rect(self.pos.x - 15, self.pos.y , 6, 4)
            pygame.draw.ellipse(self.game.screen, self.black, ellipse)

            ellipse = pygame.Rect(self.pos.x - 10, self.pos.y - 11, 8, 18)
            pygame.draw.ellipse(self.game.screen, self.snakeColor, ellipse)

        ellipse = pygame.Rect(self.pos.x - 5, self.pos.y - 9, 14, 14)
        pygame.draw.ellipse(self.game.screen, self.highlightColor, ellipse)

    def drawShadow(self,shadowColor):


        for i in range(self.length - 1, -1, -1):
            self.tail[i].drawShadow(shadowColor)

        ellipse = pygame.Rect(self.pos.x - 16 + self.ruch.x / 1.5, self.pos.y - 8 + self.ruch.y / 1.5, 24, 24)
        pygame.draw.ellipse(self.game.screen, shadowColor, ellipse)

        ellipse = pygame.Rect(self.pos.x -20, self.pos.y - 12, 32, 32)
        pygame.draw.ellipse(self.game.screen, shadowColor, ellipse)






class Segment(object):

    def __init__(self, head, pos):
        self.pos = pos # polozenie
        self.head = head

    def drawShade(self, colour, i):
        ellipse = pygame.Rect(self.pos.x - 12, self.pos.y - 12, 24, 24)
        pygame.draw.ellipse(self.head.game.screen, self.head.shadeColor - colour * i, ellipse)

    def drawShadow(self,shadowColor):
        ellipse = pygame.Rect(self.pos.x - 15, self.pos.y - 9, 24, 24)
        pygame.draw.ellipse(self.head.game.screen, shadowColor, ellipse)

    def drawLight(self, colour, i):
        ellipse = pygame.Rect(self.pos.x - 9, self.pos.y - 11, 20, 20)
        pygame.draw.ellipse(self.head.game.screen, self.head.snakeColor - colour * i, ellipse)

    def drawLastShade(self, colour):
        ellipse = pygame.Rect(self.pos.x - 10, self.pos.y - 10, 20, 20)
        pygame.draw.ellipse(self.head.game.screen, self.head.shadeColor - colour, ellipse)

    def drawLastLight(self, colour):
        ellipse = pygame.Rect(self.pos.x - 8, self.pos.y - 8, 16, 16)
        pygame.draw.ellipse(self.head.game.screen, self.head.snakeColor - colour, ellipse)


