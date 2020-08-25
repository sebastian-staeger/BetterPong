import pygame
import pandas as pd


class Player(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 2
        self.player_surface = pygame.Surface((width, height))
        self.interval = pd.Interval(y, y + 100)
        self.score = 0

    def draw(self, screen, color):
        self.player_surface.fill(color)
        screen.blit(self.player_surface, (self.x, self.y))
