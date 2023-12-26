import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the input image
input_image_path = 'road.jpg'
input_img = cv2.imread(input_image_path, cv2.IMREAD_GRAYSCALE)


if input_img is not None:
    # Display the original image
    plt.figure(figsize=(15, 5))
    plt.subplot(1, 4, 1)
    plt.imshow(input_img, cmap='gray')
    plt.title('Original Image')

    #  blur for smoothing
    blurred_img = cv2.GaussianBlur(input_img, (5, 5), 0)


    plt.subplot(1, 4, 2)
    plt.imshow(blurred_img, cmap='gray')
    plt.title('Blurred Image')


    equalized_img = cv2.equalizeHist(blurred_img)

    plt.subplot(1, 4, 3)
    plt.imshow(equalized_img, cmap='gray')
    plt.title('Equalized Image')

    laplacian = cv2.Laplacian(equalized_img, cv2.CV_64F)
    sharpened_img = equalized_img - laplacian


    sharpened_img = np.uint8(np.clip(sharpened_img, 0, 255))

    plt.subplot(1, 4, 4)
    plt.imshow(sharpened_img, cmap='gray')
    plt.title('Sharpened Image')

    plt.show()

    output_filtered_image_path = 'road.jpg'

    #  filtered image
    success = cv2.imwrite(output_filtered_image_path, sharpened_img)
