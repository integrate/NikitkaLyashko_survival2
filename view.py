import pygame, model



picture=pygame.display.set_mode([810,800])

def draw():
    picture.fill([45,76,123])
    pygame.draw.rect(picture, [86, 255, 37], model.rect_around, 1)
    pygame.draw.circle(picture, [91, 135, 37], model.rect_around.center, model.rect_around.width // 2, 1)

    for rect_qwadro_1 in model.rect_s:
        pygame.draw.rect(picture,[255,56,64],rect_qwadro_1,2)



    pygame.display.flip()
