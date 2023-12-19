# This code loads Pygame and a JSON file, setting constants based on the JSON content.
# It defines classes and functions to handle buttons, symbols, and their graphical representation.
import pygame as pg
import json

# The 'config.json' file is opened and its content is loaded into the 'constants' variable.
with open("config.json", "r") as json_file:
    constants = json.loads(json_file.read())


# The 'set_background' function sets the background image for the screen.
def set_background(screen, image_path):
    background = pg.image.load(image_path)
    screen.blit(background, (0, 0))


# The 'SymbolButton' class represents symbols as interactive buttons on the screen.
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
        pg.draw.rect(
            screen, self.button_color, (self.x, self.y, self.width, self.height)
        )
        font = pg.font.Font(None, self.font)
        text_surface = font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect()
        text_rect.center = (self.x + self.width // 2, self.y + self.height // 2)
        screen.blit(text_surface, text_rect)

    def is_clicked(self, position):
        x, y = position
        return self.x < x < self.x + self.width and self.y < y < self.y + self.height


# The 'SymbolButton' class represents symbols as interactive buttons on the screen.
class SymbolButton:
    def __init__(self, symbol, position):
        self.x = position[0]
        self.y = position[1]
        self.image = pg.image.load(
            constants["IMGS_DIR"] + constants["SYMBOLS"][str(symbol)]
        )
        self.image_rect = self.image.get_rect()
        self.image_rect.center = (
            self.x + constants["FIELD_WIDTH"] // 2,
            self.y + constants["FIELD_HEIGHT"] // 2,
        )

    def draw(self, screen):
        pg.draw.rect(
            screen,
            constants["WHITE"],
            (self.x, self.y, constants["FIELD_WIDTH"], constants["FIELD_HEIGHT"]),
        )
        screen.blit(self.image, self.image_rect)

    def is_clicked(self, pos):
        x, y = pos
        if (
            self.x < x < self.x + constants["FIELD_WIDTH"]
            and self.y < y < self.y + constants["FIELD_HEIGHT"]
        ):
            self.action = 1
        return (
            self.x < x < self.x + constants["FIELD_WIDTH"]
            and self.y < y < self.y + constants["FIELD_HEIGHT"]
        )


# The 'draw_symbol' function handles the graphical display of symbols on the Pygame window.
def draw_symbol(symbol, position, screen):
    x, y = position
    image = pg.image.load(constants["IMGS_DIR"] + constants["SYMBOLS"][str(symbol)])
    image_rect = image.get_rect()
    image_rect.center = (
        x + constants["FIELD_WIDTH"] // 2,
        y + constants["FIELD_HEIGHT"] // 2,
    )
    pg.draw.rect(
        screen,
        constants["WHITE"],
        (x, y, constants["FIELD_WIDTH"], constants["FIELD_HEIGHT"]),
    )
    screen.blit(image, image_rect)


# The 'draw_row' function manages the graphical display of symbol rows within the Pygame window.
def draw_row(symbols, position, xspace, screen):
    for i, symbol in enumerate(symbols):
        temp_position = (
            position[0] + i * (xspace + constants["FIELD_WIDTH"]),
            position[1],
        )
        draw_symbol(symbol, temp_position, screen)


# The 'draw_pegs' function handles the graphical display of pegs within the Pygame window.
def draw_pegs(pegs, position, screen):
    peg_color = [
        constants["WHITE"],
        constants["WHITE"],
        constants["WHITE"],
        constants["WHITE"],
    ]
    for i in range(0, pegs[0]):
        peg_color[i] = constants["RED"]
    for i in range(pegs[0], pegs[1] + pegs[0]):
        peg_color[i] = constants["YELLOW"]
    for y in range(2):
        for x in range(2):
            temp_position = (position[0] + x * 40, position[1] + y * 36)
            pg.draw.circle(screen, peg_color[x + y * 2], temp_position, 6)


# The 'draw_table' function is responsible for displaying symbol tables within the Pygame window.
def draw_table(symbols_list, pegs, position, xspace, yspace, screen):
    for i, symbols in enumerate(symbols_list):
        temp_position = (
            position[0],
            position[1] + i * (yspace + constants["FIELD_WIDTH"]),
        )
        draw_row(symbols, temp_position, xspace, screen)
        temp_position = (
            position[0] + 4 * (xspace + constants["FIELD_WIDTH"]) + 10,
            position[1] + i * (yspace + constants["FIELD_HEIGHT"]) + 12,
        )
        draw_pegs(pegs[i], temp_position, screen)
    pass


# The 'draw_symbol_buttons' function manages the graphical representation of symbol buttons on the Pygame window.
def draw_symbol_buttons(symbols_buttons, screen):
    for i in range(2):
        for j in range(3):
            symbols_buttons[i * 3 + j].draw(screen)
    pass


# The 'draw_text' function handles the graphical display of text within the Pygame window.
def draw_text(text, size, color, position, screen):
    font = pg.font.Font(None, size)
    text_render = font.render(text, True, color)
    text_rect = text_render.get_rect()
    text_rect.center = position
    screen.blit(text_render, text_rect)
