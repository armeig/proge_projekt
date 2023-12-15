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


dice_image = pygame.image.load('dicepic.png')
dice_image = pygame.transform.scale(dice_image, (200, 200))


def display_instructions():
    return "The player with the highest rice test score, rolls the dice first. To roll the dice, click on the dice. If the dice has been rolled, wait until the next screen with the challenge/question is displayed. The golden rule is the challenge is not complete until someone drinks. If at any point in the game you feel like you can’t drink anymore - just exchange alcohol with water. We do not encourage peer pressure! The aim of the game is to have fun! If you want to move on and there is no button, just click on the screen. In never have I ever you drink if you HAVE done it. HAVE FUN!"

def challenges(file):
    how_many_lines = 0
    data = []
    f = open(file, encoding='UTF-8')
    for line in f:
        new = line.strip().split(': ')
        how_many_lines += 1
        data.append([int(new[0]), new[1]])
    f.close()
    number = random.randint(1, how_many_lines)
    for pair in data:
        if number == pair[0]:
            question = pair[1]
    return question


def challenges_baila_title(file):
    how_many_lines = 0
    data = []
    f = open(file, encoding='UTF-8')
    for line in f:
        new = line.strip().split(': ')
        how_many_lines += 1
        title_and_explanation = new[1]
        to_get_the_title = title_and_explanation.split(' . ')
        data.append([int(new[0]), to_get_the_title[0], to_get_the_title[1]])
    f.close()
    number = random.randint(1, how_many_lines)
    for trio in data:
        if number == trio[0]:
            baila_title = trio[1]
    return baila_title

def challenges_baila_explanation(file):
    how_many_lines = 0
    data = []
    f = open(file, encoding='UTF-8')
    for line in f:
        new = line.strip().split(': ')
        how_many_lines += 1
        title_and_explanation = new[1]
        to_get_the_title = title_and_explanation.split(' . ')
        data.append([int(new[0]), to_get_the_title[0], to_get_the_title[1]])
    f.close()
    number = random.randint(1, how_many_lines)
    for trio in data:
        if number == trio[0]:
            explanation = trio[2]
    return explanation




def tiles(position):
    call = ""
    challenge_name = ""
    if position == 1 or position == 10 or position == 16:
        call = challenges('truthordrink.txt')
        challenge_name = "Truth or drink"
    elif position == 4 or position == 13 or position == 18:
        call = challenges('generalknowledgeq.txt')
        challenge_name = "General knowledge"
    elif position == 2 or position == 20:
        call = "EVERYBODY DRINKS!"
        challenge_name = "EVERYBODY DRINKS!"
    elif position == 3 or position == 9:
        call = "Step away from others with the computer for a second to see the question - it's of the upmost importance that others don't see the question!!!"
        call = challenges('paranoia.txt')
        challenge_name = "Paranoia"
    elif position == 8 or position == 15 or position == 19:
        call = challenges('dareordrink.txt')
        challenge_name = "Dare or drink"
    elif position == 6 or position == 12:
        call = challenges('neverhaveiever.txt')
        challenge_name = "Never have I ever"
    elif position == 7 or position == 14 or position == 17:
        call = challenges_baila_title('baila.txt')
        call = challenges_baila_explanation('baila.txt')
        challenge_name = "Baila"
    elif position == 5:
        call = "LUCKY YOU! You can rest right now and not drink."
        challenge_name = "LUCKY"
    elif position == 11:
        call = "Down your drink right this second and go get yourself a new one."
        challenge_name = "CHUG"
    return call, challenge_name

