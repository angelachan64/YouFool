import sys, pygame #In order to use the functions in sys and pygame, you need to
                   #import.

pygame.init() #starts pygame

size = width,height=320,240 #sets variable "size" to 320, 240
speed = [2, 2] #sets variable "speed" to [2, 2] --> LIST
black = 0, 0, 0 #sets variable "black" to 0, 0, 0

screen = pygame.display.set_mode(size) #takes a variable with two numbers
                                       #"size" variable refers back to 320,240

ball = pygame.image.load("ball.bmp") #
ballrect = ball.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit() #will exit the program if x'ed
        
        ballrect = ballrect.move(speed) #makes ball move in the x and y 
                                        #directions
        if ballrect.left < 0 or ballrect.right > width: #
            speed[0] = -speed[0]
        if ballrect.top < 0 or ballrect.bottom > height:
            speed[1] = -speed[1]
                
        screen.fill(black)
        screen.blit(ball, ballrect)
        pygame.display.flip()

