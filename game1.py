import pygame
from pygame.locals import *


RED = (255, 0, 0)
GRAY = (150, 150, 150)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)


pygame.init()
WIDTH = 640
HEIGHT = 320
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()


img1 = pygame.image.load('images/path1.png')


rect_2 = img1.get_rect()





tile_size= 64
game_map = [[0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [1,1,1,1,1,1,1,1,1,1]]        
tile_list = []






playercharacter = pygame.image.load('images/cube1.png')
playercharacterrect = playercharacter.get_rect()


playerright = False
playerleft = False
playerup = False
playerdown = False




running = True

while running:  
    clock.tick(60)
    screen.fill(GRAY)

    pygame.draw.rect(screen,RED,playercharacterrect)

    
    tile_list = []
    y = 0
    for row in game_map:
        x = 0
        for segment in row:
            if segment == 1:
              screen.blit(img1,(x*64,y*64))
            x += 1
        y += 1




    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                playerright  = True











        if event.type == KEYUP:
            if event.key == K_RIGHT:
                playerright = False




    if playerright == True:
        playercharacterrect.right += 1






    
    screen.blit(playercharacter,(playercharacterrect))
    pygame.display.flip()
    pygame.display.update()


pygame.quit()



  
