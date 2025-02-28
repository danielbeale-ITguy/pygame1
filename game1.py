import pygame
from pygame.locals import *


RED = (255, 0, 0)
GRAY = (150, 150, 150)

pygame.init()

WIDTH = 800
HEIGHT = 500



screen = pygame.display.set_mode((WIDTH,HEIGHT))

rect_1 = pygame.Rect(0,400,100,100)


clock = pygame.time.Clock()




running = True


while running:  
    clock.tick(60)
    screen.fill(GRAY)

    pygame.draw.rect(screen,RED,rect_1)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        

        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                rect_1.left += 5
            if event.key == K_LEFT:
                rect_1.right -= 5
            if event.key == K_UP:
                rect_1.top -= 5
            if event.key == K_DOWN:
                rect_1.bottom += 5

    pygame.display.flip()
    pygame.display.update()


pygame.quit()
