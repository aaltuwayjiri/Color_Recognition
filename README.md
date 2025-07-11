# Color_Recognition

This project captures live video from your video and detects the **basic color** at the center of the screen in real-time. It draws a green square at the center, analyzes the average color inside, and shows the recognized color name and RGB values.

---

## Features

- Real-time video processing using OpenCV
- Detects basic colors: **Red, Orange, Yellow, Green, Cyan, Blue, Purple, Brown, Gray, Black, White**
- Uses HSV color space for robust color classification
- Displays a live preview with:
  - Green 30×30 square in the center
  - Recognized color name and RGB values
  - Colored label background based on detected color

---

## Requirements

- Python 3.x
- OpenCV (`opencv-python`)
- NumPy

Install them via pip:

bash
pip install opencv-python numpy

--- 

## how to run 

Save the script as color_recognition.py.

Run the script:
python color_recognition.py

(Press q to quit the window.)

---

## How It Works

Captures frames from your video using OpenCV.

Samples a 30×30 pixel region in the center of the frame.

Computes the average BGR color in that region.

Converts it to HSV color space for better classification.

Uses hue, saturation, and brightness to determine the nearest basic color name.

---

## Color Classification Logic

The system uses HSV ranges to detect:

Brown = Orange hue with low brightness

Gray = Low saturation, mid brightness

White/Black = Very high or low brightness

And other basic hues (Red, Green, Blue, etc.)

---

Made with ❤️ using Python & OpenCV
Feel free to customize or extend it!

