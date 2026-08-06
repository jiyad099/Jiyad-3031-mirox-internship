import numpy as np
from PIL import Image

def apply_Gaussian(image, intensity):

    img_array = np.array(image).astype(np.float32)

    mean = 0
    sigma = intensity * 0.5

    gauss = np.random.normal(mean, sigma, img_array.shape)

    noisy = img_array + gauss
    noisy = np.clip(noisy, 0, 255).astype(np.uint8)
    return Image.fromarray(noisy)

def apply_pixel_shift(image, intensity):

    img_array = np.array(image)

    # Shift pixels horizontally
    shifted = np.roll(img_array, shift=intensity, axis=1)

    return Image.fromarray(shifted.astype(np.uint8))

