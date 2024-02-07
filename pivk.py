
import cv2
import numpy as np

def on_mouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        hsv_color = cv2.cvtColor(np.uint8([[image[y, x]]]), cv2.COLOR_BGR2HSV)
        print("HSV Values (H, S, V):", hsv_color[0, 0])

# Create a blank image (you can load an existing image as well)
image = cv2.imread(r"Task 2\images\1.png")

cv2.namedWindow("Color Picker")
cv2.setMouseCallback("Color Picker", on_mouse)

while True:
    cv2.imshow("Color Picker", image)
    
    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # Press 'Esc' to exit
        break

cv2.destroyAllWindows()
