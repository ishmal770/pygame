import pygame
from sys import exit
import random

pygame.init() #starts pygame 
def crabwalk():
    global crab, crab_ind
    crab_ind += 0.1
    if crab_ind >= len(crabwalk_frames):
        crab_ind = 0
    crab = crabwalk_frames[int(crab_ind)]
def setup_beachballs():
    beachballs.clear()
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
        o= random.randint(3,9)
        if _ % int(o) == 0:
            beachballs.append({'rect': beachball_rect, 'timer': delay, 'type': 'beachball'})
        
        if _ != 0:
            if random_1[_] == random_1[_-1]:#makes sures the balls are evenly spaced
                x = random.randint(0,800-80)
            elif abs(random_1[_] - random_1[_-1]) < 20:
                x = random.randint(0,800-80)
        delay = _ * 250
        cage_rect = cage.get_rect(topleft=(x,y)) 
        o = random.randint(7,13)
        if _ % int(o) == 0:
            beachballs.append({'rect': cage_rect, 'timer': delay, 'type': 'cage'}) # alternate between adding cage
        
        
        if _ != 0:
            if random_1[_] == random_1[_-1]:#makes sures the balls are evenly spaced
                x = random.randint(0,800-80)
            elif abs(random_1[_] - random_1[_-1]) < 250:
                x = random.randint(0,800-80)
        delay = _ * 250
        red_rect = redball.get_rect(topleft=(x,y))
        o = random.randint(14,18)
        if _ % int(o) == 0:
            beachballs.append({'rect': red_rect, 'timer': delay, 'type': 'red'}) # alternate between adding cage
        
        if _ != 0:
            if random_1[_] == random_1[_-1]:#makes sures the balls are evenly spaced
                x = random.randint(0,800-80)
            elif abs(random_1[_] - random_1[_-1]) < 250:
                x = random.randint(0,800-80)
        delay = _ * 250
        blue_rect = blueball.get_rect(topleft=(x,y)) 
        o = random.randint(6,12)
        if _ % int(o) == 0:
            beachballs.append({'rect': blue_rect, 'timer': delay, 'type': 'blue'})
        

        if _ != 0:
            if random_1[_] == random_1[_-1]:#makes sures the balls are evenly spaced
                x = random.randint(0,800-80)
            elif abs(random_1[_] - random_1[_-1]) < 250:
                x = random.randint(0,800-80)
        delay = _ * 250
        green_rect = greenball.get_rect(topleft=(x,y)) 
        o = random.randint(9,13)
        if _ % int(o) == 0:
            beachballs.append({'rect': green_rect, 'timer': delay, 'type': 'green'})


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
crab_2 = pygame.image.load('characterimages/crab_1.png').convert_alpha()
crab_2_size = pygame.transform.scale(crab_2, (230, 230))  # Use convert_alpha for images with transparency

cage = pygame.image.load('characterimages/cage.png').convert_alpha()  # Use convert_alpha for images with transparency
crab_1 = pygame.image.load('characterimages/crab.png').convert_alpha()
crab_1 = pygame.transform.scale(crab_1, (230, 230))   # Use convert_alpha for images with transparency
beachball = pygame.image.load('characterimages/beachball.png').convert_alpha()  # Use convert_alpha for images with transparency
beachball = pygame.transform.scale(beachball, (160, 160)) 

cage = pygame.transform.scale(cage,(200, 200))  
beachball_xpos = 0 #initialize
beachball_ypos = random.randint(0, 800 - 50)  

crabwalk_frames = [crab_1, crab_2_size]
crab_ind = 0
crab = pygame.transform.scale(crabwalk_frames[crab_ind], (230, 230))
player_rect = crab.get_rect(topleft=(280, 400))
redball=pygame.image.load('characterimages/redball.png').convert_alpha()  # Use convert_alpha for images with transparency
blueball=pygame.image.load('characterimages/blueball.png').convert_alpha()  # Use convert_alpha for images with transparency
greenball=pygame.image.load('characterimages/greenball.png').convert_alpha()
redball = pygame.transform.scale(redball,(160,160))
blueball = pygame.transform.scale(blueball, (160,160))
greenball = pygame.transform.scale(greenball, (160,160))  # Use convert_alpha for images with transparency
  # Initialize cage_rect

  # Center the score text at the bottom of the screen

text_rect = text_surface.get_rect(center=(400, 100))  # Center the text at the top of the screen
player_gravity = 0  # Gravity for the crab
beachballs = []
random_1 = []
player_speed = 10  # Speed of the crab
score = 0

game_active = False  # Game starts on the start screen
game_over = False
speed_boost = False
speed_slow = False
greenused = False
blueused= False

