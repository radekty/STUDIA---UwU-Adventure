import pygame
from pygame.locals import *

def run_city_level(screen):
    question = "How many more men than women are there?"
    answer = "3"

    input_text = ""

    while True:
        screen.fill((255, 255, 255))

        background_image = pygame.image.load("background_city.jpg")
        screen.blit(background_image, (0, 0))

        font = pygame.font.Font(None, 36)
        draw_text = lambda text, x, y, color=(255, 0, 0): screen.blit(font.render(text, True, color), (x, y))

        draw_text(question, 150, 0)
        draw_text("Difference:", 300, 575)
        draw_text(input_text, 440, 575)
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