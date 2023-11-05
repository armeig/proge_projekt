import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))

# Load the background image
background = pygame.image.load('board_background.jpg')  # Replace with your actual file name

# Create a clock object to control the frame rate
clock = pygame.time.Clock()

def throw_dice():
    return random.randint(1, 6)

def main():
    position = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        # Draw the background
        screen.blit(background, (0, 0))

        # Draw the player's position
        pygame.draw.circle(screen, (0, 0, 255), (position * 20 + 20, 300), 10)

        pygame.display.flip()  # Update the display

        pygame.time.delay(500)  # Delay to slow down the game (in milliseconds)

        steps = throw_dice()
        print(f"You rolled a {steps}.")

        position += steps

        if position >= 40:
            print("Congratulations! You've reached the end of the board.")
            break

        clock.tick(60)  # Cap the frame rate at 60 FPS

if __name__ == "__main__":
    main()
