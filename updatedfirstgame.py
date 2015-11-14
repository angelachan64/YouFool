import pygame,sys
pygame.init()

size= width, height = 800, 600
black = 0,0,0
screen = pygame.display.set_mode(size)
loaded = []
rects = []
loaded.append(pygame.image.load("static/youfool.png").convert())
loaded.append(pygame.image.load("static/menu_button.bmp").convert())
loaded.append(pygame.image.load("static/resume_button.bmp").convert())
for i in range(0,3):
    rects.append(loaded[i].get_rect())
rects[0]=rects[0].move(width/2 - 207.5,120)
rects[1]=rects[1].move(width/2 - 196.5, 300)
rects[2]=rects[2].move(width/2 - 196.5,400)
screen.fill(black)
for i in range(0,3):
    screen.blit(loaded[i], rects[i])
pygame.display.flip()
titlescreen = True

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    if titlescreen:
        if (rects[1].collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]):
            screen.fill(black)
            pygame.display.flip()
            titlescreen = False
