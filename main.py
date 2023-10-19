import pygame as pg
import sys
from utils import *
from longestword import *

IMGS_DIR = "./Slagalica/imgs"
# Initialize Pygame
pg.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
FONT_SIZE = 36

# Create the screen
# screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# pg.display.set_caption("Arcade Game")

# Create a font
# font = pg.font.Font(None, FONT_SIZE)
background_path = IMGS_DIR + "/background.jpg"
# Function to set the background


class GameState():
    def __init__(self):

        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        # pg.display.set_caption("Arcade Game")
        self.next_button = Button(300, 200, 200, 50, "PLAY", 36, (255, 255, 255), (0, 0, 255))

        self.state = 'main_menu'

        self.Longest_Word = LongestWord(self.screen)

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
            if event.type == pg.MOUSEBUTTONUP:
                # check if hit start btn
                mouse_pos = pg.mouse.get_pos()
                if self.next_button.is_clicked(mouse_pos):
                # Perform some action when the button is clicked
                    self.state = 'longest_word'

                    print("Button clicked!")


        # Check if the button is clicked

        # Set the background
        set_background(self.screen, background_path)


        # Display the menu options
        # display_text(self.screen, "Main Menu", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)
        # display_text(self.screen, "Press Enter to Play", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        # display_text(self.screen, "Press Q to Quit", SCREEN_WIDTH // 2, 3 * SCREEN_HEIGHT // 4)
        self.next_button.draw(self.screen)
    # def longest_word(self):
    #     for event in pg.event.get():
    #         if event.type == pg.QUIT:
    #             pg.quit()
    #             sys.exit()
    #         if event.type == pg.KEYDOWN:
    #             if event.key == pg.K_RETURN:
    #                 # Start the game (you can replace this with your game code)
    #                 self.state = 'find_number'
    #                 print("Starting the game!")
    #             if event.key == pg.K_q:
    #                 # Quit the game
    #                 pg.quit()
    #                 sys.exit()

    #     # Set the background
    #     set_background(backgrounqd_path)

    #     # Display the menu options
    #     display_text("Main Menu", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)
    #     display_text("Press Enter to longest word", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    #     display_text("Press Q to Quit", SCREEN_WIDTH // 2, 3 * SCREEN_HEIGHT // 4)
    
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
        set_background(self.screen, background_path)

        # Display the menu options
        display_text(self.screen, "Main Menu", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)
        display_text(self.screen, "Press Enter to find number", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        display_text(self.screen, "Press Q to Quit", SCREEN_WIDTH // 2, 3 * SCREEN_HEIGHT // 4)


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
        set_background(self.screen, background_path)

        # Display the menu options
        display_text(self.screen, "Main Menu", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)
        display_text(self.screen, "Press Enter to master mind", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        display_text(self.screen, "Press Q to Quit", SCREEN_WIDTH // 2, 3 * SCREEN_HEIGHT // 4)

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
                if event.key == pg.K_qq:
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
            self.state = self.Longest_Word.play(self.screen)
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