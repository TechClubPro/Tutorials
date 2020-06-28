"""
Program for Image Movement
"""



""" Import Lib"""
import pygame
import rotateImage as rotator
import time


""" Initialize Pygame"""
pygame.init()


""" Set the Dimension of the Screen"""
Width = 483
Height = 484

""" Set the Screen"""

screen = pygame.display.set_mode((Width,Height))

""" Set The Title of Screen"""

pygame.display.set_caption("Moving Image")

""" Load the Image"""
screenImg = pygame.image.load("Images/MicroMouse Grid.jpg")

""" Display Image at Specific Co-Ordinate"""

screen.blit(screenImg,(0,0))


"""Load the Bot Image"""
botImg= pygame.image.load("Images/Grid BOt.png")
screen.blit(botImg,(0,0))
# rotator.blitRotate(screen,botImg,(15,15),180)

path=[]

pathInput = ""

stepNum=1
EventStatus=""
cellX=0
cellY=0
while True:
    
    
    pygame.display.flip()
    pygame.display.update()
    time.sleep(0.5)
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            EventStatus="Quit"
            break
       
        
    if EventStatus == "Quit":
        break
    
    screen.blit(screenImg,(0,0))
    
    # screen.blit(botImg,(10,10))
    rotator.blitRotate(screen,botImg,(15,45),180)
    
    # if cellY<=420:
    #     screen.blit(botImg,(0,cellY))
    #     cellY=cellY+30
        
    # else:
    #     screen.blit(botImg,(cellX,cellY))
    #     cellX=cellX+30
 
   
