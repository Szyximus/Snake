import pygame, sys, os, random
from snake import Snake
from appleManager import AppleManager
from soundManager import SoundManager
from pygame.math import Vector2
from math import sin
from math import cos


class Game(object):
    def __init__(self):
        self.tps_max = 5.0
        self.base_tps = 5.0
        self.tps_pause = 60.0

        # initialization
        pygame.init()
        self.screen = pygame.display.set_mode((640, 640))
        self.tps_clock = pygame.time.Clock()
        self.tps_delta = 0.0

        self.sounds = SoundManager(self)

        dir = os.path.dirname(__file__)

        self.smallFont = pygame.font.Font(os.path.join(dir, "../graphics/German Beauty.ttf"), 18)
        self.largeFont = pygame.font.Font(os.path.join(dir, "../graphics/German Beauty.ttf"), 128)
        self.mediumFont = pygame.font.Font(os.path.join(dir, "../graphics/German Beauty.ttf"), 32)

        pygame.display.set_caption('Snake!')

        self.label = Label(self)

        self.background = pygame.image.load(os.path.join('../graphics/background.png'))
        self.shadowColor = pygame.math.Vector3(40, 30, 15)

        self.player = Snake(self)
        self.apples = AppleManager(self, 10)
        self.pause = Pause(self)
        self.deathScreen = DeathScreen(self)

        while True:

            while self.pause.isPause:
                # handle events
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit(0)
                # ticking
                self.tps_delta += self.tps_clock.tick() / 1000.0
                while self.tps_delta > 1 / self.tps_pause:
                    self.pause.tick()
                    self.tps_delta -= 1 / self.tps_pause

                # drawing
                # self.screen.fill((0, 0, 0))  # czyszczenie ekranu, aby obiekt przesuwal sie ze zniknieciem sladu
                self.pause.draw()

                pygame.display.flip()  # obracanie obrazu

            while self.deathScreen.isDead:
                # handle events
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit(0)
                # ticking
                self.tps_delta += self.tps_clock.tick() / 1000.0
                while self.tps_delta > 1 / self.tps_pause:
                    self.deathScreen.tick()
                    self.tps_delta -= 1 / self.tps_pause

                # drawing
                # self.screen.fill((0, 0, 0))  # czyszczenie ekranu, aby obiekt przesuwal sie ze zniknieciem sladu
                self.deathScreen.draw()

                pygame.display.flip()  # obracanie obrazu

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

            pygame.display.flip()  # obracanie obrazu

    def tick(self):  # to co ma sie wykonywac z zadana czestotliwoscia

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_ESCAPE] and self.pause.isPause == False:
            self.pause.isPause = True
            self.sounds.ambient.fadeout(2000)
            pygame.mixer.music.set_volume(1)

        if pressed[pygame.K_SPACE]:
            self.tps_max = (self.base_tps + (self.player.length - 3) / 4) * 2
            self.sounds.boostSound.play()
        else:
            self.tps_max = self.base_tps + (self.player.length - 3) / 4

        self.player.tick()
        self.apples.tick()
        self.label.tick(self.player.length - 3)

    def draw(self):  # to co ma sie wykonywac najszybciej jak sie da
        self.screen.blit(self.background, (0, 0))
        self.apples.drawShadow(self.shadowColor)
        self.player.drawShadow(self.shadowColor)
        self.player.draw()
        self.apples.draw()
        self.label.draw()


class Label:
    def __init__(self, game):
        self.font = game.smallFont
        self.wynik_napis = self.font.render('SCORE: %s' % 0, True, (255, 250, 125))
        self.wynik_pole = self.wynik_napis.get_rect()
        self.wynik_pole.topleft = (640 - 112, 12)

        self.shadow_napis = self.font.render('SCORE: %s' % 0, True, (0, 0, 0))
        self.shadow_pole = self.wynik_napis.get_rect()
        self.shadow_pole.topleft = (640 - 114, 14)

        self.game = game

    def tick(self, wynik):
        self.wynik_napis = self.font.render('SCORE: %s' % (wynik), True, (255, 250, 125))
        self.shadow_napis = self.font.render('SCORE: %s' % (wynik), True, (0, 0, 0))

    def draw(self):
        self.game.screen.blit(self.shadow_napis, self.shadow_pole)
        self.game.screen.blit(self.wynik_napis, self.wynik_pole)