pygame.init()
screen = pygame.display.set_mode((1000, 800))
mainpage_image = pygame.image.load('mainpage.jpg')
mainpage_image = pygame.transform.scale(mainpage_image, (1000, 800))
rules_image = pygame.image.load('background.jpg')
rules_image = pygame.transform.scale(rules_image, (1000, 800))
game_image = pygame.image.load('background.jpg')
game_image = pygame.transform.scale(game_image, (1000, 800))
truthordrink_image = pygame.image.load('truthordrinktile.jpg')
truthordrink_image = pygame.transform.scale(truthordrink_image, (tile_width, tile_height))
dareordrink_image = pygame.image.load('dareordrinktile.jpg')
dareordrink_image = pygame.transform.scale(dareordrink_image, (tile_width, tile_height))
downyourdrink_image = pygame.image.load('downyourdrink.jpg')
downyourdrink_image = pygame.transform.scale(downyourdrink_image, (tile_width, tile_height))
baila_image = pygame.image.load('bailatile.jpg')
baila_image = pygame.transform.scale(baila_image, (tile_width, tile_height))
everybody_drink_image = pygame.image.load('everybodydrinks.jpg')
everybody_drink_image = pygame.transform.scale(everybody_drink_image, (tile_width, tile_height))
neverhaveiever_image = pygame.image.load('neverhaveievertile.jpg')
neverhaveiever_image = pygame.transform.scale(neverhaveiever_image, (tile_width, tile_height))
lucky_you_image = pygame.image.load('lucky you.jpg')
lucky_you_image = pygame.transform.scale(lucky_you_image, (tile_width, tile_height))
paranoia_image = pygame.image.load('paranoiatile.jpg')
paranoia_image = pygame.transform.scale(paranoia_image, (tile_width, tile_height))
generalknowledge_image = pygame.image.load('generalknowledgetile.jpg')
generalknowledge_image = pygame.transform.scale(generalknowledge_image, (tile_width, tile_height))
Finish_image = pygame.image.load('finish.jpg')
Finish_image = pygame.transform.scale(Finish_image, (tile_width, tile_height))
start_image = pygame.image.load('start.jpg')
start_image = pygame.transform.scale(start_image, (tile_width, tile_height))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (251, 255, 243)
clock = pygame.time.Clock()

board_shape = [
    'START', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', 'FINISH'
]

