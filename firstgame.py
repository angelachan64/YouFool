import pygame,sys

pygame.init()

size= width, height = 800, 600
black = 0,0,0
screen = pygame.display.set_mode(size)
title =pygame.image.load("title.png").convert()
new =pygame.image.load("newbutton.png").convert()
resume =pygame.image.load("resumebutton.png").convert()
#instructions =pygame.image.load("instructions.png")
titlerect = title.get_rect()
newrect = new.get_rect()
resumerect = resume.get_rect()
#instructionsrect = instructions.get_rect()
counter = 0
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    if counter == 0:
        titlerect=titlerect.move(width/2 - 112,120)
        newrect=newrect.move(width/2-146,300)
        resumerect=resumerect.move(width/2 - 122.5,400)
        #    instructionsrect=instructionsrect.move(100,50)
        screen.fill(black)
        screen.blit(title, titlerect)
        screen.blit(new, newrect)
        screen.blit(resume, resumerect)
        #    screen.blit(instructions, instructionsrect)
        pygame.display.flip()
    counter=counter + 1

    

