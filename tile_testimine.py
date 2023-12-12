

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

import random

    





import random

def challenges(fail):
    mitu_rida = 0
    andmed = []
    f = open(fail, encoding='UTF-8')
    for rida in f:
        uus = rida.strip().split(': ')
        mitu_rida += 1
        andmed.append([int(uus[0]),uus[1]])
    f.close()
    number = random.randint(1, mitu_rida)
    print(number)
    for paar in andmed:
        if number == paar[0]:
            küsimus = paar[1]
    return küsimus

def tiles(position):
    valjakutse = ""
    challenge_name = ""
    if position == 1 or position == 10 or position == 16:
        valjakutse = challenges('truthordrink.txt')
        challenge_name = "Truth or drink"
    elif position == 4 or position == 11 or position == 18:
        valjakutse = challenges('generalknowledgeq.txt')
        challenge_name = "General knowledge"
    elif position == 2 or position == 20:
        valjakutse = "EVERYBODY DRINKS!"
        challenge_name = "EVERYBODY DRINKS!"
    elif position == 3 or position == 9:
        valjakutse = "Astu korra seadmega teistest eemale, et järgnevat küsimust näeksid ainult sina!"
        valjakutse = challenges('paranoia.txt')
        challenge_name = "Paranoia"
    elif position == 5 or position == 15 or position == 19:
        valjakutse = challenges('dareordrink.txt')
        challenge_name = "Dare or drink"
    elif position == 6 or position == 14:
        valjakutse = challenges('neverhaveiever.txt')
        challenge_name = "Never have i ever"
    elif position == 7 or position == 12 or position == 17:
        valjakutse = challenges('baila.txt')
        challenge_name = "Baila"
    elif position == 8:
        valjakutse = "LUCKY YOU! You can rest right now and not drink."
        challenge_name = "LUCKY"
    elif position == 13:
        valjakutse = "Finish your drink right this second and go make yourself a new one."
        challenge_name = "CHUG"
    return valjakutse, challenge_name





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

def display_popup(title, text, challenge_name):
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 0, 0), (200, 200, 600, 400))
    font_title = pygame.font.Font(None, 36)
    font_challenge_name = pygame.font.Font(None, 24)  
    title_text = font_title.render(title, True, (255, 255, 255))
    challenge_name_text = font_challenge_name.render(challenge_name, True, (255, 255, 255))  
    text_text = font_title.render(text, True, (255, 255, 255))
    screen.blit(title_text, (400 - title_text.get_width() // 2, 250))
    screen.blit(challenge_name_text, (210, 210))  
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

                    challenge_text, challenge_name = tiles(position)
                    if challenge_text:
                        bottom = "or drink"
                        display_popup(" ", challenge_text, challenge_name)
                        pygame.display.flip()
                        

            if welcome_screen and not instructions_screen:
                display_message("Drinking Friends", y_offset=-50)
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
                        game_won = True
                        win_time = pygame.time.get_ticks()

                    pygame.display.flip()

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
