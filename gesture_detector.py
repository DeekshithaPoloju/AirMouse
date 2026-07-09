class GestureDetector:

    CLICK_DISTANCE = 35

    @staticmethod
    def is_move(fingers):
        return (
            fingers[1] == 1 and
            fingers[2] == 0 and
            fingers[3] == 0 and
            fingers[4] == 0
        )

    @staticmethod
    def is_left_click(fingers, distance):
        return (
            fingers[1] == 1 and
            fingers[2] == 0 and
            distance < GestureDetector.CLICK_DISTANCE
        )

    @staticmethod
    def is_right_click(fingers, distance):
        return (
            fingers[2] == 1 and
            distance < GestureDetector.CLICK_DISTANCE
        )

    @staticmethod
    def is_double_click(fingers, distance):
        return (
            fingers[3] == 1 and
            distance < GestureDetector.CLICK_DISTANCE
        )

    @staticmethod
    @staticmethod
    def is_scroll(fingers):
        return (
        fingers[0] == 1 and
        fingers[1] == 0 and
        fingers[2] == 0 and
        fingers[3] == 0 and
        fingers[4] == 1
    )
    @staticmethod
    def is_drag(fingers):
        return (
            fingers[1] == 0 and
            fingers[2] == 0 and
            fingers[3] == 0 and
            fingers[4] == 0
        )
      #