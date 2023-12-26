import cv2
import matplotlib.pyplot as plt

# Read the input image
input_image_path = 'brain.jpg'
input_img = cv2.imread(input_image_path, cv2.IMREAD_GRAYSCALE)


if input_img is not None:

    plt.figure(figsize=(8, 4))
    plt.subplot(1, 2, 1)
    plt.imshow(input_img, cmap='gray')
    plt.title('Original Image')

    # Perform histogram equalization
    equalized_img = cv2.equalizeHist(input_img)


    plt.subplot(1, 2, 2)
    plt.imshow(equalized_img, cmap='gray')
    plt.title('Equalized Image')

    plt.show()


    output_equalized_image_path = 'brain.jpg'

    # equalized image
    success = cv2.imwrite(output_equalized_image_path, equalized_img)
