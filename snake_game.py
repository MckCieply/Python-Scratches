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
