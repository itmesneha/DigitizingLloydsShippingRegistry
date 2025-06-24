import cv2
import pytesseract
import pandas as pd
import numpy as np
from PIL import Image

# Load and preprocess image
img_path = 'page154.png'  # Update with your actual image
img = cv2.imread(img_path)

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Thresholding to improve contrast
_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

# Optional: dilate to fix broken letters
kernel = np.ones((1, 1), np.uint8)
processed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

# OCR configuration
custom_config = r'--oem 3 --psm 6'  # Assume a single uniform block of text

# Run OCR
text = pytesseract.image_to_string(thresh, config=custom_config)

# Save raw text output
with open("tesseract_raw_ocr_output.txt", "w", encoding="utf-8") as f:
    f.write(text)

# Read raw OCR output
with open("tesseract_raw_ocr_output.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Remove empty lines and strip whitespace
cleaned_lines = [line.strip() for line in lines if line.strip() != ""]

# Keep every alternate line: 0, 2, 4, ...
# filtered_lines = [line for i, line in enumerate(lines) if i % 2 == 0]

# Save to new file
with open("tesseract_cleaned_ocr_output.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(cleaned_lines))

