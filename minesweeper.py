import random
from turtle import *
import json

with open('char.json') as f:
    char = json.load(f)


class MyTurtle(Turtle):
    def setpen(self, *coordinate):
        self.penup()
        self.goto(*coordinate)
        self.pendown()
        self.setheading(0)

    def rectangle(self, x, y, width, height=None, fill_color='gray', border_color='black'):
        if height is None:
            height = width
        self.setpen(x, y)
        self.color(border_color)
        self.fillcolor(fill_color)
        self.begin_fill()
        for i in range(4):
            self.forward(width if i % 2 == 0 else height)
            self.right(90)
        self.end_fill()

    def square(self, x, y, length, fill_color='gray', border_color='black'):
        self.rectangle(x, y, length, fill_color=fill_color, border_color=border_color)

    def draw_char(self, x, y, char, color, background_color=None, pixel=5):
        for i, row in enumerate(char.split('\n')):
            offset_y = y - i * pixel
            for j, c in enumerate(row):
                offset_x = x + j * pixel
                if c == ' ':
                    if background_color is None:
                        continue
                    self.square(offset_x, offset_y, pixel, background_color, background_color)
                else:
                    self.square(offset_x, offset_y, pixel, color, color)

    def write_sentence(self, x, y, sentence, color, background_color=None, pixel=5, break_line=300):
        x_pos = x
        y_pos = y
        line_height = max(map(lambda c: len(char[c].split('\n')), sentence)) * pixel
        if background_color is not None:
            background_height = max(map(lambda c: len(char[c].split('\n')), sentence)) * pixel
            background_width = (sum(map(lambda c: max(map(len, char[c].split('\n'))), sentence)) + len(sentence)-1) * pixel
            self.rectangle(x, y, background_width, background_height, background_color, background_color)
        for i, c in enumerate(sentence):
            char_width = max(map(len, char[c].split('\n')))
            char_height = len(char[c].split('\n'))
            self.draw_char(x_pos, y_pos, char[c], color, None, pixel)
            x_pos += (char_width + 1) * pixel
            if x_pos - x >= break_line:
                y_pos -= line_height + pixel
                x_pos = x


class MineSweeper(object):
    need_new_game = True

    def __init__(self, level="primary", t=None):
        self.turtle = t
        if level == "primary":
            self.row = 9
            self.col = 9
            self.mine = 10
            self.mine_grid_length = 60
        else:
            raise ValueError
        self.new_game()

    def __call__(self, x, y):
        l = self.mine_grid_length
        grid_x = int((x+270)//60)
        grid_y = int((y+210)//60) + 1
        if -l/2 <= x <= l/2 and self.row*l/2+0.5*l <= y <= self.row*l/2+1.5*l:
            self.new_game()

    def new_game(self):
        print('New Game!')
        l = self.mine_grid_length
        for r in range(self.row):
            for c in range(self.col):
                self.turtle.square(c*l-self.col*l/2, r*l-self.row*l/2+l, l)
        self.turtle.square(-l/2, self.row*l/2+1.5*l, l, 'yellow')
        self.need_new_game = False

if __name__ == '__main__':
    screen = Screen()
    mt = MyTurtle()
    screen.tracer(False)
    game = MineSweeper(t=mt)
    screen.onscreenclick(game)
    screen.mainloop()
