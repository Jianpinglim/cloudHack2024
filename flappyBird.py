import pygame
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

while running:
    SCREEN.fill((0, 0, 0))
    SCREEN.blit(bgImg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.quit:
            running = False

    playerY += playerYChange
    displayPlayer(playerX, playerY)
    pygame.display.update()

pygame.quit()