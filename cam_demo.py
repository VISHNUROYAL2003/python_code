import cv2

# Open the webcam (0 is usually the default camera)
cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Capture a frame
ret, frame = cap.read()

if ret:
    # Save the captured image
    cv2.imwrite('captured_image.png', frame)
    print("Image captured and saved as 'captured_image.png'.")
else:
    print("Error: Could not read frame.")

# Release the webcam
cap.release()
