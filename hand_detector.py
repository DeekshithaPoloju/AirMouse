from cvzone.HandTrackingModule import HandDetector
import math


class AirHandDetector:

    def __init__(self):
        self.detector = HandDetector(
            staticMode=False,
            maxHands=1,
            detectionCon=0.8,
            minTrackCon=0.5
        )

    def detect_hand(self, frame):

        hands, frame = self.detector.findHands(frame)

        if hands:
            hand = hands[0]
            lmList = hand["lmList"]
            return frame, hand, lmList

        return frame, None, None

    def fingers_up(self, hand):
        return self.detector.fingersUp(hand)

    def distance(self, p1, p2):
        x1, y1 = p1[0], p1[1]
        x2, y2 = p2[0], p2[1]

        return math.hypot(x2 - x1, y2 - y1)
     boloooo