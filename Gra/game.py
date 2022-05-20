from cgi import test
from cmath import rect
import pygame
from sys import exit

def display_score():
    current_time = pygame.time.get_ticks() - start_time
    score_surf = test_font.render(f'{current_time}', False, 'White')
    score_rect = score_surf.get_rect(center = (500, 70))
    screen.blit(score_surf,score_rect)


pygame.init()
screen = pygame.display.set_mode((800,400)) # w ,h 
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50) # type font, size
game_active = True
start_time = 0

#Design
background_surface = pygame.Surface((800,800))
background_surface.fill('Black')

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
reset_text_rect = reset_text_surf.get_rect(center = (400, 140))

#Enemy
snail_surface = pygame.image.load('grafika\\snail.png').convert_alpha()
snail_rect = snail_surface.get_rect(bottomright = (700,300))

#Player
player_surf = pygame.Surface((50,100))
player_surf.fill('Red')
player_rect = player_surf.get_rect(midbottom = (80,300))
player_gravity = 0

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
                start_time = pygame.time.get_ticks()

    
    if game_active:  
        #'Render'  
        #Kolejnosc deklarowania elementow jest bardzo wazna i trzeba byc precyzyjnym
        screen.blit(background_surface,(0,0))
        screen.blit(sky_surface,(0,0)) # x , y
        screen.blit(ground_surface,(0,300))
        pygame.draw.rect(screen, 'Pink', score_text_rect)
        pygame.draw.rect(screen, 'Pink', score_text_rect, 10)
        screen.blit(score_text_surf,score_text_rect)
        display_score()

        #Enemy attributes (Movement)
        snail_rect.x -= 6
        if snail_rect.right <= 0: snail_rect.left = 800
        screen.blit(snail_surface,snail_rect)

        #Player attributes
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300: player_rect.bottom = 300
        screen.blit(player_surf,player_rect)

        #Collision
        if snail_rect.colliderect(player_rect):
            game_active = False

    else:
        screen.fill('Yellow')
        screen.blit(game_over_surf,game_over_rect)
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