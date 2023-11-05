import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((1000, 800))  # Increased screen size

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create a clock object to control the frame rate
clock = pygame.time.Clock()

# Define board layout (example)
board_layout = [
    'START', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    '10', '11', '12', '13', '14', '15', '16', '17', '18', 'FINIŠ'
]

def draw_board():
    for i, space in enumerate(board_layout):
        x = 30 + (i % 10) * 80  # Increased tile size and spacing
        y = 30 + (i // 10) * 80  # Increased tile size and spacing
        pygame.draw.rect(screen, BLACK, (x, y, 60, 60), 3)  # Added outline (3rd argument sets border width)
        font = pygame.font.Font(None, 24)
        text = font.render(space, True, BLACK)
        screen.blit(text, (x + 15, y + 15))

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(WHITE)  # Clear the screen

        draw_board()

        pygame.display.flip()  # Update the display

        clock.tick(60)  # Cap the frame rate at 60 FPS

if __name__ == "__main__":
    main()
