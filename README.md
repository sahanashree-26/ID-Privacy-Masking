ID Image Privacy Protection using OCR and Masking:

A simple cybersecurity project to protect personal data in ID card images using Python, OpenCV, and Tesseract OCR. Developed for a Hackathon.

 Objective:

To automatically detect and hide sensitive information (like name, roll number, and batch) from ID card images using OCR and image masking techniques.

 Technologies Used:

- Python 
- OpenCV
- Tesseract OCR
- Image Processing

 How It Works?

1. Load the ID card image using OpenCV.
2. Extract text and word positions using Tesseract OCR.
3. Define a list of sensitive words to mask.
4. Loop through all detected words.
5. Draw black rectangles over matching words.
6. Save the masked image.

