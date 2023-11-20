import pygame as pg
import sys
from utils import *
import random
import numpy as np
import requests

background_path = IMGS_DIR + "/background.jpg"

def make_letters():
    broj_samoglasnika = random.randint(4,6)
    print(broj_samoglasnika)
    suglasnici = "BCČĆDĐFGHJKLMNPRSTŠVZŽ"
    suglasnici = [char for char in suglasnici]
    suglasnici.append("Nj")
    suglasnici.append("Dž")
    suglasnici.append("Lj")
    samoglasnici = "AEOIU"
    samoglasnici = [char for char in samoglasnici]
    temp = list()
    for _ in range(broj_samoglasnika):
        temp.append(random.choice(samoglasnici))
        print(temp)
    for _ in range(12 - broj_samoglasnika):
        temp.append(random.choice(suglasnici))
    random.shuffle(temp)
    return temp

def make_buttons(letters):
    SPACING = 20
    BUTTON_WIDTH = 40
    BUTTON_HEIGHT = 40
    X_POS = 50
    Y_POS = 300
    buttons = []
    for i in range(12):
        button = Button(X_POS + i * (BUTTON_WIDTH + SPACING), Y_POS, BUTTON_WIDTH, BUTTON_HEIGHT, letters[i], 36, (0, 0, 0), (255, 255, 255))
        buttons.append(button)
    return buttons

class Mastermind():
    def __init__(self, screen):
        self.image_btn = ImageButton(100, 100 , 80,80 , (255, 255, 255), IMGS_DIR+"/diamonds.png")
        self.screen = screen
        self.state = 'longest_word'
        self.next_button_lw = Button(500, 500, 200, 50, "Sledeca igra", 24, (255, 255, 255), (0, 0, 255))
        # self.letters = make_letters()
        # self.buttons = make_buttons(self.letters)
        self.backspace_button = Button(600, 400,  50, 50, "<-", 35, (255, 255, 255), (0, 255, 0))
        self.erase_all_button = Button(700, 400, 50, 50, "X", 35, (255, 255, 255), (255, 0, 0))
        self.check_word_button = Button(50, 400, 200, 50, "Potvrdi rec", 24, (255, 255, 255), (255, 0, 0))

        self.player_word = list()
        self.player_word_order = list()



    def play(self, screen):
        self.screen = screen
        run = True
        print("LR")
        # print(self.letters)
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
                if event.type == pg.MOUSEBUTTONUP:
                    # check if hit start btn
                    mouse_pos = pg.mouse.get_pos()
                    if self.next_button_lw.is_clicked(mouse_pos):
                    # Perform some action when the button is clicked
                        self.state = 'mastermind'
                        print("Button clicked!")
                        continue
                    # for i,elem in enumerate(self.buttons):
                    #     print(elem.action)
                    #     if elem.action == 0 and elem.is_clicked(mouse_pos):
                    #         self.player_word.append(elem.text)
                    #         self.player_word_order.append(i)
                    #         continue
                    if self.backspace_button.is_clicked(mouse_pos):
                        if len(self.player_word)>0:
                            self.player_word.pop()
                            i = self.player_word_order.pop()
                            self.buttons[i].button_color = (255,255,255)
                            self.buttons[i].action = 0
                            continue
                    if self.erase_all_button.is_clicked(mouse_pos):
                        for elem in self.buttons:
                            elem.button_color = (255,255,255)
                            elem.action = 0
                            self.player_word=list()
                            self.player_word_order=list()
                            continue
                    if self.check_word_button.is_clicked(mouse_pos):
                            print("https://staznaci.com/" + "".join([str(i) for i in self.player_word]))
                            response = requests.get("https://staznaci.com/"+ "".join([str(i) for i in self.player_word]), timeout=30)
                            print(response)

            # Set the background
            set_background(self.screen, background_path)

            # Display the menu options
            display_text(self.screen, "".join([str(i) for i in self.player_word]), SCREEN_WIDTH // 2, 200)
            
            self.next_button_lw.draw(self.screen)
            self.backspace_button.draw(self.screen)
            self.erase_all_button.draw(self.screen)
            self.check_word_button.draw(self.screen)
            self.image_btn.draw(self.screen)
            for elem in self.buttons:
                elem.draw(self.screen)

            pg.display.update()
        return self.state