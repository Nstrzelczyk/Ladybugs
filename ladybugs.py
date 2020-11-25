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


class Game(object):
    """
    Brings all the elements of the game together.
    """

    def __init__(self, width, height):
        pygame.init()
        self.board = Board(width, height)
        self.player1 = Player(x=300, y=300)
        self.bug = Ladybug(x=100, y=100)
        # the clock with we will use to control the speed off drawing
        # consecutive frames of the game
        self.fps_clock = pygame.time.Clock()

    def run(self):
        pygame.key.set_repeat(50, 25)
        """
        Main program loop.
        """
        while not self.handle_events():
            self.board.draw(
                self.player1,
                self.bug
            )
    # loop until receiving a signal to output.

    def handle_events(self):
        """
                Handling system events.
                """
        for event in pygame.event.get():
            step = 8
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                return True
            pygame.key.get_pressed()
            if event.type == pygame.KEYDOWN:
                poz_x = self.player1.x
                poz_y = self.player1.y
                if event.key == pygame.K_LEFT:
                    self.player1.x -= step
                    if self.player1.x < 0:
                        self.player1.x = 0
                elif event.key == pygame.K_RIGHT:
                    self.player1.x += step
                    if self.player1.x > 600 - (self.player1.width)/2:
                        self.player1.x = 600 - (self.player1.width)/2
                if event.key == pygame.K_UP:
                    self.player1.y -= step
                    if self.player1.y < 0:
                        self.player1.y = 0
                elif event.key == pygame.K_DOWN:
                    self.player1.y += step
                    if self.player1.y > 600 - (self.player1.height)/2:
                        self.player1.y = 600 - (self.player1.height)/2
                    # self.player1.move(step)
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

    def blit(graphics, param):
        pass

# class Drawable(object):
#     """
#     Base class for drawn objects
#     """
#
#     def __init__(self, width, height, x, y, color=(0, 255, 0)):
#         self.width = width
#         self.height = height
#         self.surface = pygame.Surface([width, height], pygame.SRCALPHA, 32).convert_alpha()
#         self.rect = self.surface.get_rect(x=x, y=y)
#
#     def draw_on(self, surface):
#         surface.blit(self.surface, self.rect)


class Player(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.height = 50
        self.width = 50
        self.shape = pygame.Rect(self.x, self.y, self.width, self.height)
        self.graphics = pygame.image.load(os.path.join('playerbug.png'))

    def draw_on(self, surface):
        surface.blit(self.graphics, (self.x, self.y))

    def move(self, v):
        self.y = self.y + v
        self.x = self.x + v
        self.shape = pygame.Rect(self.x, self.y, self.width, self.height)


class Ladybug(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.height = 50
        self.width = 50
        self.shape = pygame.Rect(self.x, self.y, self.width, self.height)
        self.graphics = pygame.image.load(os.path.join('ladybug.png'))

    def draw_on(self, surface):
        surface.blit(self.graphics, (self.x, self.y))

    def move(self, v):
        self.y = self.y + v
        self.x = self.x + v
        self.shape = pygame.Rect(self.x, self.y, self.width, self.height)
#
# class Judge():


# This part should always be at the end of the module, we want to start our game only after all classes are declared.
if __name__ == "__main__":
    game = Game(600, 600)
    game.run()
