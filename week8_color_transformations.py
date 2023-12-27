import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import convolve
import colorsys


image_path = 'dog-.jpg'
image = cv2.imread(image_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

#  convert RGB to CMYK
def rgb_to_cmyk(rgb):
    # Normalize RGB values to the range [0, 1]
    r, g, b = [x / 255.0 for x in rgb]
    # RGB to CMY
    c, m, y = [1 - x for x in (r, g, b)]
    # CMY to CMYK
    k = min(c, m, y)
    if k == 1.0:
        c = m = y = 0.0
    else:
        c, m, y = [(x - k) / (1 - k) for x in (c, m, y)]
    return c, m, y, k

#sharpen
def sharpen_image(image, alpha=1.5):
    #  Laplacian filter
    laplacian_filter = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])
    sharpened_image = np.zeros_like(image)
    for i in range(3):
        sharpened_image[:, :, i] = convolve(image[:, :, i], laplacian_filter)

    sharpened_image = image + alpha * sharpened_image

    # Clip the values to be in the valid range [0, 255]
    sharpened_image = np.clip(sharpened_image, 0, 255)

    return sharpened_image.astype(np.uint8)

# its color space components and ima
def plot_image_and_components(color_space, color_slice_range, detect_white=False, sharpen_alpha=1.5):
    fig, axes = plt.subplots(1, 8, figsize=(40, 5))
    axes[0].imshow(image)
    axes[0].set_title('Original Image')
    axes[0].axis('off')
    color_space_codes = {
        'RGB': cv2.COLOR_BGR2RGB,
        'HSV': cv2.COLOR_BGR2HSV,
        'LAB': cv2.COLOR_BGR2LAB,
        'YCrCb': cv2.COLOR_BGR2YCrCb
    }

    # specified color space
    converted_image = cv2.cvtColor(image, color_space_codes[color_space])
    for i in range(3):
        axes[i + 1].imshow(converted_image[:, :, i], cmap='gray')
        axes[i + 1].set_title(f'{color_space} - Channel {i + 1}')
        axes[i + 1].axis('off')

    #  image to HSI
    hsi_image = cv2.cvtColor(image, cv2.COLOR_RGB2HSV) / np.array([360, 1, 255.], dtype=np.float32)
    axes[4].imshow(hsi_image[:, :, 0], cmap='hsv', vmin=0, vmax=1)
    axes[4].set_title('HSI - Hue')
    axes[4].axis('off')

    color_slice_mask = np.all((converted_image >= color_slice_range[0]) & (converted_image <= color_slice_range[1]), axis=-1)
    if detect_white:
        white_mask = np.all(converted_image >= [200, 200, 200], axis=-1)
        color_slice_mask = np.logical_or(color_slice_mask, white_mask)
    color_sliced_image = np.zeros_like(image)
    color_sliced_image[color_slice_mask] = image[color_slice_mask]
    axes[5].imshow(color_sliced_image)
    axes[5].set_title('Color Slicing')
    axes[5].axis('off')
    # Sharpen
    sharpened_image = sharpen_image(image, alpha=sharpen_alpha)
    axes[6].imshow(sharpened_image)
    axes[6].set_title('Sharpened Image')
    axes[6].axis('off')
    #  image to CMYK
    cmyk_image = np.apply_along_axis(rgb_to_cmyk, -1, converted_image)
    axes[7].imshow(cmyk_image)
    axes[7].set_title('CMYK')
    axes[7].axis('off')
    plt.show()

#  color space ('RGB', 'HSV')
selected_color_space = 'HSV'
selected_color_space = 'RGB'


selected_color_slice_range = [(0, 0, 100), (50, 255, 255)]

detect_white_color = True

sharpen_alpha = 1.5

plot_image_and_components(selected_color_space, selected_color_slice_range, detect_white_color, sharpen_alpha)
