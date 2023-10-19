import pygame as pg
import sys

IMGS_DIR = "./Slagalica/imgs"


# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
FONT_SIZE = 36

pg.font.init()
# Create the screen
# screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# pg.display.set_caption("Arcade Game")

# Create a font
font = pg.font.Font(None, FONT_SIZE)
# background_path = IMGS_DIR + "/background.jpg"
# Function to set the background
def set_background(screen, image_path):
    background = pg.image.load(image_path)
    screen.blit(background, (0, 0))

# Function to display text on the screen
def display_text(screen, text, x, y):
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

class Button:
    def __init__(self, x, y, width, height, text, font, text_color, button_color, action=0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.font = font
        self.text_color = text_color
        self.button_color = button_color
        self.action = action

    def draw(self, screen):
        pg.draw.rect(screen, self.button_color, (self.x, self.y, self.width, self.height))
        font = pg.font.Font(None, self.font)
        text_surface = font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect()
        text_rect.center = (self.x + self.width // 2, self.y + self.height // 2)
        screen.blit(text_surface, text_rect)

    def is_clicked(self, pos):
        x, y = pos
        if self.x < x < self.x + self.width and self.y < y < self.y + self.height:
            self.button_color = (0, 255, 255)
            self.action = 1
        return self.x < x < self.x + self.width and self.y < y < self.y + self.height