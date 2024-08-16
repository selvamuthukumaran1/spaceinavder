import pygame

# Initialize the pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Title and icon
pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('shuttle.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0

def player(x, y):
    screen.blit(playerImg, (x, y))

# Initialize clock
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    # RGB - red, green, blue
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Keystroke left or right
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3  # Adjust speed as needed

            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3  # Adjust speed as needed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Update the player's position
    playerX += playerX_change

    # Draw the player
    player(playerX, playerY)

    # Update the display
    pygame.display.update()

    # Cap the frame rate to 60 frames per second
    clock.tick(60)

pygame.quit()
