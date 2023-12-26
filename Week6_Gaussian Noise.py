import cv2
import numpy as np
import matplotlib.pyplot as plt


input_image_path = 'road.jpg'
noisy_img = cv2.imread(input_image_path, cv2.IMREAD_GRAYSCALE)


if noisy_img is not None:

    plt.figure(figsize=(30, 10))
    plt.subplot(1, 3, 1)
    plt.imshow(noisy_img, cmap='gray')
    plt.title('Noisy Image')

    # Denoise the image using Non-Local Means Denoising
    denoised_img = cv2.fastNlMeansDenoising(noisy_img, None, h=15, templateWindowSize=7, searchWindowSize=21)


    plt.subplot(1, 3, 2)
    plt.imshow(denoised_img, cmap='gray')
    plt.title('Denoised Image')

    # Apply the Laplacian operator for sharpening
    laplacian = cv2.Laplacian(denoised_img, cv2.CV_64F)
    sharpened_img = denoised_img - laplacian


    sharpened_img = np.uint8(np.clip(sharpened_img, 0, 255))

    # Display the sharpened image (optional)
    plt.subplot(1, 3, 3)
    plt.imshow(sharpened_img, cmap='gray')
    plt.title('Sharpened Image')

    plt.show()

    # Specify the path to save the output enhanced image
    output_enhanced_image_path = 'road.jpg'

    # Write the enhanced image
    success = cv2.imwrite(output_enhanced_image_path, sharpened_img)
