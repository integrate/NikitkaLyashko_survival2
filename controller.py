import pygame

import model


def event_type():
    event = pygame.event.get()

    for event_2 in event:
        if event_2.type == 256:
            exit()

        if event_2.type==pygame.KEYDOWN:
            print(event_2)
            if event_2.key==pygame.K_SPACE:
                model.move_rect_center()








