import cv2
import numpy as np
import matplotlib.pyplot as plt


input_image_path = 'ba.jpg'
input_img = cv2.imread(input_image_path)


if input_img is not None:

    plt.figure(figsize=(8, 4))
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(input_img, cv2.COLOR_BGR2RGB))
    plt.title('Original Image')

    # Define a 2D convolution kernel for blurring
    kernel_size = 5
    kernel = np.ones((kernel_size, kernel_size), np.float32) / (kernel_size * kernel_size)

    # Apply the 2D convolution to blur the image
    blurred_img = cv2.filter2D(input_img, -1, kernel)


    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(blurred_img, cv2.COLOR_BGR2RGB))
    plt.title('Blurred Image')

    plt.show()


    output_blurred_image_path = 'ba.jpg'

    # Write the blurred image
    success = cv2.imwrite(output_blurred_image_path, blurred_img)
