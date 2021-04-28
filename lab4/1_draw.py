import pygame
from pygame.draw import *

pygame.init()

FPS = 30
colorbg = [48,213,200]
screen = pygame.display.set_mode((400, 400))
screen.fill(colorbg)
pygame.display.set_caption("My program")
pygame.display.flip()

circle(screen, (255, 255, 0), (200, 200),150)
circle(screen, (255, 0, 0), (125, 170),40)
circle(screen, (255, 0, 0), (275, 170),40)
circle(screen, (79, 0, 20), (125, 170),15)
circle(screen, (79, 0, 20), (275, 170),15)
rect(screen, (0, 0, 0), (120, 250, 150, 40))
line(screen,(0, 0, 0), [80, 80], [180, 120], 10)
line(screen,(0, 0, 0), [220, 120], [320, 80], 10)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
