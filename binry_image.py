import cv2

# Specify the path to the input image file
input_image_path = 'brain.jpg'


input_img = cv2.imread(input_image_path, cv2.IMREAD_GRAYSCALE)


if input_img is not None:

    cv2.imshow('Original Grayscale Image', input_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Perform thresholding to create a binary image
    _, binary_img = cv2.threshold(input_img, 127, 255, cv2.THRESH_BINARY)

    cv2.imshow('Binary Image', binary_img)
    cv2.waitKey(0)  # Wait for a key press
    cv2.destroyAllWindows()

    # Resize
    new_width, new_height = 15, 10
    resized_binary_img = cv2.resize(binary_img, (new_width, new_height))


    cv2.imshow('Resized Binary Image', resized_binary_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Specify the path to save the output resized binary image
    output_resized_binary_image_path = 'brain.jpg'

    # Write the resized binary image
    success = cv2.imwrite(output_resized_binary_image_path, resized_binary_img)

    if success:
        print(f"Resized binary image successfully saved at {output_resized_binary_image_path}")
    else:
        print("Error: Unable to save the resized binary image.")
else:
    print(f"Error: Unable to read the input image from {input_image_path}")
