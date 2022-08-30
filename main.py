import pygame
# import time
import pygame.mixer as m
import sys
import math
import random

pygame.init()
m.init()

# BGM And Image
m.music.load('Audio//bgm.wav')
m.music.play(-1)
m.music.set_volume(1)
bg_img = pygame.image.load('Icons//ground.png')

# Screen
screen = pygame.display.set_mode((400, 626))
pygame.display.set_caption('The GGO Game')
icon = pygame.image.load('Icons//ball.png')
pygame.display.set_icon(icon)

# Characters
ball = pygame.image.load('Icons//ball.png')
player = pygame.image.load('Icons//myth.png')
post = pygame.image.load('Icons//post.png')

# Positions
PlayerX = 167
PlayerY = 430
playerX_change = 0
playerY_change = 0

BallX = random.randint(10, 370)  # 167
BallY = random.randint(75, 550)  # 378
BallX_change = 0
BallY_change = 2

# Score
score_val = 0
score_font = pygame.font.SysFont('Arial', 18)

# Ball Shoot
shoot = False
Ball_in = False


def score():
    tx = score_font.render('SCORE : ' + str(score_val), True, (255, 255, 255))
    screen.blit(tx, (10, 10))


# Collision
def iscollision(px, py, bx, by):
    global Ball_in
    distance = abs(math.sqrt(math.pow(px - bx, 2) + (math.pow(py - by, 2))))
    if distance < 35:
        Ball_in = True
        return True
    else:
        return False


def ballcollision(bx, by):
    yaxis = 39
    xaxis = range(173, 214)
    if by == yaxis and bx in xaxis:
        return True
    else:
        return False


running = True
while running:
    screen.blit(bg_img, (0, 0))
    screen.blit(post, (167, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                playerY_change = -2
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                playerY_change = 2
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                playerX_change = -2
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                playerX_change = 2
            if event.key == pygame.K_SPACE:
                if Ball_in:
                    shoot = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN \
                    or event.key == pygame.K_w or event.key == pygame.K_s:
                playerY_change = 0
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT \
                    or event.key == pygame.K_a or event.key == pygame.K_d:
                playerX_change = 0

    # Player Movements
    PlayerY += playerY_change
    PlayerX += playerX_change
    if PlayerY <= 0:
        PlayerY = 0
    if PlayerY >= 536:
        PlayerY = 536
    if PlayerX <= 0:
        PlayerX = 0
    if PlayerX >= 300:
        PlayerX = 300

    # Ball Limit
    if BallY <= 26:
        BallY = random.randint(75, 540)
        BallX = random.randint(10, 345)
        shoot = False
        Ball_in = False

    # Ball Collision
    if not shoot:
        det = iscollision(PlayerX, PlayerY, BallX, BallY)
        if det:
            BallX = PlayerX + 8
            BallY = PlayerY + 27

    # Goal
    if ballcollision(BallX, BallY):
        score_val += 1
        BallX = random.randint(10, 340)
        BallY = random.randint(75, 540)
        shoot = False
        Ball_in = False

    # Ball Firing
    if shoot:
        BallY -= BallY_change
        screen.blit(ball, (BallX, BallY))
    else:
        screen.blit(ball, (BallX, BallY))

    score()
    screen.blit(player, (PlayerX, PlayerY))
    pygame.display.update()
