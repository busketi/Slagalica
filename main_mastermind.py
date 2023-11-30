import pygame as pg
import sys
# from utils import *
from longestword import *
from mastermind import *

# IMGS_DIR = "./Slagalica/imgs"
IMGS_DIR = "./imgs"
# Initialize Pygame
pg.init()

# Constants
SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 600

WHITE = (255, 255, 255)
GREEN =  (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BLACK = (0,0,0)

FONT_SIZE = 36
FIELD_WIDTH = 60
FIELD_HEIGHT = 60

SYMBOLS = {
    0: "/spade.png",
    1: "/heart.png",
    2: "/clover.png",
    3: "/diamond1.png",
    4: "/star.png",
    5: "/skocko.png"
}

SIZES = {
    'small': {'size': 10, 'space': 5},
    'medium': {'size': 20, 'space': 10},
    'large': {'size': 30, 'space': 15}
}

background_path = IMGS_DIR + "/background.jpg"

SCREEN = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class Button:
    def __init__(self, position, width, height, text, font, text_color, button_color):
        self.x = position[0]
        self.y = position[1]
        self.width = width
        self.height = height
        self.text = text
        self.font = font
        self.text_color = text_color
        self.button_color = button_color

    def draw(self, screen):
        pg.draw.rect(screen, self.button_color, (self.x, self.y, self.width, self.height))
        font = pg.font.Font(None, self.font)
        text_surface = font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect()
        text_rect.center = (self.x + self.width // 2, self.y + self.height // 2)
        screen.blit(text_surface, text_rect)

    def is_clicked(self, position):
        x, y = position
        return self.x < x < self.x + self.width and self.y < y < self.y + self.height

class SymbolButton:
    def __init__(self, symbol, position):
        self.x = position[0]
        self.y = position[1]
        self.image = pg.image.load(IMGS_DIR+SYMBOLS[symbol])
        self.image_rect = self.image.get_rect()
        self.image_rect.center = (self.x + FIELD_WIDTH // 2, self.y + FIELD_HEIGHT // 2)

    def draw(self):
        pg.draw.rect(SCREEN, WHITE, (self.x, self.y, FIELD_WIDTH, FIELD_HEIGHT))
        SCREEN.blit(self.image, self.image_rect)

    def is_clicked(self, pos):
        x, y = pos
        if self.x < x < self.x + FIELD_WIDTH and self.y < y < self.y + FIELD_HEIGHT:
            self.action = 1
        return self.x < x < self.x + FIELD_WIDTH and self.y < y < self.y + FIELD_HEIGHT
    

def draw_symbol(symbol, position):
    x,y = position
    image = pg.image.load(IMGS_DIR+SYMBOLS[symbol])
    image_rect = image.get_rect()
    image_rect.center = (x + FIELD_WIDTH // 2, y + FIELD_HEIGHT // 2)
    pg.draw.rect(SCREEN, WHITE, (x, y, FIELD_WIDTH, FIELD_HEIGHT))
    SCREEN.blit(image, image_rect)
    pass

def draw_row(symbols, position, xspace):
    for i,symbol in enumerate(symbols):
        temp_position = (position[0]+i*(xspace+FIELD_WIDTH),position[1])

        # print(temp_position)
        draw_symbol(symbol, temp_position)
    # pass

def draw_table(symbols_list, position, xspace, yspace):
    for i,symbols in enumerate(symbols_list):
        temp_position = (position[0],position[1]+i*(yspace+FIELD_WIDTH))
        draw_row(symbols, temp_position, xspace)
    pass

def draw_symbol_buttons(symbols_buttons):
    for i in range(2):
        for j in range(3):
            symbols_buttons[i*3+j].draw()


             

random_btn = Button((650, 30), 100, 40, "RANDOM", 24, BLACK, YELLOW)
solve_btn = Button((650, 90), 100, 40, "SOLVE", 24, BLACK, GREEN)
erase_btn = Button((650, 150), 100, 40, "<<", 35, BLACK, RED)
line_position = (0,300)
symbol_buttons = list()
solution = [0,1,2,3]
for i in range(2):
    for j in range(3):
        symbol_buttons.append(SymbolButton(i*3+j,(800+j*(FIELD_WIDTH+20),40+i*(FIELD_HEIGHT+20))))
while True:
    for event in pg.event.get():
        # if event.type == pg.QUIT:
        #     pg.quit()
        #     sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RETURN:
                # Start the game (you can replace this with your game code)
                # self.state = 'longest_word'
                print("Starting the game!")
            if event.key == pg.K_q:
                # Quit the game
                pg.quit()
                sys.exit()
        if event.type == pg.MOUSEBUTTONUP:
            # check if hit start btn
            mouse_pos = pg.mouse.get_pos()
            if random_btn.is_clicked(mouse_pos):
            # Perform some action when the button is clicked
                solution = [random.randint(0, 5) for _ in range(4)]
                print("Random clicked!")
                continue
            for symbol,btn in enumerate(symbol_buttons):
                if btn.is_clicked(mouse_pos):
                    solution[line_position[0]] = symbol
                    line_position = ((line_position[0]+1)%4,300+(line_position[1]-300+80)%320)


    set_background(SCREEN, background_path)
    random_btn.draw(SCREEN)
    solve_btn.draw(SCREEN)
    erase_btn.draw(SCREEN)
    # draw_symbol(0,(200,200),"a")
    # draw_symbol(1,(280,200),"a")
    # draw_symbol(2,(360,200),"a")
    # draw_symbol(3,(440,200),"a")
    # draw_symbol(4,(520,200),"a")

    # draw_row([0,0,0],(200,100),70,"a")
    draw_row(solution,(300,80),20)
    draw_symbol_buttons(symbol_buttons)
    pg.draw.line(SCREEN, RED, (line_position[1],146), (line_position[1]+60,146), 6) 
    # draw_table([[0,0,0],[0,0,0]],(200,100),15,15)


    pg.display.update()