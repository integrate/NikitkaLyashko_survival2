import random

import pygame


def drive():
    global speed, speed_t,rects_copy, mod, live
    if mod=="ball stop" or mod=="Game Over":
        return
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
        mod = "ball stop"
        drive_plat()
        live=live-1
        if live==0:
            mod="Game Over"

    if c==2:
        level_2()
        if c==3:
            level_3()

def drive_plat():
    global rect_around,speed, speed_t

    x_plat=rect_plat.centerx
    y_plat=rect_plat.top
    rect_around.centerx=x_plat
    rect_around.bottom=y_plat



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

def level_3():
    global mod
    mod = "ball stop"
    drive_plat()

    for abc in range(80, 120, 30):
        for mnh in range(107, 137, 30):
            rect_qwadro = pygame.Rect(100, 100, 30, 30)
            rect_qwadro.center = [abc, mnh]
            rect_s.append(rect_qwadro)


def level_2():
    global mod,c
    mod = "ball stop"
    drive_plat()

    for abc in range(50, 80, 30):
        for mnh in range(77, 107, 30):
            rect_qwadro = pygame.Rect(100, 100, 30, 30)
            rect_qwadro.center = [abc, mnh]
            rect_s.append(rect_qwadro)
    c=3



speed = 10
speed_t=-8
live=3
rect_s=[]
rects_copy=[]

mod="ball stop"
c=0

rect_around=pygame.Rect(300, 730, 20, 20)
rect_plat=pygame.Rect(406,750,150,10)
rect_s.append(rect_plat)
drive_plat()

for abc in range(17,47,30):
    for mnh in range(47,77,30):
        rect_qwadro = pygame.Rect(100, 100, 30, 30)
        rect_qwadro.center=[abc,mnh]
        rect_s.append(rect_qwadro)
c=2













