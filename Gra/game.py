from cgi import test
from cmath import rect
import pygame
from sys import exit
from random import randint

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = test_font.render(f'{current_time}', False, 'White')
    score_rect = score_surf.get_rect(center = (500, 70))
    screen.blit(score_surf,score_rect)
    return current_time

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 7

            if obstacle_rect.bottom == 300: screen.blit(hound_surf,obstacle_rect)

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]

        return obstacle_list
    else: return[]

def collisions(player,obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect): return False
    return True

def player_animation():
    global player_surf, player_index
    if player_rect.bottom < 300:
        player_surf = player_walk0
    else:
        player_index += 0.2
        if player_index >= len(player_walk):player_index = 0
        player_surf = player_walk[int(player_index)]

pygame.init()
screen = pygame.display.set_mode((800,400)) # w ,h 
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50) # type font, size
game_active = False
start_time = 0
score = 0

#Design
background_surface = pygame.Surface((800,800))
background_surface.fill('Violet')

sky_surface = pygame.Surface((800,50))
sky_surface.fill('Blue')

ground_surface = pygame.Surface((800,100))
ground_surface.fill('Green')

#Text
score_text_surf = test_font.render('Score:', False, 'Brown')
score_text_rect = score_text_surf.get_rect(center = (300, 70))

game_over_surf = test_font.render('Game Over',False,'Brown')
game_over_rect = game_over_surf.get_rect(center = (400, 70))

reset_text_surf = test_font.render('Press SPACEBAR to play again',False,'Brown')
reset_text_rect = reset_text_surf.get_rect(center = (400, 210))

#Enemy
hound_frame0 = pygame.image.load('grafika\\Hound\\Hound_Move0000.png').convert_alpha()
hound_frame0 = pygame.transform.scale(hound_frame0, (70,40))
hound_frame1 = pygame.image.load('grafika\\Hound\\Hound_Move0001.png').convert_alpha()
hound_frame1 = pygame.transform.scale(hound_frame1, (70,40))
hound_frame2 = pygame.image.load('grafika\\Hound\\Hound_Move0002.png').convert_alpha()
hound_frame2 = pygame.transform.scale(hound_frame2, (70,40))
hound_frame3 = pygame.image.load('grafika\\Hound\\Hound_Move0003.png').convert_alpha()
hound_frame3 = pygame.transform.scale(hound_frame3, (70,40))
hound_frame4 = pygame.image.load('grafika\\Hound\\Hound_Move0004.png').convert_alpha()
hound_frame4 = pygame.transform.scale(hound_frame4, (70,40))
hound_frame5 = pygame.image.load('grafika\\Hound\\Hound_Move0005.png').convert_alpha()
hound_frame5 = pygame.transform.scale(hound_frame5, (70,40))
hound_frame6 = pygame.image.load('grafika\\Hound\\Hound_Move0006.png').convert_alpha()
hound_frame6 = pygame.transform.scale(hound_frame6, (70,40))
hound_frame7 = pygame.image.load('grafika\\Hound\\Hound_Move0007.png').convert_alpha()
hound_frame7 = pygame.transform.scale(hound_frame7, (70,40))
hound_frame8 = pygame.image.load('grafika\\Hound\\Hound_Move0008.png').convert_alpha()
hound_frame8 = pygame.transform.scale(hound_frame8, (70,40))
hound_frame9 = pygame.image.load('grafika\\Hound\\Hound_Move0009.png').convert_alpha()
hound_frame9 = pygame.transform.scale(hound_frame9, (70,40))
hound_frame10 = pygame.image.load('grafika\\Hound\\Hound_Move0010.png').convert_alpha()
hound_frame10 = pygame.transform.scale(hound_frame10, (70,40))
hound_frame11 = pygame.image.load('grafika\\Hound\\Hound_Move0011.png').convert_alpha()
hound_frame11 = pygame.transform.scale(hound_frame11, (70,40))
hound_frame12 = pygame.image.load('grafika\\Hound\\Hound_Move0012.png').convert_alpha()
hound_frame12 = pygame.transform.scale(hound_frame12, (70,40))
hound_frame13 = pygame.image.load('grafika\\Hound\\Hound_Move0013.png').convert_alpha()
hound_frame13 = pygame.transform.scale(hound_frame13, (70,40))
hound_frame14 = pygame.image.load('grafika\\Hound\\Hound_Move0014.png').convert_alpha()
hound_frame14 = pygame.transform.scale(hound_frame14, (70,40))
hound_frame15 = pygame.image.load('grafika\\Hound\\Hound_Move0015.png').convert_alpha()
hound_frame15 = pygame.transform.scale(hound_frame15, (70,40))
hound_frames = [hound_frame0, hound_frame1, hound_frame2, hound_frame3, hound_frame4, hound_frame5, hound_frame6, hound_frame7, hound_frame8, hound_frame9, hound_frame10, hound_frame11, hound_frame12, hound_frame13, hound_frame14, hound_frame15]
hound_frame_index = 0
hound_surf = hound_frames[hound_frame_index]

