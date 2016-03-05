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
        self.xcor = coords[0]
        self.ycor = coords[1]
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

character = basicsprite("characteranimations/down0.bmp", (width/2-15,height/2-26))
background2 = basicsprite("../static/map.bmp", (0,-height/4))
#enemy = basicsprite("bobby.bmp", (width/2-15,height/2-26))

screen1=False
introscreen = True
screen1group= pygame.sprite.OrderedUpdates()
count=0
movex=-2
movey=2
walkcount=0                                                                                                                                                                                                                 
dirnum = 1
lastKey= "down"

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
            screen1group.add(background2) 
            screen1group.add(character)
            #screen1group.add(enemy)
            screen1group.draw(screen)
            pygame.display.flip()
            background.fill(black)

        elif pygame.mouse.get_pressed()[0] and introgroup.sprites()[2].rect.collidepoint(pygame.mouse.get_pos()):
            introgroup.empty()
            introgroup.clear(screen, background)
            pygame.display.flip()
            introscreen = False
            screen1 = True
            screen1group.add(background2) 
            screen1group.add(character)
            screen1group.draw(screen)
            pygame.display.flip()

    
    if screen1 == True:
        changex = 0
        changey = 0
        directions = "down"
        if event.type != pygame.KEYDOWN:
            walkcount=0
            character.image = pygame.image.load("characteranimations/"+ lastKey + str(0) + ".bmp").convert_alpha()
            introgroup.clear(screen, background)
            screen1group.draw(screen)
            pygame.display.flip()
        if (character.xcor > 0 and character.xcor < width and character.ycor > 0 and character.ycor < height):        
            if( pygame.key.get_pressed()[pygame.K_w] != 0 and character.ycor > 0 ):
                changey = -5
                lastKey = "up"
                character.rect=character.rect.move(changex,changey)
            elif( pygame.key.get_pressed()[pygame.K_a] != 0 and character.xcor > 0):
                changex = -5
                lastKey = "left"
                character.rect=character.rect.move(changex,changey)
            elif( pygame.key.get_pressed()[pygame.K_s] != 0 and character.ycor < height):
                changey = 5
                lastKey = "down"
                character.rect=character.rect.move(changex,changey)
            elif( pygame.key.get_pressed()[pygame.K_d] != 0 and character.xcor < width):
                changex = 5
                lastKey = "right"
                character.rect=character.rect.move(changex,changey)
            walkcount=walkcount+1
            print "IM UP"
            #walkcount=walkcount+1
            #if (walkcount % 10 != 0):
            character.image = pygame.image.load("characteranimations/" + lastKey + str((walkcount/5) % 9) + ".bmp").convert_alpha()
            #introgroup.clear(screen, background)
            #screen1group.draw(screen)
            #pygame.display.flip()
                    
                    
            #character.image= pygame.image.load("characterup.bmp").convert_alpha()
            introgroup.clear(screen, background)
            screen1group.draw(screen)
            pygame.display.flip()
            sleep(0.029)
  
