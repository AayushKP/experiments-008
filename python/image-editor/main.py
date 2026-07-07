from editor import *

image = create_canvas(10, 10)


draw_horizontal_line(image, 5, 255)


draw_vertical_line(image, 5, 255)


fill_rectangle(image, 1, 4, 1, 4, 100)


print(image)
