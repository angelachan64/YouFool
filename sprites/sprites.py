import pygame,sys
pygame.init()

class Block(pygame.sprite.Sprite):
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image).convert_alpha()
        #self.size = size
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(width/2 - 207.5,80)

       
    #def update(self, ):
        

size = width, height = 800, 600
black = 0,0,0
screen = pygame.display.set_mode(size)
basicsprite = Block("titletrans2.bmp")
#basicsprite.__init__(self, "../static/titletrans2.bmp")
basicgroup = pygame.sprite.Group()
basicgroup.add(basicsprite)
basicgroup.draw(screen)
pygame.display.flip()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
