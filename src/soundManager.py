import pygame, os


class SoundManager:
    def __init__(self, game):
        dir = os.path.dirname(__file__)

        self.ambient = pygame.mixer.Sound(os.path.join(dir, '../sound/ambient.wav'))
        self.eatSound = pygame.mixer.Sound(os.path.join(dir, '../sound/chew.wav'))
        self.boostSound = pygame.mixer.Sound(os.path.join(dir, '../sound/boost.wav'))

        self.deathSound = pygame.mixer.Sound(os.path.join(dir, '../sound/death1.wav'))
        self.deathSound2 = pygame.mixer.Sound(os.path.join(dir, '../sound/death2.wav'))

        self.game = game
        pygame.mixer.music.load(os.path.join(dir, '../sound/music.wav'))  # muzyka w tle
        pygame.mixer.music.play(-1, 0.0)
