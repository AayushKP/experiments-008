import numpy as np


def create_canvas(height, width, color=0):
    return np.full((height, width), color, dtype=np.uint8)


def draw_horizontal_line(image, row, value):
    image[row, :] = value


def draw_vertical_line(image, column, value):
    image[:, column] = value


def fill_rectangle(image, sr, er, sc, ec, value):
    image[sr:er, sc:ec] = value


def crop(image, sr, er, sc, ec):
    return image[sr:er, sc:ec].copy()


def invert(image):
    return 255 - image


def brightness(image, amount):
    result = image.astype(int)
    result = result + amount
    return np.clip(result, 0, 255).astype(np.uint8)


def flip_horizontal(image):
    return image[:, ::-1]


def flip_vertical(image):
    return image[::-1, :]


def rotate(image):
    return np.rot90(image)
