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
            obstacle_rect.x -= 6

            if obstacle_rect.bottom == 300: screen.blit(snail_surface,obstacle_rect)

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
snail_surface = pygame.image.load('grafika\\snail.png').convert_alpha()
snail_rect = snail_surface.get_rect(bottomright = (600,300))

obstacle_rect_list = []

#Player
#player_surf = pygame.Surface((50,100))
#player_surf.fill('Red')
player_walk0 = pygame.image.load('grafika\\Player_Move0000.png').convert_alpha()
player_walk0 = pygame.transform.scale(player_walk0, (50,80))
player_walk1 = pygame.image.load('grafika\\Player_Move0001.png').convert_alpha()
player_walk1 = pygame.transform.scale(player_walk1, (50,80))
player_walk2 = pygame.image.load('grafika\\Player_Move0002.png').convert_alpha()
player_walk2 = pygame.transform.scale(player_walk2, (50,80))
player_walk3 = pygame.image.load('grafika\\Player_Move0003.png').convert_alpha()
player_walk3 = pygame.transform.scale(player_walk3, (50,80))
player_walk = [player_walk0, player_walk1, player_walk2, player_walk3]
player_index = 0

player_surf = player_walk[player_index]
player_rect = player_surf.get_rect(midbottom = (80,300))
player_gravity = 0

#Timer
obstacle_timer = pygame.USEREVENT + 1 
pygame.time.set_timer(obstacle_timer,1500)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300: 
                    player_gravity = -20
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect.left = 700
                start_time = int(pygame.time.get_ticks() / 1000)

        if event.type == obstacle_timer and game_active:
            obstacle_rect_list.append(snail_surface.get_rect(bottomright = (randint(900,1100),300)))

    
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
        #snail_rect.x -= 6
        #if snail_rect.right <= 0: snail_rect.left = 800
        #screen.blit(snail_surface,snail_rect)

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