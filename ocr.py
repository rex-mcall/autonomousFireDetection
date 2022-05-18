import pytesseract
import cv2

def max_temp(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cropped = image[130:150, 105:120]
    cv2.imshow(cropped)

    result = pytesseract.image_to_string(cropped)[:-2]

    try:
        return int(result)
    except:
        return -1