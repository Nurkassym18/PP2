import pygame
import datetime
import time

pygame.init()

screen = pygame.display.set_mode((700,600))
middle = (350,300)
pygame.display.set_caption("Mickey Clocks")

clock = pygame.time.Clock()

icon = pygame.image.load("mainclock.png")
icon = pygame.transform.scale(icon,(700,600))

right_minute = pygame.image.load("rightarm.png")
left_second = pygame.image.load("leftarm.png")

rectmin = right_minute.get_rect(center=middle)
rectsec = left_second.get_rect(center=middle)

running = True

angle_minute=0
angle_second=0


while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    time = datetime.datetime.now()
    minuteTime = time.minute
    secondTime = time.second
   

    angle_minute = -minuteTime*6-54
    angle_second = -secondTime*6

    leg_min = pygame.transform.rotate(right_minute,angle_minute)
    rectmin1 = leg_min.get_rect(center=middle)



    leg_sec = pygame.transform.rotate(left_second,angle_second)
    rectsec1 = leg_sec.get_rect(center=middle)

    screen.blit(icon,(0,0))
    screen.blit(leg_sec,rectsec1)
    screen.blit(leg_min,rectmin1)

    pygame.display.flip()
    clock.tick(60)

    