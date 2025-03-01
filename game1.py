import pygame
from pygame.locals import *


RED = (255, 0, 0)
GRAY = (150, 150, 150)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

color = GREEN
pygame.init()

WIDTH = 1200
HEIGHT = 800


screen = pygame.display.set_mode((WIDTH,HEIGHT))
x = 0
rect_1 = pygame.Rect(x,400,50,50)
Goal = pygame.Rect(900,750,10,75)


clock = pygame.time.Clock()


running = True

square_right = False
square_left = False
square_up = False
square_down = False


while running:  
    clock.tick(60)
    screen.fill(GRAY)

    #if rect_1.colliderect(Goal):
    #   running = False
    
    if rect_1.x == 900:
        rect_1.x = 0 

    pygame.draw.rect(screen,color,rect_1)
    pygame.draw.rect(screen,BLUE,Goal)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# move square in certain direction if key is pressed         
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                square_right = True
            if event.key == K_LEFT:
                square_left = True
            if event.key == K_UP:
                square_up = True
            if event.key == K_DOWN:
                square_down = True
# stop moving square if key is no longer pressed 
        if event.type == KEYUP:
            if event.key == K_RIGHT:
                square_right = False
            if event.key == K_LEFT:
                square_left = False
            if event.key == K_UP:
                square_up = False
            if event.key == K_DOWN:
                square_down = False


#movement speed
    if square_right == True:
        rect_1.right += 3
    if square_left == True:
        rect_1.left -= 3
    if square_up == True:
        rect_1.top -= 3
    if square_down == True:
        rect_1.bottom += 3



    pygame.display.flip()
    pygame.display.update()


pygame.quit()
