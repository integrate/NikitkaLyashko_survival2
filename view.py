import pygame, model
pygame.init()
picture=pygame.display.set_mode([812,800])

f=pygame.font.SysFont("arial",30,True)
font=pygame.font.SysFont("arial",150,True)
text=f.render("осталось жизней:"+str(model.live),True,[89,12,93],None)
game_over=font.render("Game Over",True,[255,0,0],None)

def draw():
    picture.fill([45,76,123])
    if model.mod!="Game Over":
        pygame.draw.circle(picture, [91, 135, 37], model.rect_around.center, model.rect_around.width // 2)
    pygame.draw.rect(picture,[0,0,0],model.rect_plat)
    text = f.render("осталось жизней:" + str(model.live), True, [89, 12, 93], None)
    if model.mod=="Game Over":
        picture.blit(game_over, [406 - game_over.get_width() / 2, 400])



    for rect_qwadro_1 in model.rect_s:
        pygame.draw.rect(picture,[255,56,64],rect_qwadro_1,2)

    # for color_blok in model.rects_copy:
    #     pygame.draw.rect(picture, [0, 0,0], color_blok,4)



    picture.blit(text,[812-text.get_width(),0])



    pygame.display.flip()