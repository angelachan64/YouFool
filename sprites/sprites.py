from time import sleep
import pygame
import sys
pygame.init()

class basicsprite(pygame.sprite.Sprite):
    def __init__(self, image, coords):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image).convert_alpha()
        #self.size = size
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(coords)
    def get_Coords():
        return coords

size = width, height = 800, 600
black = 0,0,0
screen = pygame.display.set_mode(size)
background = pygame.Surface(screen.get_size()).convert()
background.fill(black)
title = basicsprite("../static/titletrans2.bmp", (width/2 - 207.5,80))
maps = basicsprite("../static/map.bmp", (0,-height/4))
resume = basicsprite("../static/resume_button2.bmp", (width/2 - 196.5,400))
start = basicsprite("../static/menu_button2.bmp", (width/2 - 196.5,300))
#basicsprite.__init__(self, "../static/titletrans.bmp")
introgroup = pygame.sprite.OrderedUpdates()
introgroup.add(maps)
introgroup.add(title)
introgroup.add(resume)
introgroup.add(start)
introgroup.draw(screen)
pygame.display.flip()

character = basicsprite("characterdown.bmp", (width/2-15,height/2-26))

screen1=False
introscreen = True
screen1group= pygame.sprite.OrderedUpdates()
count=0
movex=-2
movey=2
walkcount=0
dirnum = 1

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    if introscreen == True:
        if count==60:
            movey*=-1

        if count==150:
            movex*=-1
            count=0
        maps.rect=maps.rect.move(movex,movey)
        introgroup.draw(screen)
        pygame.display.flip()
        sleep(0.025)
        count+=1
        if pygame.mouse.get_pressed()[0] and introgroup.sprites()[3].rect.collidepoint(pygame.mouse.get_pos()):
            introgroup.empty()
            introgroup.clear(screen, background)
            pygame.display.flip()
            introscreen = False
            screen1= True

            screen1group.add(character)
            screen1group.draw(screen)
            pygame.display.flip()



        elif pygame.mouse.get_pressed()[0] and introgroup.sprites()[2].rect.collidepoint(pygame.mouse.get_pos()):
            introgroup.empty()
            introgroup.clear(screen, background)
            pygame.display.flip()
            introscreen = False
            screen1 = True

            screen1group.add(character)
            screen1group.draw(screen)
            pygame.display.flip()

    if screen1== True:

        if( pygame.key.get_pressed()[pygame.K_w] != 0 ):
            walkcount=walkcount+1
            print "IM HERE"
            if (walkcount % 3 != 0):
                print "IM HERE TOO"
                character.image = pygame.image.load("characteranimations/up" + str(dirnum) + ".bmp").convert_alpha()
                introgroup.clear(screen, background)
                screen1group.draw(screen)
                pygame.display.flip()
                dirnum += 1
            else:
                dirnum = dirnum % 10 + 1
            character.image= pygame.image.load("characterup.bmp").convert_alpha()
            introgroup.clear(screen, background)
            character.rect=character.rect.move(0,-5)
            screen1group.draw(screen)
            pygame.display.flip()
            sleep(0.025)
        elif( pygame.key.get_pressed()[pygame.K_a] != 0 ):
            print "IM THERE"
            walkcount=walkcount+1
            if( walkcount % 10 != 0):
                print "IM THERE TOO"
                character.image = pygame.image.load("characteranimations/left" + str(dirnum) + ".bmp").convert_alpha()
                introgroup.clear(screen, background)
                screen1group.draw(screen)
                pygame.display.flip()
                dirnum += 1
            else:
                dirnum = dirnum % 10 + 1
            character.image= pygame.image.load("characterleft.bmp").convert_alpha()
            introgroup.clear(screen, background)
            character.rect=character.rect.move(-5,0)
            screen1group.draw(screen)
            pygame.display.flip()
            sleep(0.025)
        elif( pygame.key.get_pressed()[pygame.K_s] != 0 ):
            walkcount=walkcount+1
            print "IM SOMEWHERE"
            if( walkcount % 10 != 0):
                print "IM SOMEHWERE TOO"
                character.image = pygame.image.load("characteranimations/down" + str(dirnum) + ".bmp").convert_alpha()
                introgroup.clear(screen, background)
                screen1group.draw(screen)
                pygame.display.flip()
                dirnum += 1
            else:
                dirnum = dirnum % 10 + 1
            character.image= pygame.image.load("characterdown.bmp").convert_alpha()
            introgroup.clear(screen, background)
            character.rect=character.rect.move(0,5)
            screen1group.draw(screen)
            pygame.display.flip()
            sleep (0.25)
        elif( pygame.key.get_pressed()[pygame.K_d] != 0 ):
            walkcount=walkcount+1
            print "IM NOWHERE"
            if( walkcount % 10 != 0):
                print "IM NOWHERE TOO"
                character.image = pygame.image.load("characteranimations/right" + str(dirnum) + ".bmp").convert_alpha()
                introgroup.clear(screen, background)
                screen1group.draw(screen)
                pygame.display.flip()
                dirnum +=1
            else:
                dirnum = dirnum % 10 + 1
            character.image= pygame.image.load("characterright.bmp").convert_alpha()
            introgroup.clear(screen, background)
            character.rect=character.rect.move(5,0)
            screen1group.draw(screen)
            pygame.display.flip()
            sleep(0.25)
