import cv2
import numpy as np

def get_basic_color_name(b, g, r):
    color_bgr = np.uint8([[[b, g, r]]])
    hsv = cv2.cvtColor(color_bgr, cv2.COLOR_BGR2HSV)[0][0]
    h, s, v = hsv[0], hsv[1], hsv[2]

    if v < 50:
        return "Black"
    if s < 50:
        if v > 200:
            return "White"
        else:
            return "Gray"
    
    # Detect brown: hue ~10-20, saturation high, value low/medium
    if 10 <= h <= 20 and s >= 100 and v <= 150:
        return "Brown"

    if h < 5 or h > 170:
        return "Red"
    elif h < 22:
        return "Orange"
    elif h < 35:
        return "Yellow"
    elif h < 85:
        return "Green"
    elif h < 125:
        return "Blue"
    elif h < 160:
        return "Blue"
    else:
        return "Purple"

#put your video path here:
video_path = r'C:\Users\abdul\Desktop\task2\video1.mp4'
cap = cv2.VideoCapture(video_path)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    h, w, _ = frame.shape
    cx, cy = w // 2, h // 2

    size = 50  # half size of square (30x30 region)
    roi = frame[cy - size:cy + size, cx - size:cx + size]
    b, g, r = cv2.mean(roi)[:3]
    b, g, r = int(b), int(g), int(r)

    color_name = get_basic_color_name(b, g, r)

    # Draw green square around sampling area
    cv2.rectangle(frame, (cx - size, cy - size), (cx + size, cy + size), (0, 255, 0), 2)

    # Show color name and RGB values
    text = f'{color_name} (R={r} G={g} B={b})'
    cv2.rectangle(frame, (20, 20), (600, 60), (b, g, r), -1)
    text_color = (255, 255, 255) if (r*0.299 + g*0.587 + b*0.114) < 186 else (0, 0, 0)
    cv2.putText(frame, text, (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, text_color, 2)

    cv2.imshow("Color Recognition", frame)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

