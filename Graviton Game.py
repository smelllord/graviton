import pygame
from random import *
import math
pygame.init()

vert = False

screen = pygame.display.set_mode((700,200))
pygame.display.set_caption(("Graviton"))
icon = pygame.image.load("Icon.png")
pygame.display.set_icon(icon)

challengeimg = pygame.image.load("Challenge.png")
challengeX = 700
challengeY = choice([64,136])
challengeX_delta = 0
def challenge(x,y):
    screen.blit(challengeimg,(x,y))

playerimg = pygame.image.load("Player.png")
playerX = 0
playerY = 168
playerY_delta = 0
def player(x,y):
    screen.blit(playerimg,(x,y))

def is_collision(x1,y1,x2,y2):
    distance = math.sqrt(((x1 - x2)**2) + ((y1 - y2)**2))
    if distance <= 16:
        return True
    return False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                playerY_delta = -0.1
                challengeX_delta = 0- randint(10,100)/100
            if event.key == pygame.K_x:
                playerY_delta = 0.1
                challengeX_delta = 0 - randint(10,100)/100
    challengeX += challengeX_delta
    playerY += playerY_delta
    screen.fill((randint(100,255),randint(100,255),randint(100,255)))
    challenge(challengeX,challengeY)
    if challengeX < 0 - randint(50,500):
        challengeX = 700
        challengeY = choice([64,136])
    player(playerX,playerY)
    if playerY > 216:
        playerY = -16
    if playerY < -16:
        playerY = 216
    if is_collision(playerX,playerY,challengeX,challengeY):
        running = False
    pygame.display.update()
