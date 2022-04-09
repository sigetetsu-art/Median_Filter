from PIL import Image, ImageChops

def make_noise_image(original_image, w, h):
    noise_image = Image.effect_noise((w, h), 30).convert("L")
    result_image = ImageChops.multiply(original_image, noise_image)
    
    return result_image

