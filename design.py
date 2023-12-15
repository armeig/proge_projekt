

def display_instructions():
    return """
    Welcome to the game "Drinking Friends" - Ultimate Drinking Adventure!

    Embark on a journey full of laughter, friendship, and a hint of mischief. 
    "Drinking Friends" is not just a board game; it's a ticket to memorable moments and endless fun.

    You'll encounter challenges inspired by classic party games like "Never Have I Ever" and "Truth or Dare." 
    Brace yourself for unexpected twists and hilarious revelations!

    Instructions:
    - Click on the game board to start this epic adventure.
    - Roll the dice, move your token, and face the challenges that await you.
    - You win by reaching the coveted "FINISH" square, but remember! 
    The real victory lies in the shared moments and the joy of the game.

    Gather your friends, pour your favorite drinks, and let the games begin! Are you ready for the "Drinking Friends" experience?

    Press 's' and then click on the screen to start the game and let the laughter flow!
    """


import pygame
import random
import sys



challenges_dict = {
    5: [
        "Slide into your crush’s DMs.",
        "Tell everybody your biggest secret.",
        "Tell everybody a secret that you’ve never told anyone.",
        "Drink! ayyyy ;)",
        "Tell everyone about your worst date.",
        "Kiss the person that’s on your left. (If you’re in a relationship with them, kiss the person on your right - if you say no, you drink, if they say no, you both have to drink)",
        "Compliment the person sitting opposite of you.",
        "Show us your Instagram search history.",
        "Show us your Google search history.",
        "Drink! heh ;)",
        "Do 150 pushups. (If you start and can’t complete 150 pushups you have to down your drink altogether)",
        "Give everyone in this room 5€.",
        "Post on your Insta story “real friends don’t exist, everyone’s fake in this generation”",
        "Send “i miss you, wanna link?” to your ex (if you don’t have an ex - drink)",
        "Describe vividly your biggest sexual fantasy.",
    ],
    
}


pygame.init()

screen = pygame.display.set_mode((1000, 800))


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
clock = pygame.time.Clock()


board_shape = [
    'START', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', 'FINISH'
]


def draw_game_board(position):
    for i, square in enumerate(board_shape):
        x = 30 + (i % 11) * 80
        y = 30 + (i // 11) * 80
        pygame.draw.rect(screen, BLACK, (x, y, 60, 60), 3)
        font = pygame.font.Font(None, 24)
        text = font.render(square, True, BLACK)
        screen.blit(text, (x + 5, y + 5))

def display_popup(title, text):
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 0, 0), (200, 200, 600, 400))  
    font = pygame.font.Font(None, 36)
    title_text = font.render(title, True, (255, 255, 255))
    text_text = font.render(text, True, (255, 255, 255))
    screen.blit(title_text, (400 - title_text.get_width() // 2, 250))
    screen.blit(text_text, (400 - text_text.get_width() // 2, 300))

def roll_dice():
    return random.randint(1, 6)

def display_message(message, y_offset=0):
    font = pygame.font.Font(None, 24)
    lines = message.strip().split("\n")
    for i, line in enumerate(lines):
        text = font.render(line, True, BLACK)
        text_rect = text.get_rect(center=(500, 100 + y_offset + i * 30))
        screen.blit(text, text_rect)

def play_game():
    position = 0
    dice_rolled = False
    game_won = False
    game_started = False
    welcome_screen = True
    instructions_screen = False
    instructions = display_instructions()
    win_time = None
    show_popup = False



    try:
        while True:
            screen.fill(WHITE)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if not instructions_screen and welcome_screen and event.type == pygame.MOUSEBUTTONDOWN:
                    instructions_screen = True
                    display_message(instructions, y_offset=-50)
                    pygame.display.flip()

                if instructions_screen and event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                    welcome_screen = False
                    instructions_screen = False
                    game_started = True

                if game_started and event.type == pygame.MOUSEBUTTONDOWN and not dice_rolled and not game_won:
                    steps = roll_dice()
                    print(f"You rolled {steps}.")
                    position += steps
                    dice_rolled = True

            if welcome_screen and not instructions_screen:
                display_message("Drinking Friends", y_offset=-50)
                display_message("Henri and Grete", y_offset=0)
                display_message("Click on the screen to see the instructions for the game", y_offset=50)
                pygame.display.flip()

            elif instructions_screen:
                display_message(instructions, y_offset=-50)
                pygame.display.flip()

            elif game_started:
                draw_game_board(position)

                if dice_rolled:
                    pygame.draw.circle(screen, (0, 0, 255), (position % 11 * 80 + 50, position // 11 * 80 + 50), 10)
                    dice_rolled = False

                    if position >= len(board_shape) - 1:
                        
                        if position in challenges_dict and not show_popup:
                            show_popup = True

                        game_won = True
                        win_time = pygame.time.get_ticks()

                    pygame.display.flip()

                if show_popup:
                    
                    current_tile_challenges = challenges_dict[position]
                    challenge_text = current_tile_challenges[0]  
                    display_popup("Truth or Drink", challenge_text)
                    pygame.display.flip()

                    
                    for event_popup in pygame.event.get():
                        if event_popup.type == pygame.KEYDOWN and event_popup.key == pygame.K_s:
                            show_popup = False
                            current_tile_challenges.pop(0)  

                    continue  

                if game_won:
                    if pygame.time.get_ticks() - win_time < 5000:
                        display_message("Congratulations, you have won!")
                        pygame.display.flip()
                    else:
                        pygame.quit()
                        sys.exit()

            clock.tick(60)

    except KeyboardInterrupt:
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    play_game()
