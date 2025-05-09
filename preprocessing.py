import cv2

def preprocess_image(img):
    # Resize
    resized = cv2.resize(img, (256, 256))

    # Convert to HSV
    hsv_img = cv2.cvtColor(resized, cv2.COLOR_BGR2HSV)

    # Convert to Grayscale for thresholding
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

    # Apply Otsu’s thresholding
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Merge threshold with resized image
    result = cv2.merge([thresh, thresh, thresh])
    return result
