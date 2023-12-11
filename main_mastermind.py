import pygame as pg
import sys
from utils import *
from solver import *

# IMGS_DIR = "./Slagalica/imgs"
IMGS_DIR = "./imgs"
# Initialize Pygame
pg.init()

# Constants
SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 700

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

def draw_row(symbols, position, xspace):
    for i,symbol in enumerate(symbols):
        temp_position = (position[0]+i*(xspace+FIELD_WIDTH),position[1])

        # print(temp_position)
        draw_symbol(symbol, temp_position)

def draw_pegs(pegs, position):
    peg_color = [WHITE, WHITE, WHITE, WHITE]
    # print(pegs[0])
    # print(type(peg_color))
    # print(len(peg_color))
    for i in range(0,pegs[0]):
        peg_color[i]=RED
    for i in range(pegs[0],pegs[1]+pegs[0]):
        peg_color[i]=YELLOW
    # print(peg_color)
    # print(len(peg_color))
    for y in range(2):
        for x in range(2):
            temp_position = (position[0]+x*40,position[1]+y*36)
            pg.draw.circle(SCREEN, peg_color[x+y*2], temp_position, 6)

def draw_table(symbols_list, pegs, position, xspace, yspace):
    for i,symbols in enumerate(symbols_list):
        temp_position = (position[0],position[1]+i*(yspace+FIELD_WIDTH))
        draw_row(symbols, temp_position, xspace)
        temp_position = (position[0]+4*(xspace+FIELD_WIDTH)+10,position[1]+i*(yspace+FIELD_WIDTH)+12)
        draw_pegs(pegs[i], temp_position)
    pass

def draw_symbol_buttons(symbols_buttons):
    for i in range(2):
        for j in range(3):
            symbols_buttons[i*3+j].draw()
    pass


def draw_text(text, size, color, position):
    font = pg.font.Font(None, size)  # None uses the default system font
    text_render = font.render(text, True, color)
    text_rect = text_render.get_rect()
    text_rect.center = position
    SCREEN.blit(text_render, text_rect)


random_btn = Button((650, 50), 100, 40, "RANDOM", 24, BLACK, YELLOW)
solve_btn = Button((650, 130), 100, 40, "SOLVE", 24, BLACK, GREEN)
# erase_btn = Button((650, 150), 100, 40, "<<", 35, BLACK, RED)
line_position = (0,300)
symbol_buttons = list()
solution = [0,1,2,3]
knuth_symbols = [[5 for _ in range(4)] for _ in range(5)]
knuth_pegs = [(0,0) for _ in range(5)]
my_alg_symbols = [[5 for _ in range(4)] for _ in range(5)]
my_alg_pegs = [(0,0) for _ in range(5)]

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
            if solve_btn.is_clicked(mouse_pos):
                knuth_symbols, knuth_pegs = solve(solution,knuth_score)
                my_alg_symbols, my_alg_pegs = solve(solution,my_alg_score)
                # pg.event.clear()
            for symbol,btn in enumerate(symbol_buttons):
                if btn.is_clicked(mouse_pos):
                    solution[line_position[0]] = symbol
                    line_position = ((line_position[0]+1)%4,300+(line_position[1]-300+80)%320)


    set_background(SCREEN, background_path)
    random_btn.draw(SCREEN)
    solve_btn.draw(SCREEN)
    draw_text("KNUTH", 36, WHITE, (350,230))
    draw_text("MY ALGORITHM", 36, WHITE, (1020,230))

    # erase_btn.draw(SCREEN)
    # draw_symbol(0,(200,200),"a")
    # draw_symbol(1,(280,200),"a")
    # draw_symbol(2,(360,200),"a")
    # draw_symbol(3,(440,200),"a")
    # draw_symbol(4,(520,200),"a")

    # draw_row([0,0,0],(200,100),70,"a")
    draw_row(solution,(300,80),20)
    draw_symbol_buttons(symbol_buttons)
    draw_table(knuth_symbols, knuth_pegs, (200,280),20,20)
    draw_table(my_alg_symbols, my_alg_pegs, (850,280),20,20)

    pg.draw.line(SCREEN, RED, (line_position[1],146), (line_position[1]+60,146), 6) 
    # draw_table([[0,0,0],[0,0,0]],(200,100),15,15)


    pg.display.update()