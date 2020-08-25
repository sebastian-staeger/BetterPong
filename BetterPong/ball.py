import pygame
import math


class Ball(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 2.5
        self.ball_surface = pygame.Surface((width, height))
        self.ball_state_right_up = True
        self.ball_state_right_down = False
        self.ball_state_left_up = False
        self.ball_state_left_down = False
        self.ball_state_right_straight = False
        self.ball_state_left_straight = False

    def draw(self, screen, color):
        self.ball_surface.fill(color)
        screen.blit(self.ball_surface, (self.x, self.y))

    # collision for player 1
    def collision_left(self, interval):
        if (math.floor(self.x) in range(40, 45)) and self.y in interval:
            return True

    # collision for player 2
    def collision_right(self, interval):
        if (math.floor(self.x) in range(845, 850)) and self.y in interval:
            return True
