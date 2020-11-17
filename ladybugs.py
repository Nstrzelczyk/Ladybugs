#! python3
# coding=utf-8

import pygame
import pygame.locals
import os
import random
import math


class Board(object):
    """
    Game board. Responsible for drawing the game window.
    """

    def __init__(self, width, height):
        """
        Game board constructor.

        :param width:
        :param height:
        """
        self.surface = pygame.display.set_mode((width, height), 0, 32)
        pygame.display.set_caption('Ladybug')
        # Font PyGame
        pygame.font.init()
        font_path = pygame.font.match_font('arial')
        self.font = pygame.font.Font(font_path, 64)

    def draw(self, *args):
        """
        Draws the game windows

        :param args: list of object to draw
        """
        background = (100, 50, 205)
        self.surface.fill(background)
        for drawable in args:
            drawable.draw_on(self.surface)

        pygame.display.update()

    def draw_text(self, surface, text, x, y):
        """
        Draws the indicated text at the indicated location
        """
        text = self.font.render(text, True, (150, 150, 150))
        rect = text.get_rect()
        rect.center = x, y
        surface.blit(text, rect)


class Game():
    """
    Brings all the elements of the game together.
    """

    def __init__(self, width, height):
        pygame.init()
        self.board = Board(width, height)
        # the clock with we will use to control the speed off drawing
        # consecutive frames of the game
        self.fps_clock = pygame.time.Clock()

    def run(self):
        pygame.key.set_repeat(50, 25)
        """
        Main program loop.
        """
        while not self.handle_events():
            self.board.draw()
    # loop until receiving a signal to output.

    def handle_events(self):
        """
                Handling system events.
                """
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                return True
            pygame.key.get_pressed()


# class Player():
#
#     def __init__(self):
#
#     def move(self):
#
#
# class Ladybug():
#
#     def __init__(self):
#
#     def move(self):
#
# class Judge():


# This part should always be at the end of the module, we want to start our game only after all classes are declared.
if __name__ == "__main__":
    game = Game(600, 600)
    game.run()
