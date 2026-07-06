import cv2

from hand_tracker import HandTracker
from config import CAMERA_INDEX, CAMERA_WIDTH, CAMERA_HEIGHT

# Open the webcam
cap = cv2.VideoCapture(CAMERA_INDEX)

# Set camera resolution
cap.set(cv2.CAP_PROP_FRAME_WIDTH, CAMERA_WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, CAMERA_HEIGHT)

# Create HandTracker object
tracker = HandTracker()

while True:
    success, img = cap.read()

    if not success:
        print("Failed to read from camera.")
        break

    # Detect hands
    img = tracker.findHands(img)

    # Get landmark positions
    lmList = tracker.findPosition(img)

    # Print index fingertip coordinates
    if lmList:
        print("Index Finger:", lmList[8])

    # Show the webcam
    cv2.imshow("Hand Tracker Test", img)

    # Press Q to quitt
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
