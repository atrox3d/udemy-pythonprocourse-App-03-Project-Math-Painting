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
