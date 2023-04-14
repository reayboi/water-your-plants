# Example file showing a circle moving on screen
import pygame
import os

# pygame setup
pygame.init()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Water your plants!")
clock = pygame.time.Clock()
running = True
dt = 0

plantSprites = [pygame.transform.scale(pygame.image.load(os.path.join("sprites/1.png")), (300, 300)), pygame.transform.scale(pygame.image.load(os.path.join("sprites/2.png")), (300, 300)), pygame.transform.scale(pygame.image.load(os.path.join("sprites/3.png")), (300, 300)), pygame.transform.scale(pygame.image.load(os.path.join("sprites/4.png")), (300, 300))]
waterSprites = [pygame.transform.scale(pygame.image.load(os.path.join("sprites/water1.png")), (100, 100)), pygame.transform.scale(pygame.image.load(os.path.join("sprites/water2.png")), (100, 100)), pygame.transform.scale(pygame.image.load(os.path.join("sprites/water3.png")), (100, 100))]    
canSprites = [pygame.transform.scale(pygame.image.load(os.path.join("sprites/can.png")), (100, 100)), pygame.transform.scale(pygame.image.load(os.path.join("sprites/can_pouring.png")), (100, 100))]

can_rect = pygame.Rect((300, 0), (100, 100))

frame = 0
waterSprite = 0
plantSprite = 0
pouring = 0
watered = False

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    if pouring:
        if frame > 19 and frame < 40:
            waterSprite = 1
        elif frame > 39 and frame < 60:
            waterSprite = 2
        elif frame >= 60:
            waterSprite = 0
            frame = -1
            watered = True
            pouring = 0
        frame += 1

    if watered:
        if plantSprite < 3:
            plantSprite += 1

    if not pouring:
        frame = 0
        waterSprite = 0
        watered = False

    screen.blit(plantSprites[plantSprite], (50, -50))
    screen.blit(canSprites[pouring], (300, 0))

    if pygame.mouse.get_pressed()[0] and can_rect.collidepoint(pygame.mouse.get_pos()) and plantSprite < 3:
        pouring = 1
        screen.blit(waterSprites[waterSprite], (150, 50))
    else:
        pouring = 0

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()