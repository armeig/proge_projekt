import pygame
import random
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
    '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', 'FINISH'
]

def draw_board(position):
    for i, space in enumerate(board_layout):
        x = 30 + (i % 11) * 80  # Adjusted tile size and spacing
        y = 30 + (i // 11) * 80  # Adjusted tile size and spacing
        pygame.draw.rect(screen, BLACK, (x, y, 60, 60), 3)  # Added outline (3rd argument sets border width)
        font = pygame.font.Font(None, 24)
        text = font.render(space, True, BLACK)
        screen.blit(text, (x + 5, y + 5))

def throw_dice():
    return random.randint(1, 6)

def display_message(message, y_offset=0):
    font = pygame.font.Font(None, 36)
    text = font.render(message, True, BLACK)
    text_rect = text.get_rect(center=(500, 400 + y_offset))
    screen.blit(text, text_rect)

def main():
    position = 0  # Initialize position to 0 (at START)
    dice_rolled = False
    game_won = False
    game_started = False
    welcome_screen = True

    try:
        while True:
            screen.fill(WHITE)  # Clear the screen

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if welcome_screen and event.type == pygame.MOUSEBUTTONDOWN:
                    welcome_screen = False
                    game_started = True  # Game officially starts after welcome screen is clicked

                if game_started and event.type == pygame.MOUSEBUTTONDOWN and not dice_rolled and not game_won:
                    steps = throw_dice()
                    print(f"You rolled a {steps}.")
                    position += steps
                    dice_rolled = True

            if welcome_screen:
                # Display welcome screen
                display_message("Joomasõbrad", y_offset=-50)
                display_message("Henri ja Grete", y_offset=0)
                display_message("Et mängu alustada vajuta mänguaknale", y_offset=50)
                pygame.display.flip()  # Update the display

            elif game_started:
                # Display game board and handle dice rolls as before
                draw_board(position)

                if dice_rolled:
                    pygame.draw.circle(screen, (0, 0, 255), (position % 11 * 80 + 50, position // 11 * 80 + 50), 10)
                    dice_rolled = False

                    if position >= len(board_layout) - 1:  # Check if player passes or lands on FINISH tile
                        game_won = True

                    pygame.display.flip()  # Update the display
                    pygame.time.delay(2000)  # Delay to slow down the game (in milliseconds)

                if game_won:
                    display_message("Palju õnne, oled võitnud")
                    pygame.display.flip()  # Update the display
                    pygame.time.delay(5000)  # Delay to display winning message for 5 seconds
                    pygame.quit()
                    sys.exit()

            clock.tick(60)  # Cap the frame rate at 60 FPS

    except KeyboardInterrupt:
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    main()
