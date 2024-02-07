import cv2
import numpy as np

video_path = "Task 2/task_2_video.mp4"
output_video_path = "Task 2/output_task_2.mp4"
cap = cv2.VideoCapture(video_path)
width = int(cap.get(3))
height = int(cap.get(4))
fps = int(cap.get(5))

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))
lower_green = np.array([30, 100, 100])
upper_green = np.array([70, 255, 212])
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv_frame, lower_green, upper_green)
    kernel = np.ones((3, 3), np.uint8)
    mask = cv2.dilate(mask, kernel, iterations=5)
    mask = cv2.erode(mask, kernel, iterations=2)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        M = cv2.moments(contour)
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])

            cv2.circle(frame, (cX, cY), 5, (0, 0, 255), -1)
    out.write(frame)
cap.release()
out.release()
