"""
PyGame Library for Displaying Image and changing it's coordinates
"""

""" Import Lib"""
import pygame

"""Variable for Brightness of Image"""
bright=100

""" Initialize Pygame"""
pygame.init()


""" Set the Dimension of the Screen"""
Width = 1000
Height = 800

""" Set the Screen"""
screen = pygame.display.set_mode((Width,Height))


""" Set The Title of Screen"""
pygame.display.set_caption("Display Image")


""" Load the Image"""
screenImg = pygame.image.load("Images/Space.jpg")

""" Display Image at Specific Co-Ordinate"""

screen.blit(screenImg,(150,10))

""" Update the Display Continuously"""

EventStatus = "None"

while True:
    
           
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            EventStatus="Quit"
            break
        
        
    if EventStatus == "Quit":
        break
    
print("Closing")
    
    
        
    
     
            
        

    
