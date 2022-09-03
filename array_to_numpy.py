import numpy as np
from PIL import Image

# three dimension matrix
################################################################################
#                                    |  R
#                                    |  O
#                                    |  W
#   ROWS             DEPTH           |  S
#    0 1 2 3 4 : 5    0 1 2 : 3      |
#   +-+-+-+-+-+      +-+-+-+         |  A   B  B  B  B   COLUMNS
# 0 | | | | | |----->| | | |         | [0] [0, 1, 2, 3]
#   +-+-+-+-+-+      +-+-+-+         | [1] [0, 1, 2, 3]
# 1 | | | | | |      | | | |         | [2] [0, 1, 2, 3]
#   +-+-+-+-+-+      +-+-+-+         | [3] [0, 1, 2, 3]
# 2 | | | | | |      | | | |         | [4] [0, 1, 2, 3]
#   +-+-+-+-+-+      +-+-+-+         |     [0][0][0][0]
# 3 | | | | | |      | | | |         |     [1][1][1][1]
#   +-+-+-+-+-+      +-+-+-+         |     [2][2][2][2]
# 4 total    |                       |      C  C  C  C   CELLS
#            |                       |
#   COLS    \|/                      |
#   +-+-+-+-+-+                      |
# 0 | | | | | |                      |
#   +-+-+-+-+-+                      |
# 1 | | | | | |                      |
#   +-+-+-+-+-+                      |
# 2 | | | | | |                      |
#   +-+-+-+-+-+                      |
# 3 total                            |
#
################################################################################
#
# all the matrix : matrix[:]       = 0                                          5 rows * 4 columns * 3 cells
# a row          : matrix[A]       = [[0, 0, 0],[0, 0, 0],[0, 0, 0],[0, 0, 0]]  4 columns * 3 cells
# row/col        : matrix[A][B]    = [0, 0, 0]                                  3 cells
# single cell    : matrix[A][B][C] = 0                                          1 cell
#
# data[0] = [[255, 255, 0], [255, 255, 0], [255, 255, 0], [255, 255, 0]]
# data[0][0] = [255, 255, 0]
# data[0][0][0] = 255
################################################################################

data = np.zeros(                    # create zero-filled matrix
    (                               # from tuple, 3 dimensions
        5,                          # horizontal    5 rows
        4,                          # vertical      4 columns
        3                           # depth         3 cells
    ),
    dtype=np.uint8                  # set cell type to int
)

data[:] = [255, 255, 0]             # set all rows/columns to yellow
print(data)

img = Image.fromarray(data, 'RGB')  # create RGB image using data
img.save('canvas.png')              # save image to file

