import numpy as np
from PIL import Image


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


canvas = Canvas(
    height=20,
    width=30,
    color=(255, 255, 255)
)
