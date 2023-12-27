import numpy as np

def rgb_to_hsi(rgb):
    r, g, b = rgb / 255.0

    # Cal intensity (I)
    intensity = (r + g + b) / 3.0

    # Avoid division by zero errors
    if intensity == 0:
        return 0, 0, 0

    # Calculate saturation (S)
    min_rgb = np.min([r, g, b])
    saturation = 1 - min_rgb / intensity
    # Calculate hue (H)
    numerator = 0.5 * ((r - g) + (r - b))
    denominator = np.sqrt((r - g)**2 + (r - b) * (g - b))
    angle_rad = np.arccos(np.clip(numerator / denominator, -1.0, 1.0))

    hue = np.degrees(angle_rad)

    if b > g:
        hue = 360 - hue

    return hue, saturation, intensity


rgb_color = np.array([255, 0, 0])  # Red in RGB
hsi_color = rgb_to_hsi(rgb_color)
print("RGB:", rgb_color)
print("HSI:", hsi_color)