while True:
    
    for event in pygame.event.get(): #checks for all possible events
        if event.type == pygame.QUIT: #if quit then quit
            pygame.quit() #closes the window
            exit() #exits the program
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_active = True
                game_over = False
                score = 0
                player_rect.topleft = (280, 400)
                player_gravity = 0
                setup_beachballs()
            if event.key == pygame.K_UP and player_rect.bottom >= 800:
                player_gravity = -20  # Only jump when UP is pressed, not held
    
    if game_active == False and game_over == False:
        score = 0
        player_rect.topleft = (280, 400)
        beachballs.clear()
        screen.fill("#ffcc33")
        text_surface_1 = font.render('Beach Blitz', True, '#000000')
        screen.blit(text_surface_1, (250, 100))
        start_text = font.render('Press Space to Start', True, '#000000')
        start_text_rect = start_text.get_rect(center=(400, 400))
        screen.blit(start_text, start_text_rect)
    keys = pygame.key.get_pressed()
    if event.type == pygame.K_SPACE:
        game_active = True


    
    
    keys = pygame.key.get_pressed()
    if speed_boost:
        player_speed = 30
        if pygame.time.get_ticks() - speed_boost_timer > 2000:
            speed_boost = False
            player_speed = 10
    elif speed_slow:
        player_speed=1
        if pygame.time.get_ticks() - speed_slow_timer > 2000:
            speed_slow = False
            player_speed = 10
    else:
        player_speed = 10
    if keys[pygame.K_LEFT] and player_rect.left > 0:
        crabwalk()
        player_rect.x -= player_speed 
    if keys[pygame.K_RIGHT] and player_rect.right < 800:
        crabwalk()
        player_rect.x += player_speed

    player_gravity += 1
    player_rect.y += player_gravity

   #prevents crb from falling
    if player_rect.bottom >= 800:
        player_rect.bottom = 800
        player_gravity = 0
    if game_active == True:
        
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
                elif ball['type'] == 'red':
                   screen.blit(redball,ball['rect'])
                elif ball['type'] == 'blue':
                   
                    screen.blit(blueball, ball['rect']) 
                elif ball['type'] == 'green':
                  
                    screen.blit(greenball, ball['rect'])
                else:
                   screen.blit(beachball, ball['rect'])

            if ball['rect'].y > 800:
                ball['rect'].y = 0
                ball['rect'].x = random.randint(0, 800 - 80)
                ball['timer'] = random.randint(0, 100)  # Reset timer to a random value
                   
            if player_rect.colliderect(ball['rect']):
                if ball['type'] == 'cage':
                    x=random.randint(0,800-80)
                    y=0
                    delay = 150  # Random delay for the new cage
                   #cage_rect = cage.get_rect(topleft=(x,y)) 

                   #beachballs.append({'rect': cage_rect, 'timer': delay, 'type': 'cage'})
                    game_over =False#changelater
                    
                elif ball['type'] == 'beachball':   
                    beachballs.remove(ball) #add sound later
                    
                    score += 1
                    score_surface = font.render(f"Score: {score}", True, "#ffcc33")
                    screen.blit(score_surface, (20, 20))
                    x = random.randint(0, 800 - 80)
                    y = 0
                
                    delay = 150  # Random delay for the new beachball
                    beachball_rect = beachball.get_rect(topleft=(x,y))
                    beachballs.append({'rect': beachball_rect, 'timer': delay, 'type': 'beachball'})
                elif ball['type'] == 'red':
                    beachballs.remove(ball)
                    score +=10
                    score_surface = font.render(f"Score: {score}", True, "#ffcc33")
                    screen.blit(score_surface, (20, 20))
                    x=random.randint(0,800-80)
                    y =0
                    delay=300
                    red_rect = redball.get_rect(topleft=(x,y))
                    beachballs.append({'rect': red_rect, 'timer': delay, 'type': 'red'})
                elif ball['type'] == 'blue':
                    
                    if not speed_boost and not speed_slow:
                        beachballs.remove(ball)
                        speed_boost = True
                        speed_boost_timer = pygame.time.get_ticks()
                        score += 5
                        y=0
                        x=random.randint(0,800-80)
                        delay=300
                        blue_rect = blueball.get_rect(topleft=(x,y))
                        beachballs.append({'rect':blue_rect, 'timer':delay, 'type': 'blue'})
                    else:
                        beachballs.remove(ball)
                elif ball['type'] == 'green':
                    
                    if not speed_slow and not speed_boost:
                        beachballs.remove(ball)
                        score+=1
                        speed_slow = True
                        speed_slow_timer = pygame.time.get_ticks()
                        x = random.randint(0,800-80)
                        y = 0
                        delay = 300
                        green_rect = greenball.get_rect(topleft=(x,y))
                        beachballs.append({'rect':green_rect, 'timer':delay, 'type': 'green'})
                    else:
                        beachballs.remove(ball)

                    
    if game_over == True:
        score_final = score
        screen.fill("#ffcc33")
        
        game_over_surface = font.render("Game Over", True, "#000000")
        game_over_surface_rect = game_over_surface.get_rect(center=(400, 300))

        game_over_score = font.render(f"Your Score: {score_final}", True, "#000000")
        game_over_score_rect = game_over_score.get_rect(center=(400, 400))
        screen.blit(game_over_surface, game_over_surface_rect)
        screen.blit(game_over_score, game_over_score_rect)

    pygame.display.update()
    clock.tick(60)

