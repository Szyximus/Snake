import pygame, random, time

class SoundManager:

    def __init__(self, game):

        self.ambient = pygame.mixer.Sound('./sound/ambient.wav')
        self.eatSound = pygame.mixer.Sound('./sound/chew.wav')
        self.boostSound = pygame.mixer.Sound('./sound/boost.wav')

        self.deathSound = pygame.mixer.Sound('./sound/death1.wav')
        self.deathSound2 = pygame.mixer.Sound('./sound/death2.wav')

        self.game = game
        pygame.mixer.music.load('./sound/music.wav')  # muzyka w tle
        pygame.mixer.music.play(-1, 0.0)