import pytesseract
from PIL import Image
import os

# Set tesseract path
pytesseract.pytesseract.tesseract_cmd = r'tess\tesseract.exe'

# Load an image from the same folder (replace with your image file)
image = Image.open("sample_id.jpg")

# OCR to extract text
text = pytesseract.image_to_string(image)

print("Extracted Text:")
print(text)
