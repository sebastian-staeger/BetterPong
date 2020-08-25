import pygame
import random
import pandas as pd
from button import Button
from player import Player
from ball import Ball

pygame.init()

# title and icon
pygame.display.set_caption('BetterPong')
ICON = pygame.image.load('racket.png')
pygame.display.set_icon(ICON)

# clock
CLOCK = pygame.time.Clock()
FONT = pygame.font.Font('freesansbold.ttf', 32)

# screen
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# players
p1 = Player(30, 270, 20, 100)
p2 = Player(850, 270, 20, 100)

# range for collision
range1 = pd.Interval(p1.y, p1.y + 100)
range2 = pd.Interval(p2.y, p2.y + 100)

# colors
color_p1 = (255, 255, 255)
color_p2 = (255, 255, 255)

# buttons to change color
button_red_p1 = Button((10, 490), (100, 100))
button_green_p1 = Button((120, 490), (100, 100))
button_blue_p1 = Button((230, 490), (100, 100))
button_red_p2 = Button((570, 490), (100, 100))
button_green_p2 = Button((680, 490), (100, 100))
button_blue_p2 = Button((790, 490), (100, 100))

# ball
ball = Ball(100, 100, 10, 10)

# middle line
middle_line = Player(450, 0, 1, 600)

# booleans for program control
menu = True
running = False


# draw game screen
def redraw_game_screen():
    screen.fill((0, 0, 0))
    if running or menu:
        score()
        draw_score(50)
        p1.draw(screen, color_p1)
        p2.draw(screen, color_p2)
        ball.draw(screen, (255, 255, 255))
        middle_line.draw(screen, (255, 255, 255))
        border_players()
        border_ball()
        game_over()
    if menu:
        draw_start_text()
        button_red_p1.draw_red(screen)
        button_green_p1.draw_green(screen)
        button_blue_p1.draw_blue(screen)
        button_red_p2.draw_red(screen)
        button_green_p2.draw_green(screen)
        button_blue_p2.draw_blue(screen)

    pygame.display.update()


# player movement
def player_move():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        p1.y -= p1.vel
        p1.interval = pd.Interval(p1.y, p1.y + 100)
    if keys[pygame.K_s]:
        p1.y += p1.vel
        p1.interval = pd.Interval(p1.y, p1.y + 100)
    if keys[pygame.K_UP]:
        p2.y -= p2.vel
        p2.interval = pd.Interval(p2.y, p2.y + 100)
    if keys[pygame.K_DOWN]:
        p2.y += p2.vel
        p2.interval = pd.Interval(p2.y, p2.y + 100)


# ball movement
def ball_move():
    if ball.ball_state_right_up:
        ball.x += ball.vel
        ball.y -= ball.vel
    if ball.ball_state_right_down:
        ball.x += ball.vel
        ball.y += ball.vel
    if ball.ball_state_left_up:
        ball.x -= ball.vel
        ball.y -= ball.vel
    if ball.ball_state_left_down:
        ball.x -= ball.vel
        ball.y += ball.vel

# borders ball and collision
def border_ball():
    if ball.ball_state_right_up and ball.y < 0:
        ball.ball_state_right_up = False
        ball.ball_state_right_down = True
    if ball.ball_state_left_up and ball.y < 0:
        ball.ball_state_left_up = False
        ball.ball_state_left_down = True
    if ball.ball_state_right_down and ball.y > 590:
        ball.ball_state_right_down = False
        ball.ball_state_right_up = True
    if ball.ball_state_left_down and ball.y > 590:
        ball.ball_state_left_down = False
        ball.ball_state_left_up = True

    # collision players
    if ball.collision_right(p2.interval):
        if ball.ball_state_right_up:
            ball.ball_state_right_up = False
            ball.ball_state_left_up = True
        else:
            ball.ball_state_right_down = False
            ball.ball_state_left_down = True
    if ball.collision_left(p1.interval):
        if ball.ball_state_left_up:
            ball.ball_state_left_up = False
            ball.ball_state_right_up = True
        else:
            ball.ball_state_left_down = False
            ball.ball_state_right_down = True


def score():
    if ball.x > 900:
        p1.score += 1
        ball.x = random.randint(100, 200)
    if ball.x < 0:
        p2.score += 1
        ball.x = random.randint(700, 800)


def border_players():
    if p1.y < 10:
        p1.y = 10
    elif p1.y > 490:
        p1.y = 490
    if p2.y < 10:
        p2.y = 10
    elif p2.y > 490:
        p2.y = 490


def draw_start_text():
    play_text = FONT.render("Press 'P' to play", True, (255, 255, 255))
    screen.blit(play_text, (325, 200))


def draw_score(y):
    sc = FONT.render("Score : " + str(p1.score) + "         Score : " + str(p2.score), True, (255, 255, 255))
    screen.blit(sc, ((900 - sc.get_width()) // 2, y))


def game_over():
    if p1.score == 5:
        p1_text = FONT.render('PLAYER1 WINS', True, color_p1)
        screen.blit(p1_text, (((900 - p1_text.get_width()) // 2), 400))
        return True
    elif p2.score == 5:
        p2_text = FONT.render('PLAYER2 WINS', True, color_p2)
        screen.blit(p2_text, (((900 - p2_text.get_width()) // 2), 400))
        return True


while menu:
    CLOCK.tick(300)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_p]:
        menu = False
        running = True  # press p to start
        p1.score = 0
        p2.score = 0
    if button_red_p1.event_handler(event):
        color_p1 = (255, 0, 0)
    if button_green_p1.event_handler(event):
        color_p1 = (0, 255, 0)
    if button_blue_p1.event_handler(event):
        color_p1 = (0, 0, 255)
    if button_red_p2.event_handler(event):
        color_p2 = (255, 0, 0)
    if button_green_p2.event_handler(event):
        color_p2 = (0, 255, 0)
    if button_blue_p2.event_handler(event):
        color_p2 = (0, 0, 255)

    player_move()
    redraw_game_screen()

    while running:
        CLOCK.tick(300)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                menu = False
        if game_over():
            running = False
            menu = True
        player_move()
        ball_move()
        redraw_game_screen()

pygame.quit()
