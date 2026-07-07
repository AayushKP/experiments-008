import numpy as np

shape = (5, 5)
canvas = np.zeros(shape, dtype=int)
print(canvas)
print()
print("-" * 50)
print()
print(canvas.shape)
print(canvas.ndim)
print(canvas.size)
print(canvas.dtype)
print()
print("-" * 50)
print()

# writing someone on canvas
# canvas[2, 3] = 255
# print(canvas)

# Drawing a horizontal line
# canvas[2, :] = 255
# print(canvas)

# Drawing a vertical line
# canvas[:, 3] = 255
# print(canvas)

# Drwaing a rectangle
canvas[1:4, 1:4] = 255
print(canvas)
print()
print("-" * 50)
print()

# Scalar Broadcasting
arr = np.array([10, 20, 30])
print(arr + 5)

print()
print("-" * 50)
print()

# Row Broadcasting
matrix = np.array([[1, 2, 3], [4, 5, 6]])

row = np.array([10, 20, 30])
print(matrix + row)
print()
print("-" * 50)
print()

# Column Broadcasting
column = np.array([[100], [200]])
print(matrix + column)
print()
print("-" * 50)
print()


# Reshape
brr = np.arange(12)
print(brr)
mat = brr.reshape((3, 4))
print(mat)
