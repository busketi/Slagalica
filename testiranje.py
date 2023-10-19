import pygame as pg
from pgu import gui

# Initialize Pygame
pg.init()

# Create a Pygame screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Create a PGU desktop
desktop = gui.Desktop()

# Create a button
button = gui.Button("Click Me")

# Set the button's position
button.topleft = 300, 200

# Add the button to the desktop
desktop.widgets.append(button)

# Main loop
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            desktop.event(event)

    screen.fill((0, 0, 0))
    print(desktop)
    desktop.paint()
    pg.display.flip()

pg.quit()
