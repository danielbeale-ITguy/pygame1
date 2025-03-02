import pygame
from pygame.locals import *


RED = (255, 0, 0)
GRAY = (150, 150, 150)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)


pygame.init()

WIDTH = 640
HEIGHT = 640


screen = pygame.display.set_mode((WIDTH,HEIGHT))


clock = pygame.time.Clock()

img = pygame.image.load('ground.png')
img.convert()

rect_1  = img.get_rect()



tile_size= 64

game_map = [[0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,1,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,1,1,0,0,1,0,0,0],
            [0,0,0,0,0,0,0,0,0,0]]

tile_list = []


running = True


while running:  
    clock.tick(60)
    screen.fill(GRAY)


    
    tile_list = []

    y = 0
    for row in game_map:
        x = 0
        for segment in row:
            if segment == 1:
              screen.blit(img,(x*64,y*64))
            x += 1
        y += 1









    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                rect_1.right += 1
            




    

    
    pygame.display.flip()
    pygame.display.update()


pygame.quit()
