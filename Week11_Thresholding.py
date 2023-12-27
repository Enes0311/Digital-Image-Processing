import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load an image
image_path = 'day.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Apply simple binary thresholding
_, binary_threshold = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# Apply adaptive thresholding
adaptive_threshold = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

# Apply Canny Edge Detection
edges = cv2.Canny(image, 50, 150)

# Plot the images
fig, axes = plt.subplots(1, 4, figsize=(20, 5))

axes[0].imshow(image, cmap='gray')
axes[0].set_title('Original Image')
axes[0].axis('off')

axes[1].imshow(binary_threshold, cmap='gray')
axes[1].set_title('Binary Thresholding')
axes[1].axis('off')

axes[2].imshow(adaptive_threshold, cmap='gray')
axes[2].set_title('Adaptive Thresholding')
axes[2].axis('off')

axes[3].imshow(edges, cmap='gray')
axes[3].set_title('Canny Edge Detection')
axes[3].axis('off')

plt.show()
