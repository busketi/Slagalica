import pygame as pg
import sys
from utils import *
from solver import *
import random
import json


def main():
    # Initialize Pygame
    pg.init()

    # Constants
    with open("config.json", "r") as json_file:
        constants = json.loads(json_file.read())

    # Initialize the Pygame screen based on configuration constants.
    SCREEN = pg.display.set_mode(
        (constants["SCREEN_WIDTH"], constants["SCREEN_HEIGHT"])
    )
    # Create various buttons based on configuration constants.
    random_btn = Button(
        (650, 50), 100, 40, "RANDOM", 24, constants["BLACK"], constants["YELLOW"]
    )
    solve_btn = Button(
        (650, 130), 100, 40, "SOLVE", 24, constants["BLACK"], constants["GREEN"]
    )
    quit_btn = Button(
        (1300, 630), 60, 30, "quit", 24, constants["WHITE"], constants["BLACK"]
    )

    # Other initializations based on configuration constants.
    line_position = (0, 300)
    symbol_buttons = list()
    solution = [0, 1, 2, 3]
    knuth_symbols = [[5 for _ in range(4)] for _ in range(5)]
    knuth_pegs = [(0, 0) for _ in range(5)]
    my_alg_symbols = [[5 for _ in range(4)] for _ in range(5)]
    my_alg_pegs = [(0, 0) for _ in range(5)]

    # Create symbol buttons based on configuration constants.
    for i in range(2):
        for j in range(3):
            symbol_buttons.append(
                SymbolButton(
                    i * 3 + j,
                    (
                        800 + j * (constants["FIELD_WIDTH"] + 20),
                        40 + i * (constants["FIELD_HEIGHT"] + 20),
                    ),
                )
            )

    while True:
        # Event handling loop for Pygame
        for event in pg.event.get():
            # Check if the 'QUIT' event was triggered
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            # Check if a key was released and if it was the 'Escape' key
            if event.type == pg.KEYUP:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()
            # Check if the mouse button was released
            if event.type == pg.MOUSEBUTTONUP:
                mouse_pos = pg.mouse.get_pos()
                # Check if the 'quit' button was clicked
                if quit_btn.is_clicked(mouse_pos):
                    pg.quit()
                    sys.exit()
                # Check if the 'random' button was clicked
                if random_btn.is_clicked(mouse_pos):
                    solution = [random.randint(0, 5) for _ in range(4)]
                    continue
                # Check if the 'solve' button was clicked
                if solve_btn.is_clicked(mouse_pos):
                    knuth_symbols, knuth_pegs = solve(solution, knuth_score)
                    my_alg_symbols, my_alg_pegs = solve(solution, my_alg_score)
                    continue
                # Check if any symbol button was clicked
                for symbol, btn in enumerate(symbol_buttons):
                    if btn.is_clicked(mouse_pos):
                        solution[line_position[0]] = symbol
                        line_position = (
                            (line_position[0] + 1) % 4,
                            300 + (line_position[1] - 300 + 80) % 320,
                        )
                    continue

        # Drawing on the screen based on the game's state
        set_background(SCREEN, constants["BACKGROUND_PATH"])
        random_btn.draw(SCREEN)
        solve_btn.draw(SCREEN)
        quit_btn.draw(SCREEN)
        draw_text("KNUTH", 36, constants["WHITE"], (350, 230), SCREEN)
        draw_text("MY ALGORITHM", 36, constants["WHITE"], (1020, 230), SCREEN)
        draw_row(solution, (300, 80), 20, SCREEN)
        draw_symbol_buttons(symbol_buttons, SCREEN)
        draw_table(knuth_symbols, knuth_pegs, (200, 280), 20, 20, SCREEN)
        draw_table(my_alg_symbols, my_alg_pegs, (850, 280), 20, 20, SCREEN)

        pg.draw.line(
            SCREEN,
            constants["RED"],
            (line_position[1], 146),
            (line_position[1] + 60, 146),
            6,
        )

        pg.display.update()


if __name__ == "__main__":
    main()