class Pause:
    def __init__(self, game):

        self.isPause = True
        self.font = game.largeFont
        self.smallFont = game.smallFont
        self.mediumFont = game.mediumFont

        self.title_napis = self.font.render('Snake!', True, (255, 250, 125))
        self.title_pole = self.title_napis.get_rect()
        self.title_pole.topleft = (154, 64)

        self.shadow_napis = self.font.render('Snake!', True, (0, 0, 0))
        self.shadow_pole = self.title_napis.get_rect()
        self.shadow_pole.topleft = (156, 66)
        self.game = game

        self.controls_napis = self.mediumFont.render('Controls:', True, (255, 255, 255))
        self.controls_pole = self.title_napis.get_rect()
        self.controls_pole.topleft = (248, 224)

        self.controls_shadow = self.mediumFont.render('Controls:', True, (0, 0, 0))
        self.controls_shadow_pole = self.title_napis.get_rect()
        self.controls_shadow_pole.topleft = (246, 226)

        self.w_napis = self.smallFont.render('W - Move Up', True, (255, 255, 255))
        self.w_pole = self.title_napis.get_rect()
        self.w_pole.topleft = (266, 274)

        self.w_shadow = self.smallFont.render('W - Move Up', True, (0, 0, 0))
        self.w_shadow_pole = self.title_napis.get_rect()
        self.w_shadow_pole.topleft = (264, 276)

        self.s_napis = self.smallFont.render('S - Move Down', True, (255, 255, 255))
        self.s_pole = self.title_napis.get_rect()
        self.s_pole.topleft = (258, 304)

        self.s_shadow = self.smallFont.render('S - Move Down', True, (0, 0, 0))
        self.s_shadow_pole = self.title_napis.get_rect()
        self.s_shadow_pole.topleft = (256, 306)

        self.a_napis = self.smallFont.render('A - Move Left', True, (255, 255, 255))
        self.a_pole = self.title_napis.get_rect()
        self.a_pole.topleft = (260, 334)

        self.a_shadow = self.smallFont.render('A - Move Left', True, (0, 0, 0))
        self.a_shadow_pole = self.title_napis.get_rect()
        self.a_shadow_pole.topleft = (258, 336)

        self.d_napis = self.smallFont.render('D - Move Right', True, (255, 255, 255))
        self.d_pole = self.title_napis.get_rect()
        self.d_pole.topleft = (254, 364)

        self.d_shadow = self.smallFont.render('D - Move Right', True, (0, 0, 0))
        self.d_shadow_pole = self.title_napis.get_rect()
        self.d_shadow_pole.topleft = (252, 366)

        self.space_napis = self.smallFont.render('SPACE - Boost', True, (255, 255, 255))
        self.space_pole = self.title_napis.get_rect()
        self.space_pole.topleft = (252, 394)

        self.space_shadow = self.smallFont.render('SPACE - Boost', True, (0, 0, 0))
        self.space_shadow_pole = self.title_napis.get_rect()
        self.space_shadow_pole.topleft = (250, 396)

        self.e_napis = self.smallFont.render('ESC - Pause', True, (255, 255, 255))
        self.e_pole = self.title_napis.get_rect()
        self.e_pole.topleft = (264, 424)

        self.e_shadow = self.smallFont.render('ESC - Pause', True, (0, 0, 0))
        self.e_shadow_pole = self.title_napis.get_rect()
        self.e_shadow_pole.topleft = (262, 426)

        self.play_napis = self.mediumFont.render('Press SPACE to Play!', True, (255, 255, 255))
        self.play_pole = self.title_napis.get_rect()
        self.play_pole.topleft = (170, 474)

        self.play_shadow = self.mediumFont.render('Press SPACE to Play!', True, (0, 0, 0))
        self.play_shadow_pole = self.title_napis.get_rect()
        self.play_shadow_pole.topleft = (168, 476)

        self.c_napis = self.smallFont.render('Made by Szymon  Jakóbczyk', True, (255, 255, 255))
        self.c_pole = self.title_napis.get_rect()
        self.c_pole.topleft = (406, 602)

        self.c_shadow = self.smallFont.render('Made by Szymon  Jakóbczyk', True, (0, 0, 0))
        self.c_shadow_pole = self.title_napis.get_rect()
        self.c_shadow_pole.topleft = (404, 604)

        self.counter = 1.0
        self.counter1 = 0

        self.vec = Vector2(0, 0)
        self.vec1 = Vector2(0, 0)

    def tick(self):

        self.vec = Vector2(sin(self.counter / 8) * 32, sin(self.counter / 12) * 18)

        self.vec1 = Vector2(0, max(540 - self.counter1, 0))

        self.title_pole.topleft = (144 + self.vec.x, 54 + self.vec.y + self.vec1.y)
        self.shadow_pole.topleft = (140 + self.vec.x, 57 + self.vec.y + self.vec1.y)

        self.play_pole.topleft = (170 + self.vec.x / 6, 474 + self.vec.y / 8)
        self.play_shadow_pole.topleft = (168 + self.vec.x / 6, 476 + self.vec.y / 8)

        self.counter += 0.1
        self.counter1 += 1

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE]:
            self.isPause = False
            self.game.sounds.ambient.play(-1, 0, 5000)
            pygame.mixer.music.set_volume(0.05)

    def draw(self):
        self.game.screen.blit(self.game.background, (0, 0))

        if max(585 - self.counter1, 0) == 0:
            self.game.screen.blit(self.controls_shadow, self.controls_shadow_pole)
            self.game.screen.blit(self.w_shadow, self.w_shadow_pole)
            self.game.screen.blit(self.s_shadow, self.s_shadow_pole)
            self.game.screen.blit(self.a_shadow, self.a_shadow_pole)
            self.game.screen.blit(self.d_shadow, self.d_shadow_pole)
            self.game.screen.blit(self.e_shadow, self.e_shadow_pole)
            self.game.screen.blit(self.space_shadow, self.space_shadow_pole)
            self.game.screen.blit(self.play_shadow, self.play_shadow_pole)
            self.game.screen.blit(self.c_shadow, self.c_shadow_pole)

            self.game.screen.blit(self.controls_napis, self.controls_pole)
            self.game.screen.blit(self.w_napis, self.w_pole)
            self.game.screen.blit(self.s_napis, self.s_pole)
            self.game.screen.blit(self.a_napis, self.a_pole)
            self.game.screen.blit(self.d_napis, self.d_pole)
            self.game.screen.blit(self.e_napis, self.e_pole)
            self.game.screen.blit(self.space_napis, self.space_pole)
            self.game.screen.blit(self.play_napis, self.play_pole)
            self.game.screen.blit(self.c_napis, self.c_pole)

        self.game.screen.blit(self.shadow_napis, self.shadow_pole)
        self.game.screen.blit(self.title_napis, self.title_pole)