def draw_game_board(position):
    

    for i, square in enumerate(board_shape):
        x = start_x + (i % 5) * (tile_width + tile_margin)
        y = start_y + (i // 5) * (tile_height + tile_margin)
       
        if i in [1, 10, 16]:  
            screen.blit(truthordrink_image, (x, y))
        
        elif i in [8, 15, 19]:
            screen.blit(dareordrink_image, (x, y))
        
        elif i in [11]:
            screen.blit(downyourdrink_image, (x, y))
        
        elif i in [7, 14, 17]:
            screen.blit(baila_image, (x, y))
        
        elif i in [2, 20]:
            screen.blit(everybody_drink_image, (x, y))

        elif i in [6, 12]:
            screen.blit(neverhaveiever_image, (x, y))
        
        elif i in [5]:
            screen.blit(lucky_you_image, (x,y))
        
        elif i in [3, 9]:
            screen.blit(paranoia_image, (x, y))
        
        elif i in [4, 13, 18]:
            screen.blit(generalknowledge_image, (x, y))
        
        elif i in [21]:
            screen.blit(Finish_image, (x, y))
        
        elif i in [0]:
            screen.blit(start_image, (x, y))

        elif i in [0]:
            screen.blit(start_image, (x, y))

        elif i in [21]:
            screen.blit(Finish_image, (x, y))

        else:
            pygame.draw.rect(screen, BLACK, (x, y, tile_width, tile_height), 3)
            font = pygame.font.Font(None, 36)
            text = font.render(square, True, BLACK)
            text_x = x + (tile_width - text.get_width()) / 2
            text_y = y + (tile_height - text.get_height()) / 2
            screen.blit(text, (text_x, text_y))

def display_popup(title, text, challenge_name):
    screen.fill((255, 255, 255))
    screen.blit(game_image, (0, 0))
    pygame.draw.rect(screen, (251, 255, 243), (200, 200, 600, 400))
    font_title = pygame.font.Font(None, 36)
    font_challenge_name = pygame.font.Font(None, 40)  
    font_text = pygame.font.Font(None, 30)
    title_text = font_title.render(title, True, (0, 0, 0))
    challenge_name_text = font_challenge_name.render(challenge_name, True, (0, 0, 0))  
    screen.blit(title_text, (400 - title_text.get_width() // 2, 250))
    screen.blit(challenge_name_text, (210, 210))
    wrapped_text = textwrap.fill(text, width=50)
    y_offset = 350
    screen_width = screen.get_width()

    for line in wrapped_text.split('\n'):
        rendered_line = font_text.render(line, True, (0, 0, 0))
        line_width = rendered_line.get_width()  # Calculate the width of each rendered line here
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
    waiting_for_input = False
    button_x, button_y, button_width, button_height = 400, 600, 200, 200
    button2_x, button2_y, button2_width, button2_height = 350, 475, 300, 100
    Green = (251, 255, 243)
    button_font = pygame.font.Font(None, 36)
    
    try:
        while True:
            screen.fill(WHITE)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    if current_screen in [TITLE_SCREEN, RULES_SCREEN]:
                        if button2_x <= mouse_x <= button2_x + button2_width and button2_y <= mouse_y <= button2_y + button2_height:
                            if current_screen == TITLE_SCREEN:
                                current_screen = RULES_SCREEN
                            elif current_screen == RULES_SCREEN:
                                current_screen = GAME_SCREEN

                    elif current_screen == GAME_SCREEN:
                        if button_x <= mouse_x <= button_x + button_width and button_y <= mouse_y <= button_y + button_height:
                            steps = roll_dice()
                            print(f"You rolled {steps}.")
                            position += steps
                            new_position = position 
                            if new_position >= len(board_shape) - 1:
                                new_position = len(board_shape) - 1  

                            position = new_position
                            dice_rolled = True
                            challenge_text, challenge_name = tiles(position)
                            
                            screen.blit(game_image, (0, 0))
                            draw_game_board(position)

       
                            dot_x = start_x + (position % 5) * (tile_width + tile_margin) + tile_width / 2
                            dot_y = start_y + (position // 5) * (tile_height + tile_margin) + tile_height / 2
                            

        
                            pygame.draw.circle(screen, (255, 0, 0), (int(dot_x), int(dot_y)), 15)
                            
                            pygame.display.flip()
                            pygame.time.delay(1200)
                           
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
                        position = len(board_shape) - 1
                        game_won = True
                        win_time = pygame.time.get_ticks()

                if game_won:
                    victory_title = "Congratulations!"
                    victory_text = "You have won the game!"
                    victory_challenge_name = "VICTORY"
                    display_popup2(victory_title, victory_text, victory_challenge_name)
                    pygame.display.flip()
                    
                    waiting_for_input = True
                    while waiting_for_input:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                            elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
                                waiting_for_input = False
                        break

            if current_screen == TITLE_SCREEN:
                screen.blit(mainpage_image, (0, 0))
                pygame.draw.rect(screen, Green, (button2_x, button2_y, button2_width, button2_height))
                text_surface = button_font.render("Start", True, BLACK)  
                text_rect = text_surface.get_rect(center=(button2_x + button2_width // 2, button2_y + button2_height // 2))
                screen.blit(text_surface, text_rect)


            elif current_screen == RULES_SCREEN:
                display_message(display_instructions(), y_offset=-50)
                screen.blit(rules_image, (0, 0))
                pygame.draw.rect(screen, Green, (button2_x, button2_y, button2_width, button2_height))  
                text_surface = button_font.render("Start game", True, BLACK)  
                text_rect = text_surface.get_rect(center=(button2_x + button2_width // 2, button2_y + button2_height // 2))
                screen.blit(text_surface, text_rect)


            elif current_screen == GAME_SCREEN:
                screen.blit(game_image, (0, 0))
                draw_game_board(position)
                screen.blit(dice_image, (button_x, button_y))
                dot_x = start_x + (position % 5) * (tile_width + tile_margin) + tile_width / 2
                dot_y = start_y + (position // 5) * (tile_height + tile_margin) + tile_height / 2
                pygame.draw.circle(screen, (255, 0, 0), (int(dot_x), int(dot_y)), 15)

            pygame.display.flip()
            clock.tick(60)

    except KeyboardInterrupt:
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    play_game()
