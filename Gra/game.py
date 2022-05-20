from cgi import test
from cmath import rect
import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400)) # w ,h 
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50) # type font, size
game_active = True

#Design
background_surface = pygame.Surface((800,800))
background_surface.fill('Black')

sky_surface = pygame.Surface((800,50))
sky_surface.fill('Blue')

ground_surface = pygame.Surface((800,100))
ground_surface.fill('Green')

#Text
score_surf = test_font.render('Score:', False, 'Brown')
score_rect = score_surf.get_rect(center = (400, 70))

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
        
        if player_rect.bottom == 300 :
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos): 
                    player_gravity = -20
        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player_gravity = -20
    
    if game_active:  
        #'Render'  
        #Kolejnosc deklarowania elementow jest bardzo wazna i trzeba byc precyzyjnym
        screen.blit(background_surface,(0,0))
        screen.blit(sky_surface,(0,0)) # x , y
        screen.blit(ground_surface,(0,300))
        pygame.draw.rect(screen, 'Pink', score_rect)
        pygame.draw.rect(screen, 'Pink', score_rect, 10)
        screen.blit(score_surf,score_rect)

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
    #Kontent do dokonczenia YT: 1:52:30
    else:
        screen.fill('Yellow')
        
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