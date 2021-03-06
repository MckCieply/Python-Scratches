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
    if change_to == "UP" and s_direction != "DOWN":
        s_direction = "UP"    
    if change_to == "DOWN" and s_direction != "UP":
        s_direction = "DOWN"
    if change_to == "LEFT" and s_direction != "RIGHT":
        s_direction = "LEFT"
    if change_to == "RIGHT" and s_direction != "LEFT":
        s_direction = "RIGHT"

    if s_direction == "UP":
        s_position[1] -= 10
    if s_direction == "DOWN":
        s_position[1] += 10
    if s_direction == "LEFT":
        s_position[0] -= 10
    if s_direction == "RIGHT":
        s_position[0] += 10

    s_body.insert(0, list(s_position))
    if s_position[0] == f_position[0] and s_position[1] == f_position[1]:
        score += 10
        f_spawn = False
    else:
        s_body.pop()
    if not f_spawn:
        f_position = [random.randrange(1, (window_x//10))* 10, random.randrange(1, (window_y//10))* 10]
    f_spawn = True
    window.fill(black)

    for pos in s_body:
        pygame.draw.rect(window, green, pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(window, white, pygame.Rect(f_position[0], f_position[1], 10, 10))

    if s_position[0] < 0 or s_position[0] > window_x - 10:
        game_over()
    if s_position[1] < 0 or s_position[1] > window_y - 10:
        game_over()
    for block in s_body[1:]:
        if s_position[0] == block[0] and s_position[1] == block[1]:
            game_over()
    show_score(1, white, 'times new roman', 20)

    pygame.display.update()
    fps.tick(s_speed)