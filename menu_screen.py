import pygame
from pygame.locals import *

def run_menu_screen(screen):
    font = pygame.font.Font(None, 36)
    draw_text = lambda text, x, y, color=(0, 0, 0): screen.blit(font.render(text, True, color), (x, y))

    background_image = pygame.image.load("background_menu.jpg")
    screen.blit(background_image, (0, 0))

    draw_text("1. In the canals", 300, 300, (255, 255, 0))
    draw_text("2. On the bridge", 300, 350, (255, 255, 0))
    draw_text("3. In the city", 300, 400, (255, 255, 0))
    draw_text("Press Q to exit", 300, 450, (255, 255, 0))

    pygame.display.flip()