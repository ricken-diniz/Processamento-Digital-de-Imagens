from affine_transformations import scalar_transformation, translation
import numpy as np
import cv2 as cv
import os

# black_img = np.full((2,2), 0, dtype=np.uint8)
# black_img[0][1] = 144
# cv.imshow("black", black_img)

# resized_image = scalar_transformation(black_img, 4, 2)
# cv.imshow('resized', resized_image)

imagem = cv.imread("./static/relogio.jpg")
imagem = cv.cvtColor(imagem, cv.COLOR_BGR2GRAY)

resized_img = scalar_transformation(imagem, 500,500)
# translated_img = translation(resized_img, 90)
cv.imshow('resized', resized_img)

cv.waitKey(0)
cv.destroyAllWindows()
