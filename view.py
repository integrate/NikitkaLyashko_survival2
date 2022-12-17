import pygame, model



picture=pygame.display.set_mode([800,800])

def draw():
    picture.fill([45,76,123])
    pygame.draw.rect(picture, [86, 255, 37], model.rect,1)

    pygame.display.flip()