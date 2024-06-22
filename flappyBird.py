import pygame
import random
pygame.init()

SCREEN = pygame.display.set_mode((500, 750))

bgImg = pygame.image.load('pygameBG.png')
playerImg = pygame.image.load('player.png')

playerX = 50
playerY = 300
playerYChange = 0

running = True

def displayPlayer(x, y):
    SCREEN.blit(playerImg, (x, y))

# Pipes stuff
obs_width = 70
obs_ht = random.randint(150, 450)
obs_clr = (211, 253, 117)
obs_x_change = -6
obs_x = 500

def display_obstacle(height):
    top_obs_height = height
    bottom_obs_height = 635 - height - 150  # Calculate the bottom part height based on top height

    pygame.draw.rect(SCREEN, obs_clr, (obs_x, 0, obs_width, top_obs_height))
    pygame.draw.rect(SCREEN, obs_clr, (obs_x, 635 - bottom_obs_height, obs_width, bottom_obs_height))

while running:
    SCREEN.fill((0, 0, 0))
    SCREEN.blit(bgImg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    playerY += playerYChange

    if playerY <= 0:
        playerY = 0
    if playerY >= 571:
        playerY = 571

    obs_x += obs_x_change
    if obs_x <= -obs_width:  # Check if obstacle has moved off the screen
        obs_x = 500
        obs_ht = random.randint(200, 400)  # Generate new random height for next obstacle

    display_obstacle(obs_ht)

    displayPlayer(playerX, playerY)
    pygame.display.update()

pygame.quit()
