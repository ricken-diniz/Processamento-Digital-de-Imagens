from affine_transformations import scalar_transformation
import numpy as np
import cv2 as cv
import os

black_img = np.full((1,2), 0, dtype=np.uint8)
black_img[0][1] = 144
cv.imshow("black", black_img)

resized_image = scalar_transformation(black_img, 4, 2)
cv.imshow('resized', resized_image)

cv.waitKey(0)
cv.destroyAllWindows()
