import numpy as np

def interpolate_by_nearest_neighbor(transformed_pixels, img_size, h_scale, w_scale):

    height, width = img_size
    new_img_matrix = np.full((int(height * h_scale), int(width * w_scale)), 0, dtype=np.uint8)

    for pixel in transformed_pixels:
        v, w, value = pixel
        
        for lin in range(v, v + h_scale):
            for col in range(w, w + w_scale):
                new_img_matrix[lin][col] = value

    return new_img_matrix



    # for h in range(len(resized_image_matrix)):
    #     for w in range(len(resized_image_matrix[h])):
    #         resized_image_matrix[h][w] = img[h//h_scale][w//w_scale]

    # return resized_image_matrix


    