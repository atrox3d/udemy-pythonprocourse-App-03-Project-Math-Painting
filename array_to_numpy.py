import numpy as np
from PIL import Image

data = np.zeros((
    5,                      # horizontal
    4,                      # vertical
    3                       # depth
),
    dtype=np.uint8
)

data[:] = [255, 255, 0]

print(data)