class DeathScreen:
    def __init__(self, game):
        self.game = game

        self.isDead = False
        self.font = self.game.largeFont
        self.mediumFont = self.game.mediumFont
        self.score = self.game.player.length - 3

        self.score1_napis = self.mediumFont.render('SCORE:', True, (255, 255, 255))
        self.score1_pole = self.score1_napis.get_rect()
        self.score1_pole.topleft = (260, 144)

        self.score1_shadow = self.mediumFont.render('SCORE', True, (0, 0, 0))
        self.score1_shadow_pole = self.score1_napis.get_rect()
        self.score1_shadow_pole.topleft = (258, 146)

        self.score_napis = self.font.render('%s' % (self.score), True, (255, 250, 125))
        self.score_pole = self.score_napis.get_rect()
        self.score_pole.topleft = (262, 224)

        self.shadow_napis = self.font.render('%s' % (self.score), True, (0, 0, 0))
        self.shadow_pole = self.score_napis.get_rect()
        self.shadow_pole.topleft = (258, 226)
        self.game = game

        self.play_napis = self.mediumFont.render('Press SPACE to Retry!', True, (255, 255, 255))
        self.play_pole = self.score_napis.get_rect()
        self.play_pole.topleft = (170, 424)

        self.play_shadow = self.mediumFont.render('Press SPACE to Retry!', True, (0, 0, 0))
        self.play_shadow_pole = self.score_napis.get_rect()
        self.play_shadow_pole.topleft = (168, 426)

        self.counter = 1.0

        self.vec = Vector2(0, 0)

    def tick(self):
        self.vec = Vector2(sin(self.counter / 8) * 32, sin(self.counter / 12) * 18)

        self.score_napis = self.font.render('%s' % (self.score), True, (255, 250, 125))
        self.shadow_napis = self.font.render('%s' % (self.score), True, (0, 0, 0))

        self.score_pole.topleft = (262 + self.vec.x, 224 + self.vec.y)
        self.shadow_pole.topleft = (258 + self.vec.x, 227 + self.vec.y)

        self.play_pole.topleft = (170 + self.vec.x / 6, 424 + self.vec.y / 8)
        self.play_shadow_pole.topleft = (168 + self.vec.x / 6, 426 + self.vec.y / 8)

        self.counter += 0.1

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE]:
            self.isDead = False
            self.game.sounds.ambient.play(-1, 0, 5000)
            pygame.mixer.music.set_volume(0.05)

    def draw(self):
        self.game.screen.blit(self.game.background, (0, 0))

        self.game.screen.blit(self.score1_shadow, self.score1_shadow_pole)

        self.game.screen.blit(self.score1_napis, self.score1_pole)

        self.game.screen.blit(self.play_shadow, self.play_shadow_pole)

        self.game.screen.blit(self.play_napis, self.play_pole)

        self.game.screen.blit(self.shadow_napis, self.shadow_pole)

        self.game.screen.blit(self.score_napis, self.score_pole)


if __name__ == "__main__":
    Game()
