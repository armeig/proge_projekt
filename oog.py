import pygame
import random
import sys
import textwrap

TITLE_SCREEN = 0
RULES_SCREEN = 1
GAME_SCREEN = 2
current_screen = TITLE_SCREEN
tile_width = 120
tile_height = 120
tile_margin = 20

start_x = 50
start_y = 50


dice_image = pygame.image.load('R.png')
dice_image = pygame.transform.scale(dice_image, (200, 200))


def display_instructions():
    return """
    Welcome to the game "Drinking Friends" - Ultimate Drinking Adventure!
    ...
    Press 's' and then click on the screen to start the game and let the laughter flow!
    """

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
        x = start_x + (i % 5) * (tile_width + tile_margin)
        y = start_y + (i // 5) * (tile_height + tile_margin)
        pygame.draw.rect(screen, BLACK, (x, y, tile_width, tile_height), 3)
        font = pygame.font.Font(None, 36)
        text = font.render(square, True, BLACK)
        text_x = x + (tile_width - text.get_width()) / 2
        text_y = y + (tile_height - text.get_height()) / 2
        screen.blit(text, (text_x, text_y))


def display_popup(title, text, challenge_name):
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 0, 0), (200, 200, 600, 400))
    font_title = pygame.font.Font(None, 36)
    font_challenge_name = pygame.font.Font(None, 40)  
    font_text = pygame.font.Font(None, 30)
    title_text = font_title.render(title, True, (255, 255, 255))
    challenge_name_text = font_challenge_name.render(challenge_name, True, (255, 255, 255))  
    #text_text = font_title.render(text, True, (255, 255, 255))
    screen.blit(title_text, (400 - title_text.get_width() // 2, 250))
    screen.blit(challenge_name_text, (210, 210))  
    #screen.blit(text_text, (400 - text_text.get_width() // 2, 300))

    wrapped_text = textwrap.fill(text, width=50)  
    y_offset = 350
    screen_width = screen.get_width()

    for line in wrapped_text.split('\n'):
        rendered_line = font_text.render(line, True, (255, 255, 255))
        #screen.blit(rendered_line, (220, y_offset))
        line_width = rendered_line.get_width()
        x_coordinate = (screen_width - line_width) // 2
        screen.blit(rendered_line, (x_coordinate, y_offset))
        y_offset += font_text.get_linesize()

def roll_dice():
    return random.randint(1, 6)

def display_message(message, y_offset=0):
    font = pygame.font.Font(None, 24)
    lines = message.strip().split("\n")
    for i, line in enumerate(lines):
        text = font.render(line, True, BLACK)
        text_rect = text.get_rect(center=(500, 100 + y_offset + i * 30))
        screen.blit(text, text_rect)

def display_message2(message, y_offset=0):
    font = pygame.font.Font(None, 40)
    lines = message.strip().split("\n")
    for i, line in enumerate(lines):
        text = font.render(line, True, BLACK)
        text_rect = text.get_rect(center=(500, 400 + y_offset + i * 30))
        screen.blit(text, text_rect)

def play_game():
    global current_screen
    
    position = 0
    dice_rolled = False
    game_won = False
    game_started = False
    welcome_screen = True
    instructions_screen = False
    instructions = display_instructions()
    win_time = None
    show_popup = False
    button_x, button_y, button_width, button_height = 400, 600, 200, 200 

    try:
        while True:
            screen.fill(WHITE)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    if button_x <= mouse_x <= button_x + button_width and button_y <= mouse_y <= button_y + button_height:
                        if current_screen == TITLE_SCREEN:
                            current_screen = RULES_SCREEN
                        elif current_screen == RULES_SCREEN:
                            current_screen = GAME_SCREEN

            if current_screen == TITLE_SCREEN:
                display_message("Drinking Friends - Click to Start", y_offset=-50)
                pygame.draw.rect(screen, BLACK, (button_x, button_y, button_width, button_height))

            elif current_screen == RULES_SCREEN:
                display_message(display_instructions(), y_offset=-50)
                pygame.draw.rect(screen, BLACK, (button_x, button_y, button_width, button_height))

            elif current_screen == GAME_SCREEN:
                draw_game_board(position)

                screen.blit(dice_image, (button_x, button_y))
                
                dot_x = start_x + (position % 5) * (tile_width + tile_margin) + tile_width / 2
                dot_y = start_y + (position // 5) * (tile_height + tile_margin) + tile_height / 2
                pygame.draw.circle(screen, (255, 0, 0), (int(dot_x), int(dot_y)), 15)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_x, mouse_y = event.pos
                        if button_x <= mouse_x <= button_x + button_width and button_y <= mouse_y <= button_y + button_height:
                            steps = roll_dice()
                            print(f"You rolled {steps}.")
                            position += steps
                            dice_rolled = True
                            challenge_text, challenge_name = tiles(position)
                            if challenge_text:
                                display_popup(" ", challenge_text, challenge_name)
                                pygame.display.flip()

                                waiting_for_input = True
                                while waiting_for_input:
                                    for sub_event in pygame.event.get():
                                        if sub_event.type == pygame.QUIT:
                                            pygame.quit()
                                            sys.exit()
                                        elif sub_event.type == pygame.MOUSEBUTTONDOWN or sub_event.type == pygame.KEYDOWN:
                                            waiting_for_input = False

                if dice_rolled:
                    pygame.draw.circle(screen, (0, 0, 255), (position % 11 * 80 + 50, position // 11 * 80 + 50), 10)
                    dice_rolled = False

                    if position >= len(board_shape) - 1:
                        game_won = True
                        win_time = pygame.time.get_ticks()

                if game_won:
                    if pygame.time.get_ticks() - win_time < 5000:
                        display_message2("Congratulations, you have won!")
                        pygame.display.flip()
                    else:
                        pygame.quit()
                        sys.exit()

            pygame.display.flip()
            clock.tick(60)

    except KeyboardInterrupt:
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    play_game()