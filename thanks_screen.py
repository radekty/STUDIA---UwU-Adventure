import pygame
import sys
from pygame.locals import *

def run_thanks_screen(screen):
    bg_color = (255, 255, 255)

    screen.fill(bg_color)
    background_image = pygame.image.load("background_thanks.jpg")
    screen.blit(background_image, (0, 0))

    pygame.display.flip()

    pygame.time.delay(3000)
    pygame.quit()
    sys.exit()