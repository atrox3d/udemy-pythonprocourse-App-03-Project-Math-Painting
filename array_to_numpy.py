import numpy as np
from PIL import Image

# three dimension matrix
################################################################################
# R                                |  R
# O                                |  O
# W                                |  W
# S COLUMNS          DEPTH         |  S
#    0 1 2 3 : 4    0 1 2 : 3      |
#   +-+-+-+-+      +-+-+-+         |  A   B  B  B  B   COLUMNS
# 0 | | | | |----->| | | |         | [0] [0, 1, 2, 3]
#   +-+-+-+-+      +-+-+-+         | [1] [0, 1, 2, 3]
# 1 | | | | |      | | | |         | [2] [0, 1, 2, 3]
#   +-+-+-+-+      +-+-+-+         | [3] [0, 1, 2, 3]
# 2 | | | | |      | | | |         | [4] [0, 1, 2, 3]
#   +-+-+-+-+      +-+-+-+         |     [0][0][0][0]
# 3 | | | | |      | | | |         |     [1][1][1][1]
#   +-+-+-+-+      +-+-+-+         |     [2][2][2][2]
# 4 | | | | |      | | | |         |      C  C  C  C   CELLS
#   +-+-+-+-+      +-+-+-+         |
# 4 total  |                       |
#          |                       |
#   COLS  \|/                      |
#   +-+-+-+-+                      |
# 0 | | | | |                      |
#   +-+-+-+-+                      |
# 1 | | | | |                      |
#   +-+-+-+-+                      |
# 2 | | | | |                      |
#   +-+-+-+-+                      |
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

data = np.zeros(                                    # create zero-filled matrix
    (                                               # from tuple, 3 dimensions
        5,                                          # horizontal    5 rows
        4,                                          # vertical      4 columns
        3                                           # depth         3 cells
    ),
    dtype=np.uint8                                  # set cell type to int
)

data[:] = [255, 255, 0]                             # set all rows/columns to yellow
print(data.shape)                                   # 5, 4, 3

# data[0:5:2] = [[255, 0, 0], [0, 255, 0], [0, 0, 255], [255, 0, 255]]

# [1:3]
# select rows 1 and 2, 3 excluded
#
# [    ]
# [****]
# [****]
# [    ]
# [    ]
#
# data[1:3] = [255, 0, 0]                           # set matrix/image rows to red


#
# [, :1:3]
# select all rows and columns 2 and 3, 4 excluded
#
# the comma implies function slice tuple:
# data[(slice(), slice(1,3))]
#
# [ ** ]
# [ ** ]
# [ ** ]
# [ ** ]
# [ ** ]
#
slice_all = slice(None)
slice_1and2 = slice(1, 3)
slice_allrows_cols1and2 = (slice(None), slice(1, 3))
# data[(slice(None), slice(1, 3))] = [255, 0, 0]      # set matrix/image rows 2 and 3 to red
# data[:, 1:3] = [255, 0, 0]                          # set matrix/image rows 2 and 3 to red

#
# [1:3, :1:3]
# select a square: rows 2 and 3, cols 2 and 3
#
# the comma implies function slice tuple:
# data[(slice(1, 3), slice(1, 3))]
#
# [    ]
# [ ** ]
# [ ** ]
# [    ]
# [    ]
#
slice_1and2 = slice(1, 3)
slice_square = (slice(1, 3), slice(1, 3))
# data[(slice(1, 3), slice(1, 3))] = [255, 0, 0]      # set matrix/image rows 2 and 3 to red
# data[1:3, 1:3] = [255, 0, 0]                          # set matrix/image rows 2 and 3 to red


#
# [    ]
# [ ** ]
# [ ** ]
# [ ** ]
# [    ]
#
slice_1to3 = slice(1, 4)
slice_rect = (slice(1, 4), slice(1, 3))
data[(slice(1, 4), slice(1, 3))] = [255, 0, 0]      # set matrix/image rows 2 and 3 to red
data[1:4, 1:3] = [255, 0, 0]                          # set matrix/image rows 2 and 3 to red


img = Image.fromarray(data, 'RGB')                  # create RGB image using data
img.save('canvas.png')                              # save image to file


