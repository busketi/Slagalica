import pygame as pg
import sys
from utils import *

background_path = IMGS_DIR + "/background.jpg"

class LongestWord():
    def __init__(self, screen, state):
        self.screen = screen
        self.state = 'longest_word'


    def play(self, screen):
        self.screen = screen
        run = True
        print("LR")
        while run:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN:
                        # Start the game (you can replace this with your game code)
                        self.state = 'find_number'
                        # print("Starting the game!")
                    if event.key == pg.K_q:
                        # Quit the game
                        pg.quit()
                        sys.exit()
                    if event.key == pg.K_n:
                        # Quit the game
                        self.state = 'find_number'

                        run = False

            # Set the background
            set_background(self.screen, background_path)

            # Display the menu options
            display_text(self.screen, "Main Menu", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)
            display_text(self.screen, "Press Enter to Play LONGESTWORD", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
            display_text(self.screen, "Press Q to Quit", SCREEN_WIDTH // 2, 3 * SCREEN_HEIGHT // 4)
            # return self.state
            pg.display.update()
        return self.state