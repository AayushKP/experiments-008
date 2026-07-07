import numpy as np

shape = (5, 5)
canvas = np.zeros(shape, dtype=int)
print(canvas)
print(canvas.shape)
print(canvas.ndim)
print(canvas.size)
print(canvas.dtype)

canvas[2, 3] = 255
print(canvas)
