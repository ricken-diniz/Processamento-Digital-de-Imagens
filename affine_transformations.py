import numpy as np
import cv2 as cv
from image_interpolation import interpolate_by_nearest_neighbor

def scalar_transformation(img, hNew, wNew):

    height = len(img)
    width = len(img[0])

    h_scale = hNew / height
    w_scale = wNew / width

    img_size = (height,width)
    transformed_pixels = []

    for lin in range(height):
        for col in range(width):
            transformed_pixel = (int(lin*h_scale), int(col*w_scale), img[lin][col])
            transformed_pixels.append(transformed_pixel)


    return interpolate_by_nearest_neighbor(transformed_pixels, img_size, h_scale, w_scale)

def translation(img, rotation):
    sin = np.sin(np.deg2rad(rotation))
    cos = np.cos(np.deg2rad(rotation))

    rNew = len(img)
    cNew = len(img[0])

    new_img_matrix = np.full((rNew,cNew), 0, dtype=np.uint8)

    for x in range(rNew):
        for y in range(cNew):
            newX = int(np.round(x*cos - y*sin))
            newY = int(np.round(x*sin + y*cos))
            new_img_matrix[x, y] = img[newX][newY]

    return new_img_matrix