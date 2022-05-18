from cgi import test
from cmath import rect
import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400)) # w ,h 
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50) # type font, size

background_surface = pygame.Surface((800,800))
background_surface.fill('Black')

sky_surface = pygame.Surface((800,50))
sky_surface.fill('Blue')
#ladowanie obrazu: pygame.image.load('sciezka obrazu')
ground_surface = pygame.Surface((800,100))
ground_surface.fill('Green')

text_surface = test_font.render('My game', False, 'Brown')

snail_surface = pygame.image.load('grafika\\snail.png').convert_alpha()
snail_rect = snail_surface.get_rect(bottomright = (700,300))

player_surf = pygame.Surface((50,100))
player_surf.fill('Red')
player_rect = player_surf.get_rect(midbottom = (80,300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    #Kolejnosc deklarowania elementow jest bardzo wazna i trzeba byc precyzyjnym
    screen.blit(background_surface,(0,0))
    screen.blit(sky_surface,(0,0)) # x , y
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface,(300,50))

    snail_rect.x -= 4
    if snail_rect.right <= 0: snail_rect.left = 800
    screen.blit(snail_surface,snail_rect) 
    screen.blit(player_surf,player_rect)

    #if player_rect.colliderect(snail_rect): YT: 1:10:34
        

    pygame.display.update()
    clock.tick(60)