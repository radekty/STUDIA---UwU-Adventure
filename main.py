import pygame
import sys
from pygame.locals import *
from menu_screen import run_menu_screen
from level_canals import run_canals_level
from level_bridge import run_bridge_level
from level_city import run_city_level
from thanks_screen import run_thanks_screen

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("UwU Adventure")

bg_color = (255, 255, 255)

# Add a state variable
current_state = "menu"

def main():
    global current_state
    
    while True:
        screen.fill(bg_color)

        # Use a conditional statement to determine what should be drawn and handled in the current state
        if current_state == "menu":
            run_menu_screen(screen)
        elif current_state == "canals":
            if run_canals_level(screen):
                print("Congratulations! You are progressing to the next level.")
                current_state = "bridge"
        elif current_state == "bridge":
            if run_bridge_level(screen):
                print("Congratulations! You are progressing to the next level.")
                current_state = "city"
        elif current_state == "city":
            if run_city_level(screen):
                print("Congratulations! You are progressing to the next level.")
                current_state = "thanks"
        elif current_state == "thanks":
            run_thanks_screen(screen)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                # Add handling for changing the game state when specific keys are pressed
                if event.key == K_1:
                    current_state = "canals"
                elif event.key == K_2:
                    current_state = "bridge"
                elif event.key == K_3:
                    current_state = "city"
                elif event.key == K_q:
                    current_state = "thanks"

if __name__ == "__main__":
    main()