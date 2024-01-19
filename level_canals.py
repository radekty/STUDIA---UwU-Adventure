import pygame
from pygame.locals import *

def run_canals_level(screen):
    question = "What is the sum of the digits found in the picture?"
    answer = "39"
    
    input_text = ""
    
    while True:
        screen.fill((255, 255, 255))

        background_image = pygame.image.load("background_canals.jpg")
        screen.blit(background_image, (0, 0))

        font = pygame.font.Font(None, 36)
        draw_text = lambda text, x, y, color=(255, 0, 0): screen.blit(font.render(text, True, color), (x, y))

        draw_text(question, 100, 0)
        draw_text("Sum of the digits:", 250, 575)
        draw_text(input_text, 470, 575)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    if input_text == answer:
                        return True
                elif event.key == K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode