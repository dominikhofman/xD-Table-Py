import time
from udp import UdpInterface

import constants
from random import randint
from display import Color, Board


class Piece(object):
    def __init__(self, board):
        self.x = 3
        self.y = 0
        self.rotation = 0
        self.board = board

        # random shape
        self.shape = constants.shapes[randint(0, len(constants.shapes) - 1)]

        # random color
        self.color = randint(1, len(constants.colors) - 1)

    def draw(self, board=None, fill=None):
        if board is None:
            board = self.board

        if fill is None:
            fill = self.color

        shape = self.shape[self.rotation]
        # draw new position
        for dy, row in enumerate(shape):
            for dx, col in enumerate(row):
                if col:
                    board.set(self.x + dx, int(self.y + dy), fill)

    def can_move(self, dx, dy, rotation=None):
        # check if custom rotation is applied
        if rotation is None:
            shape = self.shape[self.rotation]
        else:
            shape = self.shape[rotation]

        # check if can move by vector dx, dy
        for ddy, row in enumerate(shape):
            for ddx, col in enumerate(row):
                if col:
                    nx = self.x + dx + ddx
                    ny = self.y + dy + ddy
                    ny = int(ny)
                    if nx > self.board.width - 1 or \
                       nx < 0 or \
                       ny > self.board.height - 1 or \
                       self.board.get(nx, ny):
                        return False
        return True

    def move(self, dx, dy, rotation=None):
        if not self.can_move(dx, dy, rotation):
            return False

        self.y += dy
        self.x += dx
        if rotation is not None:
            self.rotation = rotation

        return True

    def rotate(self, direction):
        new_rotation = (self.rotation + direction) % 4
        self.move(0, 0, new_rotation)

    def persist(self):
        self.draw()


class Tetris(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.reset()

    def step(self, dt):
        if not self.current_piece.move(0, 1 * dt):
            self.current_piece.persist()
            if not self.spawn_piece():
                print("GAME OVER!!!@#!@$!@%@!%!%@")
                self.reset()
            self.check_lines()

    def spawn_piece(self):
        self.current_piece = Piece(self.board)
        return self.current_piece.can_move(0, 0)

    def render(self, display):
        for y in range(display.height):
            for x in range(display.width):
                display.set(x, y, constants.colors[self.board.get(x, y)])

        self.current_piece.draw(display, constants.colors[self.current_piece.color])

    def check_lines(self):
        for y in range(self.board.height):
            for x in range(self.board.width):
                if not self.board.get(x, y):
                    break
            else:
                self.erase_line(y)

    def erase_line(self, n):
        for y in reversed(range(1, n + 1)):
            for x in range(self.board.width):
                self.board.set(x, y, self.board.get(x, y - 1))

    def reset(self):
        self.board = Board(self.width, self.height)
        self.spawn_piece()

    def on_press(self, key):
        if key == 'a':
            self.current_piece.move(-1, 0)

        if key == 'd':
            self.current_piece.move(1, 0)

        if key == 's':
            self.current_piece.move(0, 1)

        if key == 'r':
            self.current_piece.rotate(1)

        if key == 't':
            self.current_piece.rotate(-1)

        if key == 'n':
            self.reset()
