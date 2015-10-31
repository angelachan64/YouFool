import pygame,sys

pygame.init()

size= width, height = 320, 240
black = 0,0,0
screen = pygame.display.set_mode(1336, 768)
title =pygame.image.load("title.png").convert()
new =pygame.image.load.load("newbutton.png").convert()
resume =pygame.image.load("resumebutton.png").convert()
instructions =pygame.image.load("instructions.png")
titlerect=titlerect.move(160,120)
newrect=newrect.move(200,150)
resumerect=resumerect.move(250,150)
instructionsrect=instructionsrect.move(100,50)
screen.fill(black)
screen.blit(title, titlerect)
screen.blit(new, newrect)
screen.blit(resume, resumerect)
screen.blit(instructions, instructionsrect)
pygame.display.flip()

    

