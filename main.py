import pygame
from sys import exit
import random
import asyncio

async def main():
    global crab, crab_ind, crabwalk_frames, original_crabwalk_frames
    pygame.init()
    #
    screen = pygame.display.set_mode((800, 800), pygame.SCALED)
    pygame.display.set_caption("Beach Blitz")
    clock = pygame.time.Clock()
    font = pygame.font.Font('./textfont/Pixel-regular.ttf', 50)

    # --- First-click requirement (black screen, white centered text) ---
    screen.fill((0, 0, 0))
    start_text = font.render("CLICK ANYWHERE TO START", True, (255, 255, 255))
    start_text_rect = start_text.get_rect(center=(400, 400))  # Centered on 800x800 screen
    screen.blit(start_text, start_text_rect)
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                waiting = False
        await asyncio.sleep(0)  # Critical for pygbag

    # --- Asset loading with explicit paths ---
    test_surface = pygame.image.load('./graphicsbg/background.png')
    crab_2 = pygame.image.load('./characterimages/crab_1.png').convert_alpha()
    crab_2 = pygame.transform.scale(crab_2, (230, 230))
    cage = pygame.image.load('./characterimages/cage.png').convert_alpha()
    crab_1 = pygame.image.load('./characterimages/crab.png').convert_alpha()
    crab_1 = pygame.transform.scale(crab_1, (230, 230))
    beachball = pygame.image.load('./characterimages/beachball.png').convert_alpha()
    beachball = pygame.transform.scale(beachball, (160, 160))
    cage = pygame.transform.scale(cage, (200, 200))
    redball = pygame.image.load('./characterimages/redball.png').convert_alpha()
    blueball = pygame.image.load('./characterimages/blueball.png').convert_alpha()
    greenball = pygame.image.load('./characterimages/greenball.png').convert_alpha()
    redball = pygame.transform.scale(redball, (160, 160))
    blueball = pygame.transform.scale(blueball, (160, 160))
    greenball = pygame.transform.scale(greenball, (160, 160))
    bluegreen_crab = pygame.image.load('./characterimages/bluegreen.png').convert_alpha()
    bluegreen_crab = pygame.transform.scale(bluegreen_crab, (230, 230))
    bluegreen_crab_1 = pygame.image.load('./characterimages/bluegreen_1.png').convert_alpha()
    bluegreen_crab_1 = pygame.transform.scale(bluegreen_crab_1, (230, 230))


    def crabwalk():
        global crab, crab_ind,crab_1,crab_2_size
        
        crab_ind+=0.1
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
            delay = _ * 40
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
            o = random.randint(4,8)
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
    crab_2 = pygame.transform.scale(crab_2, (230, 230))  

    cage = pygame.image.load('characterimages/cage.png').convert_alpha()  
    crab_1 = pygame.image.load('characterimages/crab.png').convert_alpha()
    crab_1 = pygame.transform.scale(crab_1, (230, 230))   
    beachball = pygame.image.load('characterimages/beachball.png').convert_alpha()  
    beachball = pygame.transform.scale(beachball, (160, 160)) 

    cage = pygame.transform.scale(cage,(200, 200))  
    beachball_xpos = 0 #initialize
    beachball_ypos = random.randint(0, 800 - 50)  

    original_crabwalk_frames = [crab_1, crab_2]
    crabwalk_frames = original_crabwalk_frames.copy()
    crab_ind = 0
    crab = pygame.transform.scale(crabwalk_frames[crab_ind], (230, 230))
    player_rect = crab.get_rect(topleft=(280, 400))
    redball=pygame.image.load('characterimages/redball.png').convert_alpha()  
    blueball=pygame.image.load('characterimages/blueball.png').convert_alpha()  
    greenball=pygame.image.load('characterimages/greenball.png').convert_alpha()
    redball = pygame.transform.scale(redball,(160,160))
    blueball = pygame.transform.scale(blueball, (160,160))
    greenball = pygame.transform.scale(greenball, (160,160))  
    bluegreen_crab = pygame.image.load('characterimages/bluegreen.png').convert_alpha()
    bluegreen_crab = pygame.transform.scale(bluegreen_crab, (230,230))
    bluegreen_crab_1 = pygame.image.load('characterimages/bluegreen_1.png').convert_alpha()
    bluegreen_crab_1 = pygame.transform.scale(bluegreen_crab_1, (230,230))


    text_rect = text_surface.get_rect(center=(400, 100))  
    player_gravity = 0  
    beachballs = []
    random_1 = []
    player_speed = 10 
    score = 0

    game_active = False  
    game_over = False
    speed_boost = False
    speed_slow = False
    greencollected = False
    bluecollected = False
    bluegreen_powerup = False
    bluegreen_powerup_timer = 0

    powerup_ready_time = 0
    crab_ind = 0
    specialcollect = 0
    showboostpowerup = False
    showslowpowerup = False
    showbgpowerup = False
    showboostpowerup = False
    showslowpowerup = False
    showbgpowerup = False
    speed_boost = False
    speed_slow = False
    bluegreen_powerup = False
    screen.fill((0, 0, 0))

    while True:

        pygame.time.get_ticks() 

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
                    powerup_ready_time = pygame.time.get_ticks() + random.randint(30000, 90000)  # e.g. 30-90 seconds
                    showboostpowerup = False
                    showslowpowerup = False
                    showbgpowerup = False
                    speed_boost = False
                    speed_slow = False
                    bluegreen_powerup = False

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
        
        if bluegreen_powerup == True:
            specialcollect = 0
        
            player_speed = 35
            crab = bluegreen_crab
            if pygame.time.get_ticks() - bluegreen_powerup_timer > 5000:
                bluegreen_powerup = False
                showbgpowerup = False
                showboostpowerup = False      # <-- add this
                showslowpowerup = False       # <-- add this
                player_speed = 10
                crabwalk_frames = original_crabwalk_frames.copy()
                crab = crabwalk_frames[int(crab_ind)]
        elif speed_boost:
            
            player_speed = 20
            crab = crabwalk_frames[int(crab_ind)]
            if pygame.time.get_ticks() - speed_boost_timer > 2000:
                speed_boost = False
                showboostpowerup = False
                showbgpowerup = False
                showboostpowerup = False      # <-- add this
                showslowpowerup = False
                player_speed = 10
        elif speed_slow:
            
            player_speed=1
            crab = crabwalk_frames[int(crab_ind)]
            if pygame.time.get_ticks() - speed_slow_timer > 2000:
                speed_slow = False
                showslowpowerup = False
                showbgpowerup = False
                showboostpowerup = False      # <-- add this
                showslowpowerup = False    
                player_speed = 10
        else:
            player_speed = 10
            crab = crabwalk_frames[int(crab_ind)]

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
        if game_active == True and not game_over:
        
            screen.blit(test_surface, (0, 0))  # center the image
            screen.blit(text_surface, text_rect)
            score_surface = font.render(f"Score: {score}", True, "#ffcc33")
            screen.blit(score_surface, (20, 20))
            screen.blit(crab, player_rect)
            if showboostpowerup == True:
                symbol = font.render("Speed Boost Active!", True, "#ffcc33")
                try:
                    icon = pygame.image.load('characterimages/powerup.png').convert_alpha()
                except pygame.error as e:
                    print(f"Error loading powerup icon: {e}")
                icon = pygame.transform.scale(icon, (100, 100))
            
                screen.blit(icon, (20, 150))
                
            

            elif showslowpowerup == True:
                symbol = font.render("Speed Slow Powerup Active!", True, "#ffcc33")
                try:
                    icon = pygame.image.load('characterimages/slowdown.png').convert_alpha()
                except pygame.error as e:
                    print(f"Error loading slowdown icon: {e}")
                icon = pygame.transform.scale(icon, (100, 100))
                
                screen.blit(icon, (20, 150))
                
            elif showbgpowerup == True:
                symbol = font.render("Blue-Green Powerup Active!", True, "#ffcc33")
                try:
                    icon = pygame.image.load('characterimages/bgpowerup.png').convert_alpha()
                except pygame.error as e:
                    print(f"Error loading bgpowerup icon: {e}")
                icon = pygame.transform.scale(icon, (100, 100))
                
                screen.blit(icon, (20, 150))
            
            
            for ball in beachballs[:]:
                
                
                if ball['timer'] > 0:
                    ball['timer'] -= 1
                else:
                    ball['rect'].y += 6

                    if ball['type'] == 'cage':
                        screen.blit(cage, ball['rect'])
                    elif ball['type'] == 'red':
                        screen.blit(redball, ball['rect'])
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
                       
                        if ball['rect'].y < 600:
                            x = random.randint(0, 800-80)
                            y = 0
                            delay = 150
                            cage_rect = cage.get_rect(topleft=(x, y))
                            beachballs.append({'rect': cage_rect, 'timer': delay, 'type': 'cage'})
                            game_over = True
                            break
                        #

                    elif ball['type'] == 'beachball':
                        beachballs.remove(ball)  # add sound later

                        score += 1
                        score_surface = font.render(f"Score: {score}", True, "#ffcc33")
                        screen.blit(score_surface, (20, 20))
                        x = random.randint(0, 800 - 80)
                        y = 0
                    
                        delay = 40  # Random delay for the new beachball
                        beachball_rect = beachball.get_rect(topleft=(x,y))
                        beachballs.append({'rect': beachball_rect, 'timer': delay, 'type': 'beachball'})
                    elif ball['type'] == 'red':
                        redcollected = True
                        beachballs.remove(ball)
                        score +=15
                        score_surface = font.render(f"Score: {score}", True, "#ffcc33")
                        screen.blit(score_surface, (20, 20))
                        x=random.randint(0,800-80)
                        y =0
                        delay=300
                        red_rect = redball.get_rect(topleft=(x,y))
                        beachballs.append({'rect': red_rect, 'timer': delay, 'type': 'red'})
                    elif ball['type'] == 'blue':
                        specialcollect += 1
                        bluecollected = True
                        showboostpowerup = True
                        if greencollected and bluecollected and specialcollect >= 4: #and pygame.time.get_ticks() >= powerup_ready_time:
                            bluegreen_powerup = True
                            showboostpowerup = False
                            showslowpowerup = False
                            showbgpowerup = True
                            bluegreen_powerup_timer = pygame.time.get_ticks()
                            speed_boost = False
                            speed_slow = False
                            greencollected = False
                            bluecollected = False
                            crabwalk_frames = [bluegreen_crab, bluegreen_crab_1]
                        if not speed_boost and not speed_slow:
                            beachballs.remove(ball)
                            score += 5
                            speed_boost = True
                            
                            speed_boost_timer = pygame.time.get_ticks()
                            y=0
                            x=random.randint(0,800-80)
                            delay=300
                            blue_rect = blueball.get_rect(topleft=(x,y))
                            beachballs.append({'rect':blue_rect, 'timer':delay, 'type': 'blue'})
                        else:
                            beachballs.remove(ball)
                    elif ball['type'] == 'green':
                        greencollected = True
                        specialcollect += 1
                        showslowpowerup = True
                        if greencollected and bluecollected and specialcollect >= 4: #and pygame.time.get_ticks() >= powerup_ready_time:
                                bluegreen_powerup = True
                                showbgpowerup = True
                                showboostpowerup = False
                                showslowpowerup = False
                                bluegreen_powerup_timer = pygame.time.get_ticks()
                                speed_boost = False
                                speed_slow = False
                                bluecollected = False
                                greencollected = False
                                crabwalk_frames = [bluegreen_crab, bluegreen_crab_1]
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
            
            
            crabwalk_frames = original_crabwalk_frames.copy()
            crab = crabwalk_frames[0]
            
            game_over_surface = font.render("Game Over", True, "#000000")
            game_over_surface_rect = game_over_surface.get_rect(center=(400, 300))

            game_over_score = font.render(f"Your Score: {score_final}", True, "#000000")
            game_over_score_rect = game_over_score.get_rect(center=(400, 400))
            screen.blit(game_over_surface, game_over_surface_rect)
            screen.blit(game_over_score, game_over_score_rect)

        
        pygame.display.update()
        clock.tick(60)
        await asyncio.sleep(0)  # Yield control to browser/event loop


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())