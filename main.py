import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()  # Create a Clock object
    dt = 0  # Delta time variable

    # Instantiate the Player in the middle of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Create updatable and drawable groups
    updatables = [player]
    drawables = [player]

    # Game loop
    while True:
        # Handle quit events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Draw the game onto the screen
        screen.fill((0, 0, 0))  # Fill screen with black

        # Update all updatables
        for obj in updatables:
            obj.update(dt)

        # Draw all drawables
        for obj in drawables:
            obj.draw(screen)

        pygame.display.flip()   # Refresh the screen

        # Pause to maintain 60 FPS and update dt
        dt = clock.tick(60) / 1000  # Convert milliseconds to seconds

if __name__ == "__main__":
    main()

