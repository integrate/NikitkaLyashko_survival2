import random
import time, model, view
import pygame

# picture=pygame.display.set_mode([800,800])
#
# rect=pygame.Rect(400,400,50,100)

while True:
    time.sleep(1 / 60)
    # event = pygame.event.get()

    # for event_2 in event:
    #     if event_2.type == 256:
    #         exit()
    #
    # rect.right += 3
    # print(rect)
    #
    # picture.fill([45,76,123])
    # pygame.draw.rect(picture, [86, 255, 37], rect,1)
    #
    #
    #
    #
    #
    # pygame.display.flip()
    view.draw()
