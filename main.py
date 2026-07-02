import cv2
import time

from hand_detector import AirHandDetector
from mouse_controller import MouseController
from gesture_detector import GestureDetector
from config import *

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, CAMERA_WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, CAMERA_HEIGHT)

detector = AirHandDetector()
mouse = MouseController()

left_click_active = False
right_click_active = False
double_click_active = False

scroll_y = None
drag_mode = False

current_gesture = "NONE"

prev_time = 0
curr_time = 0

while True:

    success, frame = cap.read()

    if not success:
        break

    current_gesture = "NONE"

    curr_time = time.time()

    if prev_time == 0:
        fps = 0
    else:
        fps = 1 / (curr_time - prev_time)

    prev_time = curr_time

    frame = cv2.flip(frame, 1)

    frame, hand, lmList = detector.detect_hand(frame)

    cv2.rectangle(
        frame,
        (FRAME_MARGIN, FRAME_MARGIN),
        (CAMERA_WIDTH - FRAME_MARGIN,
         CAMERA_HEIGHT - FRAME_MARGIN),
        (255, 0, 255),
        2
    )

    if hand:

        fingers = detector.fingers_up(hand)

        thumb = lmList[4]
        index = lmList[8]
        middle = lmList[12]
        little = lmList[20]

        x, y, _ = index

        left_distance = detector.distance(thumb, index)
        right_distance = detector.distance(thumb, middle)
        index_middle_distance = detector.distance(index, middle)

        # =====================================
        # MOVE
        # =====================================

        if GestureDetector.is_move(fingers):

            mouse.move_mouse(x, y)
            current_gesture = "MOVE"

        # =====================================
        # LEFT CLICK
        # =====================================

        if GestureDetector.is_left_click(fingers, left_distance):

            if not left_click_active and mouse.can_click():

                mouse.left_click()
                mouse.update_click_time()

                current_gesture = "LEFT CLICK"

                left_click_active = True

        else:

            left_click_active = False

        # =====================================
        # RIGHT CLICK
        # =====================================

        if GestureDetector.is_right_click(fingers, right_distance):

            if not right_click_active and mouse.can_click():

                mouse.right_click()
                mouse.update_click_time()

                current_gesture = "RIGHT CLICK"

                right_click_active = True

        else:

            right_click_active = False

        # =====================================
        # DOUBLE CLICK
        # =====================================

        if (
            fingers[1] == 1 and
            fingers[2] == 1 and
            index_middle_distance < 30
        ):

            if not double_click_active and mouse.can_click():

                mouse.double_click()
                mouse.update_click_time()

                current_gesture = "DOUBLE CLICK"

                double_click_active = True

        else:

            double_click_active = False
                    # =====================================
        # SCROLL
        # Thumb + Little Finger
        # =====================================

        if GestureDetector.is_scroll(fingers):

            current_gesture = "SCROLL"

            current_y = little[1]

            if scroll_y is None:
                scroll_y = current_y

            difference = scroll_y - current_y

            if difference > 10:

                mouse.scroll(300)
                scroll_y = current_y

            elif difference < -10:

                mouse.scroll(-300)
                scroll_y = current_y

        else:

            scroll_y = None

        # =====================================
        # DRAG & DROP
        # Closed Fist
        # =====================================

        if GestureDetector.is_drag(fingers):

            current_gesture = "DRAG"

            if not drag_mode:

                mouse.start_drag()
                drag_mode = True

            mouse.move_mouse(x, y)

        else:

            if drag_mode:

                mouse.stop_drag()
                drag_mode = False

    # =====================================
    # DISPLAY CURRENT GESTURE
    # =====================================

    cv2.putText(
        frame,
        f"Gesture : {current_gesture}",
        (20, 35),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 255),
        2
    )

    # =====================================
    # DISPLAY FPS
    # =====================================

    cv2.putText(
        frame,
        f"FPS : {int(fps)}",
        (500, 35),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2
    )

    cv2.imshow("Air Mouse", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()