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
    'START', '2', '3', '4', '5', '6', '7', '8', '9',
    '10', '11', '12', '13', '14', '15', '16', '17', '18', 'FINISH'
]

def draw_board(positions):
    for i, space in enumerate(board_layout):
        x = 30 + (i % 9) * 80  # Adjusted tile size and spacing
        y = 30 + (i // 9) * 80  # Adjusted tile size and spacing
        pygame.draw.rect(screen, BLACK, (x, y, 60, 60), 3)  # Added outline (3rd argument sets border width)
        font = pygame.font.Font(None, 24)
        text = font.render(space, True, BLACK)
        screen.blit(text, (x + 5, y + 5))

def throw_dice():
    return random.randint(1, 6)

def display_message(message):
    font = pygame.font.Font(None, 36)
    text = font.render(message, True, BLACK)
    text_rect = text.get_rect(center=(500, 400))
    screen.blit(text, text_rect)

def show_welcome_screen():
    screen.fill(WHITE)
    font = pygame.font.Font(None, 72)
    text1 = font.render("Joomasõbrad", True, BLACK)
    text_rect1 = text1.get_rect(center=(500, 200))
    screen.blit(text1, text_rect1)

    font = pygame.font.Font(None, 36)
    text2 = font.render("Henri ja Grete", True, BLACK)
    text_rect2 = text2.get_rect(center=(500, 300))
    screen.blit(text2, text_rect2)

    text3 = font.render("Et mängu alustada vajuta mänguaknale", True, BLACK)
    text_rect3 = text3.get_rect(center=(500, 400))
    screen.blit(text3, text_rect3)

    pygame.display.flip()

def main():
    num_players = 4
    player_positions = [1] * num_players  # Initialize positions for each player
    dice_rolled = [False] * num_players  # Keep track of whether each player has rolled the dice
    game_won = [False] * num_players  # Keep track of whether each player has won the game

    show_welcome_screen()

    try:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Handle dice roll for each player
                for player in range(num_players):
                    if not dice_rolled[player] and not game_won[player]:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            steps = throw_dice()
                            print(f"Player {player + 1} rolled a {steps}.")
                            player_positions[player] += steps
                            dice_rolled[player] = True

            screen.fill(WHITE)  # Clear the screen

            draw_board(player_positions)

            # Move player dots and check for game win
            for player in range(num_players):
                if dice_rolled[player]:
                    pygame.draw.circle(screen, (0, 0, 255), (player_positions[player] % 9 * 80 + 50, player_positions[player] // 9 * 80 + 50), 10)
                    dice_rolled[player] = False

                    if player_positions[player] >= len(board_layout) - 1:  # Check if player passes or lands on FINISH tile
                        game_won[player] = True

            if all(game_won):
                display_message("Palju õnne, kõik mängijad on võitnud!")
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
