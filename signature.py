import cv2

# Load image
img = cv2.imread('document.jpg')

# Convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply binary threshold to create a black and white image
_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

# Find contours in the image
contours, _ = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# Create an empty list to store signature contours
signature_contours = []

# Loop through all the contours and check if they meet the signature criteria
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    aspect_ratio = w / float(h)
    area = cv2.contourArea(contour)
    if aspect_ratio > 0.8 and aspect_ratio < 1.2 and area > 1000 and area < 5000:
        signature_contours.append(contour)

# Draw bounding boxes around the detected signatures
for contour in signature_contours:
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Display the result
cv2.imshow('Signature Detection', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
