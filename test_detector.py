import cv2
from hand_detector import AirHandDetector

cap = cv2.VideoCapture(0)

detector = AirHandDetector()

while True:

    success, frame = cap.read()

    if not success:
        break

    frame, hand, lmList = detector.detect_hand(frame)

    if hand:

        print("Index Tip :", lmList[8])
        print("Thumb Tip :", lmList[4])

    cv2.imshow("Air Mouse", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
cv2.destroyAllWindows()