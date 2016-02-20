import pygame,sys
pygame.init()

size= width, height = 800, 600
black = 0,0,0
screen = pygame.display.set_mode(size)
loaded = []
rects = []
titlescreen = True
titlescreenloaded = True
def introscreen():
    loaded.append(pygame.image.load("static/map.bmp").convert_alpha())
    titlelogo = pygame.image.load("static/titletrans.bmp").convert_alpha()
    titlelogo.set_colorkey((0,0,0))
    loaded.append(titlelogo)
    startnew = pygame.image.load("static/menu_button2.bmp").convert_alpha()
    startnew.set_colorkey((0,0,0))
    loaded.append(startnew)
    resume = pygame.image.load("static/resume_button2.bmp").convert_alpha()
    resume.set_colorkey((0,0,0))
    loaded.append(resume)
    for i in range(0,4):
        rects.append(loaded[i].get_rect())
    rects[0]=rects[0].move(0,0)
    rects[1]=rects[1].move(width/2 - 207.5,80)
    rects[2]=rects[2].move(width/2 - 196.5, 300)
    rects[3]=rects[3].move(width/2 - 196.5,400)
    screen.fill(black)
    for i in range(0,4):
        screen.blit(loaded[i], rects[i])
    pygame.display.flip()

while 1:
    if titlescreenloaded:
        introscreen()
        titlescreenloaded = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    if titlescreen:
        if (rects[2].collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]):
            screen.fill(black)
            pygame.display.flip()
            titlescreen = False
