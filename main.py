import pygame
import random
# Initialize the pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Title and icon
pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('shuttle.png')
pygame.display.set_icon(icon)

# Background
background = pygame.image.load('back.png')

# Player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = pygame.image.load('play.png')
enemyImgX = 736
enemyImgY = 20
enemyX_change = 0
enemyY_change = 30

# Bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = 'ready'

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y):
    screen.blit(enemyImg, (x, y))

def bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg, (x, y))
# Initialize clock
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    # RGB - red, green, blue
    screen.fill((128, 128, 128))
    # Background image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Keystroke left or right
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -2.5  # Adjust speed as needed

            if event.key == pygame.K_RIGHT:
                playerX_change = 2.5  # Adjust speed as needed

            if event.key == pygame.K_SPACE:
                bullet(playerX, bulletY_change)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Update the player's position
    playerX += playerX_change
    enemyImgX += enemyX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    if enemyImgX <= 0:
        enemyX_change = 2
        enemyImgY += enemyY_change
    elif enemyImgX >= 736:
        enemyX_change = -2
        enemyImgY += enemyY_change

    if bullet_state == 'fire':
        bullet(playerX, bulletY)
        bulletY -= bulletY_change


    # Draw the player
    player(playerX, playerY)

    # Enemy
    enemy(enemyImgX, enemyImgY)

    bullet(playerX, playerY)
    # Update the display
    pygame.display.update()

    # Cap the frame rate to 60 frames per second
    clock.tick(60)

pygame.quit()
