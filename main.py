import pygame
from constants import *

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Game loop
    while True:
        # Handle quit events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Draw the game onto the screen
        screen.fill((0, 0, 0))  # Fill screen with black
        pygame.display.flip()   # Refresh the screen

if __name__ == "__main__":
    main()

