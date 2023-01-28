import random

import pygame



speed = 0
speed_t=-3
rect_s=[]
rects_copy=[]


rect_around=pygame.Rect(400, 350, 100, 100)

for abc in range(15,800,30):
    for mnh in range(90,150,30):
        rect_qwadro = pygame.Rect(100, 100, 30, 30)
        rect_qwadro.center=[abc,mnh]
        rect_s.append(rect_qwadro)

    for center_2 in range(500,600,30):
        rect_qwadro_2=pygame.Rect(100, 100, 30, 30)
        rect_qwadro_2.center=[abc,center_2]
        rect_s.append(rect_qwadro_2)

# for i in range(20):
#     rects_copy.append(random.choice(rect_s))

#
# and rect_around.top <= border.bottom and rect_around.bottom < border.top:
# rect_around.top = border.bottom

def drive():
    global speed, speed_t,rects_copy

    rects_copy=rect_s.copy()
    if speed_t > 0:
        rects_copy.clear()

    drive_up()
    drive_down()


    if rect_around.right>=800:
        rect_around.right=800
        speed=-speed

    if rect_around.left<=0:
        rect_around.left=0
        speed=-speed

    if rect_around.top<=0:
        rect_around.top=0
        speed_t=-speed_t

    if rect_around.bottom>=800:
        rect_around.bottom=800
        speed_t=-speed_t



def move_rect_center():
    rect_around.center = [400, 400]


def drive_up():
    global  speed_t
    if speed_t < 0:
        for border in rects_copy.copy():
            left_right_ne_ottalk = rect_around.left >= border.right or rect_around.right <= border.left

            if left_right_ne_ottalk == True or rect_around.bottom <= border.top:
                rects_copy.remove(border)


        for last_rects in rects_copy:
            if rect_around.top <= last_rects.bottom:
                rect_around.top = last_rects.bottom
                speed_t=abs(speed_t)

def drive_down():
    global speed_t
    rect_around.top += speed_t
