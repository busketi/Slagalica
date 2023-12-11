import pygame as pg
import sys

def set_background(screen, image_path):
    background = pg.image.load(image_path)
    screen.blit(background, (0, 0))

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

    def draw(self, screen):
        pg.draw.rect(SCREEN, WHITE, (self.x, self.y, FIELD_WIDTH, FIELD_HEIGHT))
        screen.blit(self.image, self.image_rect)

    def is_clicked(self, pos):
        x, y = pos
        if self.x < x < self.x + FIELD_WIDTH and self.y < y < self.y + FIELD_HEIGHT:
            self.action = 1
        return self.x < x < self.x + FIELD_WIDTH and self.y < y < self.y + FIELD_HEIGHT