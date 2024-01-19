import sys
import pygame
from pygame.locals import *

def run_bridge_level(screen):
    question = "Which car color is most common?"
    options = ["Red", "Yellow", "Black", "Silver"]
    correct_answer = "Red"

    selected_option = None

    while True:
        screen.fill((255, 255, 255))

        background_image = pygame.image.load("background_bridge.jpg")
        screen.blit(background_image, (0, 0))

        font = pygame.font.Font(None, 36)
        draw_text = lambda text, x, y, color=(255, 0, 0): screen.blit(font.render(text, True, color), (x, y))

        draw_text(question, 200, 0)

        for i, option in enumerate(options):
            color = (0, 0, 255) if option == selected_option else (0, 0, 0)
            draw_text(option, 50, 400 + i * 50, color)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_DOWN:
                    if selected_option is None:
                        selected_option = options[0]
                    else:
                        index = options.index(selected_option)
                        if index < len(options) - 1:
                            selected_option = options[index + 1]
                elif event.key == K_UP:
                    if selected_option is None:
                        selected_option = options[-1]
                    else:
                        index = options.index(selected_option)
                        if index > 0:
                            selected_option = options[index - 1]
                elif event.key == K_RETURN:
                    if selected_option == correct_answer:
                        return True