import random

import pygame


def drive():
    global speed, speed_t,rects_copy

    rects_copy=rect_s.copy()

    drive_up()
    rects_copy = rect_s.copy()
    drive_down()
    rects_copy = rect_s.copy()
    drive_left()
    rects_copy = rect_s.copy()
    drive_right()


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
        print("Game Over")

def drive_plat():
    global rect_around,speed, speed_t

    x_plat=rect_plat.centerx
    y_plat=rect_plat.top
    rect_around.centerx=x_plat
    rect_around.bottom=y_plat



def move_rect_center():
    rect_around.center = [400, 400]

def drive_up():
    global  speed_t
    if speed_t < 0:
        for border in rects_copy.copy():
            left_right_ne_ottalk = rect_around.left >= border.right or rect_around.right <= border.left

            if left_right_ne_ottalk == True or rect_around.bottom <= border.top:
                rects_copy.remove(border)

        rect_around.top += speed_t

        for last_rects in rects_copy.copy():
            if rect_around.top <= last_rects.bottom:
                rect_around.top = last_rects.bottom
                speed_t=abs(speed_t)

        for black_rect in rects_copy.copy():
            if black_rect is not rect_plat and rect_around.top==black_rect.bottom:
                rects_copy.remove(black_rect)
                rect_s.remove(black_rect)


def drive_down():
    global speed_t

    if speed_t > 0:

        for border in rects_copy.copy():
            left_right_ne_ottalk = rect_around.left >= border.right or rect_around.right <= border.left

            if left_right_ne_ottalk == True or rect_around.top >= border.bottom:
                rects_copy.remove(border)

        rect_around.top += speed_t

        for last_rects in rects_copy.copy():
            if rect_around.bottom >= last_rects.top:
                rect_around.bottom = last_rects.top
                speed_t = -abs(speed_t)

        for black_rect in rects_copy.copy():
            if black_rect is not rect_plat and rect_around.bottom==black_rect.top:
                rects_copy.remove(black_rect)
                rect_s.remove(black_rect)





def drive_left():
    global speed
    if speed<0:
        for border in rects_copy.copy():
            left_right_ne_ottalk = rect_around.top >= border.bottom or rect_around.bottom <= border.top
            if left_right_ne_ottalk==True or rect_around.right<=border.left:
                rects_copy.remove(border)
        rect_around.right+=speed

        for left_black_border in rects_copy.copy():
            if rect_around.left<=left_black_border.right:
                rect_around.left=left_black_border.right
                speed=abs(speed)

        for black_rect in rects_copy.copy():
            if black_rect is not rect_plat and rect_around.left == black_rect.right:
                rects_copy.remove(black_rect)
                rect_s.remove(black_rect)

def drive_right():
    global speed
    if speed>0:
        for border in rects_copy.copy():
            left_right_ne_ottalk = rect_around.top >= border.bottom or rect_around.bottom <= border.top
            if left_right_ne_ottalk==True or rect_around.left>=border.right:
                rects_copy.remove(border)
        rect_around.right += speed

        for right_black_border in rects_copy.copy():
            if rect_around.right>=right_black_border.left:
                rect_around.right=right_black_border.left
                speed=-abs(speed)

        for black_rect in rects_copy.copy():
            if black_rect is not rect_plat and rect_around.right == black_rect.left:
                rects_copy.remove(black_rect)
                rect_s.remove(black_rect)




speed = 0
speed_t=0
rect_s=[]
rects_copy=[]

mod="ball stop"

rect_around=pygame.Rect(300, 730, 20, 20)
rect_plat=pygame.Rect(406,750,150,10)
rect_s.append(rect_plat)
drive_plat()

for abc in range(17,800,30):
    for mnh in range(17,180,30):
        rect_qwadro = pygame.Rect(100, 100, 30, 30)
        rect_qwadro.center=[abc,mnh]
        rect_s.append(rect_qwadro)

    # for center_2 in range(500,600,40):
    #     rect_qwadro_2=pygame.Rect(100, 100, 40, 40)
    #     rect_qwadro_2.center=[abc,center_2]
    #     rect_s.append(rect_qwadro_2)


for y_center_2 in range(155,480,40):
    for x_center_2 in range(10,100,40):

        rect_qwadro_2=pygame.Rect(100, 100, 40, 40)
        rect_qwadro_2.center=[x_center_2,y_center_2]
        rect_s.append(rect_qwadro_2)

    for center_2x in range(600,800,40):
        rect_qwadro_2=pygame.Rect(100, 100, 40, 40)
        rect_qwadro_2.center=[center_2x,y_center_2]
        rect_s.append(rect_qwadro_2)










