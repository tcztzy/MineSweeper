import random
import turtle

char_0 = '''\
 *** 
*  **
* * *
**  *
*   *
 *** '''
char_1 = '''\
  *  
 **  
  *  
  *  
  *  
 *** '''
char_2 = '''\
 *** 
*   *
   * 
  *  
 *   
*****'''
char_3 = '''\
*****
    *
  ** 
    *
*   *
 *** '''
char_4 = '''\
   * 
  ** 
 * * 
*  * 
*****
   * '''
char_5 = '''\
*****
*    
**** 
    *
*   *
 *** '''
char_6 = '''\
 *** 
*    
**** 
*   *
*   *
 *** '''
char_7 = '''\
*****
    *
   * 
  *  
  *  
  *  '''
char_8 = '''\
 *** 
*   *
 *** 
*   *
*   *
 *** '''
char_9 = '''\
 *** 
*   *
*   *
 ****
    *
 *** '''
char_numbers = [char_0, char_1, char_2, char_3, char_4,
                char_5, char_6, char_7, char_8, char_9]


class MyTurtle(turtle.Turtle):
    def setpen(self, *coordinate):
        self.penup()
        self.goto(*coordinate)
        self.pendown()
        self.setheading(0)

    def rectangle(self, coordinate, width, height=None, fill_color='gray', border_color='black'):
        if height is None:
            height = width
        self.setpen(coordinate)
        self.color(border_color)
        self.fillcolor(fill_color)
        self.begin_fill()
        for i in range(4):
            self.forward(width if i % 2 == 0 else height)
            self.right(90)
        self.end_fill()

    def square(self, coordinate, length, fill_color='gray', border_color='black'):
        self.rectangle(coordinate, length, fill_color=fill_color, border_color=border_color)

    def draw_char(self, coordinate, char, color, border_color='black', pixel=5):
        x, y = coordinate
        for i, row in enumerate(char.split('\n')):
            offset_y = y - i * pixel
            for j, c in enumerate(row):
                offset_x = x + j * pixel
                if c == ' ':
                    pass
                else:
                    self.square((offset_x, offset_y), pixel, color, border_color)


class MineSweeper(object):
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

    def new_game(self):
        l = self.mine_grid_length
        for r in range(self.row):
            for c in range(self.col):
                self.turtle.square((c*l-self.col*l/2, r*l-self.row*l/2+l), l)
        self.turtle.square((-l/2, self.row*l/2+1.5*l), l, 'yellow')


if __name__ == '__main__':
    mt = MyTurtle()
    mt.tracer(10000, 0.0001)
    minesweeper = MineSweeper(t=mt)
    turtle.done()
