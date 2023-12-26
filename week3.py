import numpy as np
import matplotlib.pyplot as plt


import cv2


input_image_path = 'brain.jpg'

# Read the input image
input_img = cv2.imread(input_image_path)

# Check if the input image was successfully loaded
if input_img is not None:

    cv2.imshow('Input Image', input_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Specify the path to save the output image
    output_image_path = 'brain.jpg'


    success = cv2.imwrite(output_image_path, input_img)

    if success:
        print(f"Image successfully saved at {output_image_path}")
    else:
        print("Error: Unable to save the image.")
else:
    print(f"Error: Unable to read the input image from {input_image_path}")

