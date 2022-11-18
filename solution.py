import numpy as np

"""
write a program that calculates pixel coordinate values for an image 
that is to be displayed on a two dimensional surface given the dimensions 
of the image and the corner points of the image as it is to be displayed.

For example, if an image is defined by a 3x3 grid of pixel values, 
and the (x, y) coordinates of the four corner points to display the 
image at are: (1, 1), (3, 1), (1, 3), and (3, 3) 

then the program should calculate and return the coordinates: 
(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (3, 1), (3, 2), (3, 3) 
which are the coordinates at which to place the 9 pixels in the image such that 
they're evenly spaced within the corner points. 
"""
def get_pixel_coordinates(image_dimensions, corner_points):
    height, width = image_dimensions
    corner_points = np.asarray(corner_points, dtype=float)

    x_min, x_max = corner_points[:, 0].min(), corner_points[:, 0].max()
    y_min, y_max = corner_points[:, 1].min(), corner_points[:, 1].max()

    x = np.linspace(start=x_min, stop=x_max, num=width)
    y = np.linspace(start=y_min, stop=y_max, num=height)

    x, y = np.meshgrid(x, y)
    return np.stack((x, y), axis=-1).reshape(-1, 2)

if __name__ == '__main__':
    image_dimensions = (3, 3)
    corner_points = [(1, 1), (3, 1), (1, 3), (3, 3)]
    print(get_pixel_coordinates(image_dimensions, corner_points))


