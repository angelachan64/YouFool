import pygame,sys
pygame.init()

class basicsprite(pygame.sprite.Sprite):
    def __init__(self, image, coords):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image).convert_alpha()
        #self.size = size
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(coords)

       
    #def update(self, ):
        

size = width, height = 800, 600
black = 0,0,0
screen = pygame.display.set_mode(size)
title = basicsprite("../static/titletrans.bmp", (width/2 - 207.5,80))
maps = basicsprite("../static/map.bmp", (0,0))
resume = basicsprite("../static/resume_button2.bmp", (width/2 - 196.5,400))
start = basicsprite("../static/menu_button2.bmp", (width/2 - 196.5,300))
#basicsprite.__init__(self, "../static/titletrans.bmp")
basicgroup = pygame.sprite.Group()
basicgroup.add(maps)
basicgroup.add(title)
basicgroup.add(resume)
basicgroup.add(start)
basicgroup.draw(screen)
pygame.display.flip()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
