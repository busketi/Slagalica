import pygame as pg
import sys

IMGS_DIR = "./Slagalica/imgs"
# Initialize Pygame
pg.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
FONT_SIZE = 36

# Create the screen
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("Arcade Game")

# Create a font
font = pg.font.Font(None, FONT_SIZE)
background_path = IMGS_DIR + "/background.jpg"
# Function to set the background
def set_background(image_path):
    background = pg.image.load(image_path)
    screen.blit(background, (0, 0))

# Function to display text on the screen
def display_text(text, x, y):

    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)



class GameState():
    def __init__(self):
        self.state = 'main_menu'

    def main_menu(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    # Start the game (you can replace this with your game code)
                    self.state = 'longest_word'
                    print("Starting the game!")
                if event.key == pg.K_q:
                    # Quit the game
                    pg.quit()
                    sys.exit()

        # Set the background
        set_background(background_path)

        # Display the menu options
        display_text("Main Menu", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)
        display_text("Press Enter to Play", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        display_text("Press Q to Quit", SCREEN_WIDTH // 2, 3 * SCREEN_HEIGHT // 4)

    def longest_word(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    # Start the game (you can replace this with your game code)
                    self.state = 'find_number'
                    print("Starting the game!")
                if event.key == pg.K_q:
                    # Quit the game
                    pg.quit()
                    sys.exit()

        # Set the background
        set_background(background_path)

        # Display the menu options
        display_text("Main Menu", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)
        display_text("Press Enter to longest word", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        display_text("Press Q to Quit", SCREEN_WIDTH // 2, 3 * SCREEN_HEIGHT // 4)
    
    def find_number(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    # Start the game (you can replace this with your game code)
                    self.state = 'master_mind'
                    print("Starting the game!")
                if event.key == pg.K_q:
                    # Quit the game
                    pg.quit()
                    sys.exit()

        # Set the background
        set_background(background_path)

        # Display the menu options
        display_text("Main Menu", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)
        display_text("Press Enter to find_number", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        display_text("Press Q to Quit", SCREEN_WIDTH // 2, 3 * SCREEN_HEIGHT // 4)

    def master_mind(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    # Start the game (you can replace this with your game code)
                    self.state = 'who_knows_knows'
                    print("Starting the game!")
                if event.key == pg.K_q:
                    # Quit the game
                    pg.quit()
                    sys.exit()

        # Set the background
        set_background(background_path)

        # Display the menu options
        display_text("Main Menu", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)
        display_text("Press Enter to master_mind", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        display_text("Press Q to Quit", SCREEN_WIDTH // 2, 3 * SCREEN_HEIGHT // 4)

    def who_knows_knows(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    # Start the game (you can replace this with your game code)
                    self.state = 'longest_word'
                    print("Starting the game!")
                if event.key == pg.K_q:
                    # Quit the game
                    pg.quit()
                    sys.exit()

        # Set the background
        set_background(background_path)

        # Display the menu options
        display_text("Main Menu", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)
        display_text("Press Enter to who_knows_knows", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        display_text("Press Q to Quit", SCREEN_WIDTH // 2, 3 * SCREEN_HEIGHT // 4)
    
    def state_manager(self):
        if self.state == 'main_menu':
            self.main_menu()
        if self.state == 'longest_word':
            self.longest_word()
        if self.state == 'find_number':
            self.find_number()
        if self.state == 'master_mind':
            self.master_mind()
        if self.state == 'who_knows_knows':
            self.who_knows_knows()
game = GameState()
while True:
    game.state_manager()
    pg.display.update()