import pytesseract
from PIL import Image
import os

# (Optional) set tesseract path manually if needed
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_malayalam_text(image_path):
    # Open the image
    img = Image.open(image_path)
    
    # Use tesseract to extract Malayalam text
    text = pytesseract.image_to_string(img, lang='mal')
    
    return text

