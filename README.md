# 🖱️ Air Mouse using Hand Gestures

## 📌 Overview

Air Mouse is a computer vision project that allows users to control the mouse cursor using hand gestures through a webcam.

The project uses OpenCV, MediaPipe (via CVZone), and PyAutoGUI to recognize hand gestures and perform mouse operations without touching a physical mouse.

---

## 🚀 Features

- Cursor Movement
- Left Click
- Right Click
- Double Click
- Scroll
- Drag and Drop
- FPS Counter
- Real-Time Gesture Recognition

---

## 🛠 Technologies Used

- Python
- OpenCV
- MediaPipe
- CVZone
- PyAutoGUI
- NumPy

---

## 📂 Project Structure

```
AirMouse/
│
├── config.py
├── gesture_detector.py
├── hand_detector.py
├── mouse_controller.py
├── main.py
├── requirements.txt
└── README.md
```

---

## ▶️ Installation

```bash
pip install -r requirements.txt
```

---

## ▶️ Run

```bash
python main.py
```

---

## ✋ Gesture Controls

| Gesture | Action |
|----------|--------|
| ☝️ Index Finger | Move Cursor |
| 👍 + ☝️ | Left Click |
| 👍 + 🖕 | Right Click |
| 🤏 Index + Middle | Double Click |
| 🤙 Thumb + Little | Scroll |
| ✊ Closed Fist | Drag and Drop |

---

## 📈 Future Improvements

- Volume Control
- Brightness Control
- Virtual Keyboard
- Multi-Hand Support
- AI Gesture Recognition

---

## 👨‍💻 Author

Developed using Python, OpenCV, MediaPipe, and CVZone.
