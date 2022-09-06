from PIL import Image
import numpy as np


class Canvas:

    def __init__(self, height, width, color):
        self.height = height
        self.width = width
        self.color = color

        self.data = np.zeros(                           # create zero-filled matrix
            (                                           # from tuple, 3 dimensions
                self.height,                            # vertical
                self.width,                             # horizontal
                3                                       # depth         3 cells
            ),
            dtype=np.uint8                              # set cell type to int
        )
        self.data[:] = self.color                       # set all cells to color

    def make(self, imagepath):
        img = Image.fromarray(self.data, 'RGB')
        img.save(imagepath)


class Rectangle:

    def __init__(self, row, column, height, width, color):
        self.row = row
        self.column = column
        self.height = height
        self.width = width
        self.color = color

    def draw(self, canvas):
        canvas.data[                                    # slicing with tuple
            self.row:                                   # first dimension: from row
            self.row + self.height                      # to row + height
            ,                                           # comma for tuple
            self.column:                                # second dimension: from col
            self.column + self.width                    # to col + width
        ] = self.color


class Square:
    def __init__(self, row, column, side, color):
        self.row = row
        self.column = column
        self.side = side
        self.color = color

    def draw(self, canvas):
        canvas.data[
            self.row:                                   # slicing with tuple
            self.row + self.side                        # first dimension: from row
            ,                                           # to row + side
            self.column:                                # comma for tuple
            self.column + self.side                     # second dimension: from col
        ] = self.color                                  # to col + side


canvas = Canvas(
    height=20,
    width=30,
    color=(255, 255, 255)
)

r1 = Rectangle(row=1, column=6, height=7, width=10, color=(100, 200, 125))
r1.draw(canvas)
s1 = Square(row=1, column=3, side=3, color=(0, 100, 222))
s1.draw(canvas)
canvas.make('test.png')

