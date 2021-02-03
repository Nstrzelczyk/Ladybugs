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
        background = (40, 120, 40)
        self.surface.fill(background)
        for drawable in args:
            drawable.draw_on(self.surface)

        pygame.display.update()


class Text(object):

    def __init__(self, board):
        self.board = board
        # Font PyGame
        pygame.font.init()
        font_path = pygame.font.match_font('arial')
        self.font = pygame.font.Font(font_path, 48)

    def draw_text(self, surface, text, x, y):
        """
        Draws the indicated text at the indicated location
        """
        text = self.font.render(text, True, (200, 150, 150))
        rect = text.get_rect()
        rect.center = x, y
        surface.blit(text, rect)

    def draw_on(self, surface):
        """
        Draws the indicated text at the indicated location.
        """
        height = self.board.surface.get_height()
        width = self.board.surface.get_width()
        self.draw_text(surface, "Press SPACE to start", width/2, height/2)


class Game(object):
    """
    Brings all the elements of the game together.
    """
    def __init__(self, width, height,display):
        pygame.init()
        self.width = width
        self.height = height
        self.display = display
        self.board = Board(width, height)
        self.player1 = Player(x=width/2, y=height/2)
        self.player_start = Player(x=width/3, y=height/4)
        self.bug_start = Ladybug(x=width*2/3, y=height/4, vx=0, vy=0)
        self.start_text = Text(self.board)
        self.invasion = []
        for i in range(5):
            self.bug = Ladybug(x=random.randint(0, self.width), y=random.randint(50, self.height - 50),
                               vx=random.randint(-4, 4), vy=random.randint(-4, 4))
            self.invasion.append(self.bug)


        # the clock with we will use to control the speed off drawing
        # consecutive frames of the game
        self.fps_clock = pygame.time.Clock()

    def run(self):
        pygame.key.set_repeat(50, 25)
        """
        Main program loop.
        """
        while not self.handle_events():
            if self.display == "Menu":
                self.board.draw(
                    self.player_start,
                    self.bug_start,
                    self.start_text
                )
            elif self.display == "Play game":
                self.board.draw(
                    self.player1,
                    self.invasion[0],
                    self.invasion[1],
                    self.invasion[2],
                    self.invasion[3],
                    self.invasion[4]
                )
            elif self.display == "End":
                self.board.draw(
                    self.player_start,
                    self.bug_start
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
                if event.key == pygame.K_LEFT:
                    self.player1.x -= step
                    if self.player1.x < 0:
                        self.player1.x = 0
                elif event.key == pygame.K_RIGHT:
                    self.player1.x += step
                    if self.player1.x > self.width - self.player1.width/2:
                        self.player1.x = self.width - self.player1.width/2
                if event.key == pygame.K_UP:
                    self.player1.y -= step
                    if self.player1.y < 0:
                        self.player1.y = 0
                elif event.key == pygame.K_DOWN:
                    self.player1.y += step
                    if self.player1.y > self.height - self.player1.height/2:
                        self.player1.y = self.height - self.player1.height/2
                if event.key == pygame.K_SPACE:
                    if self.display != "Play game":
                        self.display = "Play game"
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
        if self.bug.collision(self.player1.shape):
            self.player1 = self.player_start
            self.bug = self.bug_start
            self.display = "End"

    def blit(self, graphics, param):
        pass


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


class Ladybug(object):

    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.height = 50
        self.width = 50
        self.vx = vx
        self.vy = vy
        self.shape = pygame.Rect(self.x, self.y, self.width, self.height)
        self.graphics = pygame.image.load(os.path.join('ladybug.png'))

    def draw_on(self, surface):
        surface.blit(self.graphics, (self.x, self.y))

    def move(self):
        self.x += self.vx
        self.y += self.vy
        if self.x <= 0 or self.x >= game.width:
            self.vx *= -1
        if self.y <= 0 or self.y >= game.height:
            self.vy *= -1


    def collision(self, player):
        if self.shape.colliderect(player):
            return True
        else:
            return False
#
# class Judge():


# This part should always be at the end of the module, we want to start our game only after all classes are declared.
if __name__ == "__main__":
    game = Game(600, 600, "Menu")
    game.run()
