import numpy as np

shape = (5, 5)
canvas = np.zeros(shape, dtype=int)
print(canvas)
print(canvas.shape)
print(canvas.ndim)
print(canvas.size)
print(canvas.dtype)

# writing someone on canvas
canvas[2, 3] = 255
print(canvas)

# Drawing a horizontal line
canvas[2, :] = 255
print(canvas)
