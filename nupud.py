import pygame
import sys


image = pygame.image.load('R.png').convert_alpha()


# Define a button class
class Button:
    def __init__(self, text, position, action):
        self.text = text
        self.position = position
        self.action = action
        self.font = pygame.font.Font(None, 36)
        self.width = 200
        self.height = 50
        self.inactive_color = (50, 50, 50)
        self.active_color = (100, 100, 100)
        self.text_color = (255, 255, 255)
        self.rect = pygame.Rect(self.position[0], self.position[1], self.width, self.height)
    
    def draw(self, screen):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if self.rect.collidepoint(mouse):
            pygame.draw.rect(screen, self.active_color, self.rect)
            if click[0] == 1:
                self.action()
        else:
            pygame.draw.rect(screen, self.inactive_color, self.rect)

        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

# Functions to handle actions for different buttons
def button1_action():
    print("Button 1 clicked!")

def button2_action():
    print("Button 2 clicked!")

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Multiple Buttons in Pygame Loop')

# Create button instances with different functions
button1 = Button("Button 1", (50, 50), button1_action)
button2 = Button("Button 2", (50, 150), button2_action)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))  # Fill the screen with white

    # Draw buttons and handle their behavior
    button1.draw(screen)
    button2.draw(screen)

    pygame.display.update()

pygame.quit()
sys.exit()
