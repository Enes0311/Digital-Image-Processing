import numpy as np
import cv2

def saltPepperNoise(image):
    row, col, ch = image.shape
    s_vs_p = 0.5
    amount = 0.04
    noisy = np.copy(image)

    # Add salt noise
    num_salt = int(np.ceil(amount * image.size * s_vs_p))
    salt_coords = [np.random.choice(range(dim), num_salt) for dim in image.shape]
    noisy[salt_coords[0], salt_coords[1], salt_coords[2]] = 1

    # Add pepper noise
    num_pepper = int(np.ceil(amount * image.size * (1.0 - s_vs_p)))
    pepper_coords = [np.random.choice(range(dim), num_pepper) for dim in image.shape]
    noisy[pepper_coords[0], pepper_coords[1], pepper_coords[2]] = 0

    return noisy

def exponentialNoise(image, scale=0.1):
    noise = np.random.exponential(scale, image.shape)
    noisy = image + noise
    return np.clip(noisy, 0, 1)

def uniformNoise(image, low=-0.1, high=0.1):
    noise = np.random.uniform(low, high, image.shape)
    noisy = image + noise
    return np.clip(noisy, 0, 1)

img = cv2.imread("salt.jpg")


if img is not None:
    img = img / 255.0

    # Salt and Pepper Noise
    salt_pepper_img = saltPepperNoise(img)

    # Exponential Noise
    exp_noise_img = exponentialNoise(img)

    # Uniform Noise
    uniform_noise_img = uniformNoise(img)


    cv2.imshow("Original Image", img)
    cv2.imshow("Salt and Pepper Noise", salt_pepper_img)
    cv2.imshow("Exponential Noise", exp_noise_img)
    cv2.imshow("Uniform Noise", uniform_noise_img)

    cv2.waitKey(0)
else:
    print("Error loading the image.")
