import pygame
import time
import random

s_speed = 15
window_x = 720
window_y = 480

red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255,255,255)

pygame.init()
window = pygame.display.set_mode((window_x, window_y))            #?
fps = pygame.time.Clock()

s_position = [100,50]
s_body = [[100,50],[90,50],[80,50],[70,50]]
s_direction = 'RIGHT'
change_to = s_direction
f_position = [random.randrange(1, (window_x//10)) * 10, random.randrange(1, (window_y//10)) * 10]
f_spawn = True

score = 0
def show_score(choice, color, font, size):
    sc_font = pygame.font.SysFont(font, size)
    sc_surface = sc_font.render(f"Score: {str(score)}", True, color)
    sc_rect = sc_surface.get_rect()

    window.blit(sc_surface, sc_rect)

def game_over():
    font = pygame.font.SysFont('times new roman', 50)
    g_over_surface = font.render(f"Your score is: {str(score)}", True, red)
    g_over_rect = g_over_surface.get_rect()
    g_over_rect.midtop = (window_x/2, window_y/4)

    window.blit(g_over_surface, g_over_rect)
    pygame.display.flip()
    time.sleep(2)
    
    pygame.quit()
    quit()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = "UP"
            if event.key == pygame.K_DOWN:
                change_to = "DOWN"
            if event.key == pygame.K_LEFT:
                change_to = "LEFT"
            if event.key == pygame.K_RIGHT:
                change_to = "RIGHT"
    if change_to == "UP" and direction != "DOWN":
        direction = "UP"    
    if change_to == "DOWN" and direction != "UP":
        direction = "DOWN"
    if change_to == "LEFT" and direction != "RIGHT":
        direction = "LEFT"
    if change_to == "RIGHT" and direction != "LEFT":
        direction = "RIGHT"

    if direction == "UP":
        s_position[1] -= 10
    if direction == "DOWN":
        s_position[1] += 10
    if direction == "LEFT":
        s_position[0] -= 10
    if direction == "RIGHT":
        s_position[0] += 10