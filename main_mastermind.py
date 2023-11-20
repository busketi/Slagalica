import pygame as pg
import sys
from utils import *
from longestword import *
from mastermind import *

# IMGS_DIR = "./Slagalica/imgs"
IMGS_DIR = "./imgs"
# Initialize Pygame
pg.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
FONT_SIZE = 36

SYMBOLS = {
    0: "/diamond.png",
    1: "/heart.png",
    2: "/clover.png",
    3: "/skocko.png",
    4: "/spade.png",
    5: "/star.png"
}

background_path = IMGS_DIR + "/background.jpg"

SCREEN = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))



class ImageButton:
    def __init__(self, x, y, width, height, button_color, image_path, action=0):
        self.x = x
        self.y = y
        self.image = pg.image.load(image_path)
        self.image_rect = self.image.get_rect()
        self.image_rect.center = (x + width // 2, y + height // 2)
        self.width = width
        self.height = height
        self.button_color = button_color
        self.action = action

    def draw(self, screen):
        pg.draw.rect(screen, self.button_color, (self.x, self.y, self.width, self.height))
        screen.blit(self.image, self.image_rect)

    def is_clicked(self, pos):
        x, y = pos
        if self.x < x < self.x + self.width and self.y < y < self.y + self.height:
            self.button_color = (0, 255, 255)
            self.action = 1
        return self.x < x < self.x + self.width and self.y < y < self.y + self.height
    

def draw_symbol(symbol, postion, size):
    

def draw_row(symbols, postion, xspace, size):


def draw_table(symbols_list, postion, xspace, yspace, size):



random_btn = Button(500, 500, 200, 50, "Random", 24, (255, 255, 255), (0, 0, 255))
solve_btn = Button(600, 400,  50, 50, "Solve", 35, (255, 255, 255), (0, 255, 0))


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RETURN:
                # Start the game (you can replace this with your game code)
                # self.state = 'longest_word'
                print("Starting the game!")
            if event.key == pg.K_qq:
                # Quit the game
                pg.quit()
                sys.exit()


    set_background(SCREEN, background_path)
    random_btn.draw(SCREEN)
    solve_btn.draw(SCREEN)



    pg.display.update()