import cv2
import matplotlib.pyplot as plt

# Open a connection to the camera (0 is the default camera, change it if needed)
cap = cv2.VideoCapture(0)

# Check if the camera is opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
else:
    # Read a frame from the camera
    ret, frame = cap.read()

    if ret:
        # Display the captured frame
        plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        plt.title('Captured Image')
        plt.show()
    else:
        print("Error: Could not read a frame from the camera.")

# Release the camera
cap.release()
