import rembg
import cv2
import numpy as np
import os

def resize_img(path):
    raw_image = cv2.imread(path)
    screen_width, screen_height = 1920,1080
    if raw_image.shape[0] <= screen_height and raw_image.shape[1] <= screen_width:
        image = raw_image
        cv2.imshow("Original Image", raw_image)
    else:
        aspect_ratio = min(screen_width / raw_image.shape[0], screen_height / raw_image.shape[1])
        new_width = int(raw_image.shape[1] * aspect_ratio)
        new_height = int(raw_image.shape[0] * aspect_ratio)
        resized_image = cv2.resize(raw_image, (new_width, new_height))
        image= resized_image
        cv2.imshow("resized_image Image", resized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return image

def outline_image(image):
    rect_roi = cv2.selectROI(image)
    selected_region = image[int(rect_roi[1]):int(rect_roi[1] + rect_roi[3]),
                            int(rect_roi[0]):int(rect_roi[0] + rect_roi[2])]
    cv2.destroyAllWindows()
    cv2.imshow("Selected Region", selected_region)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    bg_img = rembg.remove(selected_region)
    gray_img = cv2.cvtColor(bg_img, cv2.COLOR_BGR2GRAY)
    _, mask = cv2.threshold(gray_img, 0, 255, cv2.THRESH_BINARY)
    kernel = np.ones((3, 3), np.uint8)
    mask = cv2.dilate(mask, kernel, iterations=7)
    kernel = np.ones((3, 3), np.uint8)
    mask = cv2.erode(mask, kernel, iterations=7)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours_scaled = [np.array(contour) + (int(rect_roi[0]), int(rect_roi[1])) for contour in contours]
    cv2.drawContours(image, contours_scaled, -1, (0, 255, 0), 4)
    return image

input_folder_path = 'Task 1/TEST IMAGES'
file_names =  os.listdir(input_folder_path)
for image_name in file_names:
    image_path = os.path.join(input_folder_path,image_name)
    cv2.imshow('Outline the region of intrest',outline_image(resize_img(image_path)))
    key = cv2.waitKey(0)
    if key == ord('c'):
        cv2.destroyAllWindows()
    elif key == ord('q'):
        break
