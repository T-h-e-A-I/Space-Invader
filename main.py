import random
import math
import pygame
from pygame import mixer
# initialize pygame
pygame.init()

# create window
screen = pygame.display.set_mode((800, 600))

running = True
# background music
mixer.music.load("background.wav")
mixer.music.play(-1)
# Title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("ufo.png").convert()
pygame.display.set_icon(icon)
# Background
background = pygame.image.load("background.jpg").convert_alpha()
# Bullet
bulletImg = pygame.image.load("bullet.png").convert_alpha()
bulletX = 370
bulletY = 480
bulletChange = 3
bulletReady = True
bulletFired = False
bulletShow = True
def bullet(x, y):
    screen.blit(bulletImg, (x, y))
# Player
playerImg = pygame.image.load("spaceship.png").convert_alpha()
playerX = 370
playerY = 480


def player(x, y):
    screen.blit(playerImg, (x, y))
# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyChange = []
no_of_enemies = 6
for i in range(no_of_enemies):
    name = "alien"+str(i)+".png"
    enemyImg.append(pygame.image.load(name).convert_alpha())
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyChange.append(0.5)

def enemy(x, y,i):
    screen.blit(enemyImg[i], (x, y))

def isCollision(bx,by,ex,ey):
    distance = math.sqrt(math.pow((bx-ex),2)+math.pow((by-ey),2))
    if distance < 27:
        return True
    else:
        return False
#score
score = 0
font = pygame.font.Font("freesansbold.ttf",32)
textX = 10
textY = 10
def showScore(x,y):
    score_value= font.render("Score : "+str(score),True,(255,255,255))
    screen.blit(score_value,(x,y))
#gameOver
gameOver = False
font2 = pygame.font.Font("freesansbold.ttf",72)
overX = 200
overY = 100
def showGameOver(x,y):
    score_value= font2.render("GAME OVER",True,(255,255,255))
    screen.blit(score_value,(x,y))
# Game loop
while running:
    # RGB
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_LEFT:
        #         playerX -= 5
        #         print(playerX)
        #     if event.key == pygame.K_RIGHT:
        #         playerX += 5
        #         print(playerX)
    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[pygame.K_LEFT]:
        if playerX > 0:
            playerX -= 3

    if keys_pressed[pygame.K_RIGHT]:
        if playerX < 736:
            playerX += 3
    if keys_pressed[pygame.K_SPACE]:
        bullet_fired = mixer.Sound("laser.wav")
        bullet_fired.play()
        bulletX = playerX
        bulletReady = False
        bulletFired = True

    for i in range(no_of_enemies):
        if enemyY[i]>420:
            gameOver = True
        if enemyX[i] > 736:
            enemyChange[i] = -0.5
            enemyY[i] += 30
        if enemyX[i] < 0:
            enemyChange[i] = 0.5
            enemyY[i] += 30

        enemyX[i] += enemyChange[i]
        if isCollision(bulletX,bulletY,enemyX[i],enemyY[i]) and not(gameOver):
            bulletFired = False
            bulletReady = True
            bulletY = 480
            bulletX = playerX
            enemyX[i] =  random.randint(0, 736)
            enemyY[i] =  random.randint(30, 230)
            score = score+1
            collision_sound = mixer.Sound("explosion.wav")
            collision_sound.play()
            print(score)
    if bulletFired:
        bulletY -= bulletChange
    if bulletY < 0:
        bulletFired = False
        bulletReady = True
        bulletY = 480
        bulletX = playerX
    if bulletReady == True and bulletFired == False:
        bullet(playerX + 16, bulletY)
    else:
        bullet(bulletX + 16, bulletY)
    player(playerX, playerY)
    if not(gameOver):
        for i in range (no_of_enemies):
            enemy(enemyX[i],enemyY[i],i)
    if gameOver:
            showGameOver(overX,overY)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    showScore(textX,textY)
    pygame.display.update()
