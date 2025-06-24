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
score =0
score_surface = font.render(f"Score: {score}", True, "#ffcc33")
screen.blit(score_surface, (20, 20))

cage = pygame.image.load('characterimages/cage.png').convert_alpha()  # Use convert_alpha for images with transparency
crab = pygame.image.load('characterimages/crab.png').convert_alpha()  # Use convert_alpha for images with transparency
beachball = pygame.image.load('characterimages/beachball.png').convert_alpha()  # Use convert_alpha for images with transparency
beachball = pygame.transform.scale(beachball, (160, 160)) 
crab = pygame.transform.scale(crab, (230, 230))
cage = pygame.transform.scale(cage,(200, 200))  
beachball_xpos = 0 #initialize
beachball_ypos = random.randint(0, 800 - 50)  
player_rect = crab.get_rect(topleft=(280, 400))
  # Initialize cage_rect

  # Center the score text at the bottom of the screen

text_rect = text_surface.get_rect(center=(400, 100))  # Center the text at the top of the screen
player_gravity = 0  # Gravity for the crab
beachballs = []
random_1 = []
for _ in range(6):
    x = random.randint(0,800-80)
    y = 0
    random_1.append(x)
    if _ != 0:
        if random_1[_] == random_1[_-1]:#makes sures the balls are evenly spaced
            x = random.randint(0,800-80)
        elif abs(random_1[_] - random_1[_-1]) < 150:
            x = random.randint(0,800-80)


    delay = _ * 150
    beachball_rect = beachball.get_rect(topleft=(x,y))
    if _ != 0:
        if random_1[_] == random_1[_-1]:#makes sures the balls are evenly spaced
            x = random.randint(0,800-80)
        elif abs(random_1[_] - random_1[_-1]) < 150:
            x = random.randint(0,800-80)

    cage_rect = cage.get_rect(topleft=(x,y)) 
    beachballs.append({'rect': beachball_rect, 'timer': delay, 'type': 'beachball'})
    o = random.randint(3,9)
    if _ != 0:
        if _ % int(o) == 0:
            beachballs.append({'rect': cage_rect, 'timer': delay, 'type': 'cage'}) # alternate between adding cage

score = 0

game_active = True  # Add this line to define game_active


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
    if game_active:
        screen.fill((0, 0, 0))  
        screen.blit(test_surface, (0, 0))  #center tje image
        screen.blit(text_surface, text_rect)
        score_surface = font.render(f"Score: {score}", True, "#ffcc33")
        screen.blit(score_surface, (20, 20))
        screen.blit(crab, player_rect)
        
        for ball in beachballs[:]:
            if ball['timer'] > 0:
                ball['timer'] -= 1
            else:
                ball['rect'].y += 6

                if ball['type'] == 'cage':
                    screen.blit(cage, ball['rect'])
                else:
                    screen.blit(beachball, ball['rect'])

            if ball['rect'].y > 800:
                ball['rect'].y = 0
                ball['rect'].x = random.randint(0, 800 - 80)
                ball['timer'] = random.randint(0, 100)  # Reset timer to a random value
                   
            if player_rect.colliderect(ball['rect']):
                if ball['type'] == 'cage':
                    beachballs.append({'rect': obstacle_rect, 'timer': delay, 'type': 'cage'})
                    game_active = False
                beachballs.remove(ball) #add sound later
                score += 1
                score_surface = font.render(f"Score: {score}", True, "#ffcc33")
                screen.blit(score_surface, (20, 20))
                x = random.randint(0, 800 - 80)
                y = 0
               
                delay = 150  # Random delay for the new beachball
                obstacle_rect = beachball.get_rect(topleft=(x,y))
                beachballs.append({'rect': obstacle_rect, 'timer': delay, 'type': 'beachball'})
            
    else:
        screen.fill("#ffcc33")
        game_over_surface = font.render("Game Over", True, "#000000")
        game_over_score = font.render(f"Your Score: {score}", True, "#000000")
        screen.blit(game_over_surface, (250, 300))
        screen.blit(game_over_score, (250, 400))

    pygame.display.update()
    clock.tick(60)

