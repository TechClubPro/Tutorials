"""
PyGame Library for Displaying Image
"""

""" Import Lib"""
import pygame

"""Variable for Brightness of Image"""
bright=100

""" Initialize Pygame"""
pygame.init()


""" Set the Dimension of the Screen"""
Width = 1000
Height = 1000

""" Set the Screen"""
screen = pygame.display.set_mode((Width,Height))


""" Set The Title of Screen"""
pygame.display.set_caption("Display Image")


""" Load the Image"""
screenImg = pygame.image.load("Images/Space.jpg")

""" Display Image at Specific Co-Ordinate"""

screen.blit(screenImg,(0,0))

""" Update the Display Continuously"""

EventStatus = "None"

while True:
    
           
    pygame.display.update()
    

    
        
    
     
            
        

    