obstacle_rect_list = []

#Player
#player_surf = pygame.Surface((50,100))
#player_surf.fill('Red')
player_walk0 = pygame.image.load('grafika\\Player\\Player_Move0000.png').convert_alpha()
player_walk0 = pygame.transform.scale(player_walk0, (50,80))
player_walk1 = pygame.image.load('grafika\\Player\\Player_Move0001.png').convert_alpha()
player_walk1 = pygame.transform.scale(player_walk1, (50,80))
player_walk2 = pygame.image.load('grafika\\Player\\Player_Move0002.png').convert_alpha()
player_walk2 = pygame.transform.scale(player_walk2, (50,80))
player_walk3 = pygame.image.load('grafika\\Player\\Player_Move0003.png').convert_alpha()
player_walk3 = pygame.transform.scale(player_walk3, (50,80))
player_walk = [player_walk0, player_walk1, player_walk2, player_walk3]
player_index = 0

player_surf = player_walk[player_index]
player_rect = player_surf.get_rect(midbottom = (80,300))
player_gravity = 0

#Timer
obstacle_timer = pygame.USEREVENT + 1 
pygame.time.set_timer(obstacle_timer,1500)

hound_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(hound_animation_timer,20)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300: 
                    player_gravity = -18
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -18
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                
                start_time = int(pygame.time.get_ticks() / 1000)

        if game_active:
            if event.type == obstacle_timer:
                obstacle_rect_list.append(hound_surf.get_rect(bottomright = (randint(900,1100),300)))
            if event.type == hound_animation_timer:
                if hound_frame_index == 0: hound_frame_index = 1
                elif hound_frame_index == 1: hound_frame_index = 2
                elif hound_frame_index == 2: hound_frame_index = 3
                elif hound_frame_index == 3: hound_frame_index = 4
                elif hound_frame_index == 4: hound_frame_index = 5
                elif hound_frame_index == 5: hound_frame_index = 6
                elif hound_frame_index == 6: hound_frame_index = 7
                elif hound_frame_index == 7: hound_frame_index = 8
                elif hound_frame_index == 8: hound_frame_index = 9
                elif hound_frame_index == 9: hound_frame_index = 10
                elif hound_frame_index == 10: hound_frame_index = 11
                elif hound_frame_index == 11: hound_frame_index = 12
                elif hound_frame_index == 12: hound_frame_index = 13
                elif hound_frame_index == 13: hound_frame_index = 14
                elif hound_frame_index == 14: hound_frame_index = 15
                else: hound_frame_index = 0
                hound_surf = hound_frames[hound_frame_index]
    
    if game_active:  
        #'Render'  
        #Kolejnosc deklarowania elementow jest bardzo wazna i trzeba byc precyzyjnym
        screen.blit(background_surface,(0,0))
        screen.blit(sky_surface,(0,0)) # x , y
        screen.blit(ground_surface,(0,300))
        pygame.draw.rect(screen, 'Pink', score_text_rect)
        pygame.draw.rect(screen, 'Pink', score_text_rect, 10)
        screen.blit(score_text_surf,score_text_rect)
        score = display_score()

        #Enemy attributes (Movement) old
        #hound_rect.x -= 6
        #if hound_rect.right <= 0: hound_rect.left = 800
        #screen.blit(hound_surface,hound_rect)


        #Player attributes
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300: player_rect.bottom = 300
        player_animation()
        screen.blit(player_surf,player_rect)

        #Obstacle movment
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)


        #Collision
        game_active = collisions(player_rect,obstacle_rect_list)

    else:
        screen.fill('Yellow')
        screen.blit(game_over_surf,game_over_rect)
        obstacle_rect_list.clear()
        player_rect.midbottom = (80,300)
        player_gravity = 0
        score_message = test_font.render(f'Your score: {score}', False, 'Brown')
        score_message_rect = score_message.get_rect(center = (400, 140))
        screen.blit(score_message,score_message_rect)
        screen.blit(reset_text_surf,reset_text_rect)
        
    #Other solutions
        #Jump
        #keys = pygame.key.get_pressed()
        #if keys[pygame.K_SPACE]:
        # player_gravity = -10

        #Mouse reaction
        #mouse_pos = pygame.mouse.get_pos()
        #if player_rect.collidepoint(mouse_pos):
        #   print('collision')
            

    pygame.display.update()
    clock.tick(60)