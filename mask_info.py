import cv2
import pytesseract

# Set path to your Tesseract installation
pytesseract.pytesseract.tesseract_cmd = r'tess\tesseract.exe'

# Load the image
img = cv2.imread('sample_id.jpg')

# Make sure the image loads
if img is None:
    print("❌ Error: Could not load 'sample_id.jpg'. Please check the filename.")
    exit()

# Extract text with box positions
data = pytesseract.image_to_data(img, output_type=pytesseract.Output.DICT)

# Words to hide
sensitive_words = ['SAHANA', 'SHREE', '23JEIT212', '2023', '2027']

# Loop through all detected words
n_boxes = len(data['text'])
for i in range(n_boxes):
    word = data['text'][i]
    if any(s in word for s in sensitive_words):
        (x, y, w, h) = (data['left'][i], data['top'][i], data['width'][i], data['height'][i])
        # 🖤 Draw a black rectangle instead of blurring
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 0), -1)

# Save the final image
cv2.imwrite('masked_id.jpg', img)
print("✅ Sensitive info masked with black boxes and saved as 'masked_id.jpg'")
