import pygame
from pygame.locals import *
import random


WIDTH = 500
HEIGHT = 500
TILE = 25
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT),0,32)


clock = pygame.time.Clock()


x = 0
y = 0


snake_body = [(x,y)]

  

Direction = 'LEFT'



running = True
while running:  

    clock.tick(10)

    
    
    screen.fill('black')

    
    fruit = pygame.draw.rect(screen,'blue',(100,0,TILE,TILE))
    

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type ==KEYDOWN:
            if event.key == K_RIGHT:
                Direction = 'RIGHT'        
            



    
    if Direction == 'RIGHT':
        x += TILE


    snake_body.insert(0,(x,y))

    #find way to check if snake body postion 1 == Fruit Rect if so increase then snake body insert again
#    if Direction == 'RIGHT':
#        snake_body.insert(0,(x,y))    
    




    snake_body.pop()

#   
 
    for i in snake_body:
        pygame.draw.rect(screen,'pink',(i[0],i[1],TILE,TILE))

 
    
        
    
    pygame.display.flip()
    pygame.display.update()


pygame.quit()
