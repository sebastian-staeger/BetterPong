import pygame


class Button(object):

    def __init__(self, position, size):

        # create 3 buttons
        self.buttons = [
            pygame.Surface(size),
            pygame.Surface(size),
            pygame.Surface(size),
        ]

        # fill buttons with color
        self.buttons[0].fill((255, 0, 0))
        self.buttons[1].fill((0, 255, 0))
        self.buttons[2].fill((0, 0, 255))

        # get button size and position
        self.square = pygame.Rect(position, size)

        # button indices
        self.index0 = 0
        self.index1 = 1
        self.index2 = 2

    def draw_red(self, screen):

        # draw red button
        screen.blit(self.buttons[self.index0], self.square)

    def draw_green(self, screen):

        # draw green button
        screen.blit(self.buttons[self.index1], self.square)

    def draw_blue(self, screen):

        # draw blue button
        screen.blit(self.buttons[self.index2], self.square)

    def event_handler(self, event):

        # change player color when button is pressed
        if event.type == pygame.MOUSEBUTTONDOWN:  # some button is clicked
            if event.button == 1:  # left button is clicked
                if self.square.collidepoint(event.pos):  # is mouse over button
                    return True
