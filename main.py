import make_noise
import padding
from PIL import Image
import numpy as np

FILTER_LENGTH = 3
PADDING_SIZE = int((FILTER_LENGTH - 1) / 2)

def median_filter(padding_image):
    w, h = padding_image.shape[1], padding_image.shape[0]
    output_image = padding_image.copy()
    
    for y in range(PADDING_SIZE, h - PADDING_SIZE):
        for x in range(PADDING_SIZE, w - PADDING_SIZE):
            output_image[y][x] = np.median(output_image[y - PADDING_SIZE: y + PADDING_SIZE + 1, x - PADDING_SIZE: x + PADDING_SIZE + 1])
    
    return output_image

def main():
    original_image = Image.open("Images/input.jpg")
    original_image = original_image.convert("L")
    original_image.save("Images/grey.jpg")
    w, h = original_image.size
    noise_image = make_noise.make_noise_image(original_image, w, h)
    noise_image.save("Images/noise.jpg")
    padding_image = padding.mirror_padding(noise_image, PADDING_SIZE)
    
    filtered_image = median_filter(padding_image)
    
    filtered_image = Image.fromarray(filtered_image, "L")
    
    filtered_image.show()
    filtered_image.save("Images/output.jpg")

if __name__ == "__main__":
    main()
     