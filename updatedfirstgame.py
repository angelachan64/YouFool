import pygame,sys

pygame.init()

size= width, height = 800, 600
black = 0,0,0
screen = pygame.display.set_mode(size)
title =pygame.image.load("titletrans.bmp").convert()
'''new =pygame.image.load("menu_button.bmp").convert()'''
resume =pygame.image.load("resumebutton.bmp").convert()
titlerect = title.get_rect()
newrect = new.get_rect()
resumerect = resume.get_rect()
titlerect=titlerect.move(width/2 - 207.5,120)
newrect=newrect.move(width/2-196.5,300)
resumerect=resumerect.move(width/2 - 122.5,400)
screen.fill(black)
screen.blit(title, titlerect)
screen.blit(new, newrect)
screen.blit(resume, resumerect)
pygame.display.flip()
'''
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
'''
