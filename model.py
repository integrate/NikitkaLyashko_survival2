import random

import pygame

qwadro=random.randint(30,200)

speed = 5
speed_t=-5
rect_s=[]
rect_around=pygame.Rect(400, 400, qwadro + 20, qwadro + 20)

for abc in range(15,800,30):
    for mnh in range(90,240,30):
        rect_qwadro = pygame.Rect(100, 100, 30, 30)
        rect_s.append(rect_qwadro)
        rect_qwadro.center=[abc,mnh]

def drive():
    global speed, speed_t
    rect_around.right+=speed
    rect_around.top+=speed_t
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

