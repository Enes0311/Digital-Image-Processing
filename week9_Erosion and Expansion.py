import cv2
import numpy as np
import matplotlib.pyplot as plt

image_path = 'new-year.png'
image = cv2.imread(image_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# morphological operations
kernel = np.ones((5, 5), np.uint8)


erosion_image = cv2.erode(image, kernel, iterations=1)

dilation_image = cv2.dilate(image, kernel, iterations=1)

opening_image = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

closing_image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)




fig, axes = plt.subplots(2, 4, figsize=(20, 10))

axes[0, 0].imshow(image)
axes[0, 0].set_title('Original Image')
axes[0, 0].axis('off')

axes[0, 1].imshow(erosion_image)
axes[0, 1].set_title('Erosion')
axes[0, 1].axis('off')

axes[0, 2].imshow(dilation_image)
axes[0, 2].set_title('Dilation')
axes[0, 2].axis('off')

axes[0, 3].imshow(cv2.subtract(image, opening_image))
axes[0, 3].set_title('Difference (Original - Opening)')
axes[0, 3].axis('off')

axes[1, 0].imshow(opening_image)
axes[1, 0].set_title('Opening')
axes[1, 0].axis('off')

axes[1, 1].imshow(closing_image)
axes[1, 1].set_title('Closing')
axes[1, 1].axis('off')

axes[1, 2].imshow(cv2.subtract(closing_image, image))
axes[1, 2].set_title('Difference (Closing - Original)')
axes[1, 2].axis('off')

axes[1, 3].axis('off')

plt.show()
