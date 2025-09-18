import numpy as np
import cv2 as cv
from image_interpolation import interpolate_by_nearest_neighbor

def scalar_transformation(img, h_scale, w_scale):

    height = len(img)
    width = len(img[0])
    img_size = (height,width)
    transformed_pixels = []

    for lin in range(height):
        for col in range(width):
            transformed_pixel = (lin*h_scale, col*w_scale, img[lin][col])
            transformed_pixels.append(transformed_pixel)


    return interpolate_by_nearest_neighbor(transformed_pixels, img_size, h_scale, w_scale)