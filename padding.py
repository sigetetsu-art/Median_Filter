from PIL import Image
import numpy as np

def mirror_padding(original_image, padding_size):
    img_pixels = np.array(original_image)
    padding_image = np.pad(img_pixels, ((padding_size, padding_size), (padding_size, padding_size)), "edge")
    return padding_image