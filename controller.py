import pygame
import model



def event_type():
    event = pygame.event.get()
    print(event)

    for event_2 in event:
        if event_2.type == pygame.QUIT:
            exit()

        if event_2.type==pygame.MOUSEMOTION:
            x = event_2.pos[0]
            model.rect_plat.centerx = x

            if model.mod=="ball stop":
                model.drive_plat()



        if event_2.type==pygame.MOUSEBUTTONDOWN:
            model.speed=3
            model.speed_t=-5
            model.mod="ball fly"













