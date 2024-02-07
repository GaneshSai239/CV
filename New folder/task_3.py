import os
import cv2
import easyocr

input_folder_path = 'License Images'
file_names =  os.listdir(input_folder_path)
output_folder_path = "License Images output"
os.makedirs(output_folder_path,exist_ok=True)  
# image = cv2.imread(r'License Images\Alaska.jpg')
reader = easyocr.Reader(['en'])
result = reader.readtext(r'License Images\Alaska.jpg')

def cleanup_text(text):
	return "".join([c if ord(c) < 128 else "" for c in text]).strip()

def ocr(file_names):
    for image_name in file_names:
        image_path = os.path.join(input_folder_path,image_name)
        result = reader.readtext(image_path)
        image = cv2.imread(image_path)
        for (bbox, text, prob) in result:

            (tl, tr, br, bl) = bbox
            tl = (int(tl[0]), int(tl[1]))
            tr = (int(tr[0]), int(tr[1]))
            br = (int(br[0]), int(br[1]))
            bl = (int(bl[0]), int(bl[1]))

            text = cleanup_text(text)
            cv2.rectangle(image, tl, br, (0, 0, 255), 2)
            cv2.putText(image, text, (tl[0], tl[1]-5),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
        
        output_path = os.path.join(output_folder_path,image_name)
        cv2.imwrite(output_path,image)


ocr(file_names)