import pygame
from sys import exit
import random

pygame.init() #starts pygame 

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Beach Blitz") #sets the title of the window
clock = pygame.time.Clock() # create a Clock object
font = pygame.font.Font('textfont/Pixel-regular.ttf',50)

test_surface = pygame.image.load('graphicsbg/background.png')
bg_rect = test_surface.get_rect(center=(400, 300))  #centerofscreen
text_surface = font.render('Beach Blitz', False, '#ffcc33')
text_surface_1 = font.render('Score', False, '#ffcc33')

crab = pygame.image.load('characterimages/crab.png').convert_alpha()  # Use convert_alpha for images with transparency
beachball = pygame.image.load('characterimages/beachball.png').convert_alpha()  # Use convert_alpha for images with transparency
beachball = pygame.transform.scale(beachball, (160, 160)) 
crab = pygame.transform.scale(crab, (230, 230))  
beachball_xpos = 0 #initialize
beachball_ypos = random.randint(0, 800 - 50)  
player_rect = crab.get_rect(topleft=(280, 400))
obstacle_rect = beachball.get_rect(topleft=(beachball_ypos, 0))  
text_1_rect = text_surface_1.get_rect(center=(400, 700))  # Center the score text at the bottom of the screen

text_rect = text_surface.get_rect(center=(400, 100))  # Center the text at the top of the screen
player_gravity = 0  # Gravity for the crab

while True:
    for event in pygame.event.get(): #checks for all possible events
        if event.type == pygame.QUIT: #if quit then quit
            pygame.quit() #closes the window
            exit() #exits the program

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_rect.left > 0:
        player_rect.x -= 10  
    if keys[pygame.K_RIGHT] and player_rect.right < 800:
        player_rect.x += 10
    
    if keys[pygame.K_UP] and player_rect.bottom >= 800:
        player_gravity = -20  

    
    player_gravity += 1
    player_rect.y += player_gravity

   #prevents crb from falling
    if player_rect.bottom >= 800:
        player_rect.bottom = 800
        player_gravity = 0

    screen.fill((0, 0, 0))  
    screen.blit(test_surface, (0, 0))  #center tje image
    screen.blit(text_surface, text_rect)
    screen.blit(text_surface_1, text_1_rect)  
    screen.blit(crab, player_rect) 
    screen.blit(beachball, (beachball_ypos, beachball_xpos))  
    beachball_xpos += 10  
    if beachball_xpos > 800: 
        beachball_xpos = -230
        beachball_ypos = random.randint(0, 800 - 50)  # Start from the top again
    pygame.display.update()
    clock.tick(60)

