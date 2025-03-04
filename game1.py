import pygame
from pygame.locals import *
import random


WIDTH = 500
HEIGHT = 500
TILE = 25
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT),0,32)


clock = pygame.time.Clock()



snake = pygame.rect.Rect([100,100,TILE-2,TILE-2])
segments = [snake.copy()]
length = 1
snake_dir = (0,0)


running = True
while running:  

    clock.tick(60)

    screen.fill('black')
    
    for segment in segments:
        pygame.draw.rect(screen,'green',segment)
    


    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

 
        if event.type == KEYDOWN:
            if event.key == K_UP:
                snake_dir = (0,-TILE)
            if event.key == K_DOWN:
                snake_dir = (0,TILE)
            if event.key == K_LEFT:
                snake_dir = (-TILE,0)
            if event.key == K_RIGHT:
                snake_dir = (TILE,0)    

    

  

    snake.move_ip(snake_dir)
    segments.append(snake.copy())
    segments = segments[-length:]
    
    pygame.display.flip()
    pygame.display.update()


pygame.quit()

  
