import cv2
import numpy as np
import easyocr
import pdf2image
import re
import pandas as pd

pdf_path = "data_lake/blueprints/bygg/6.4 Ritningar/6.4.1 Arkitekt ritningar.pdf"

#related keys
window_keywords = ["FÖ", "FAÖ", "FTÖ", "FAF", "FTF"]


reader = easyocr.Reader(['sv','en'])

detected_windows = []

def preprocess_image(image):
    img = np.array(image.convert('L')) 
    img = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))  
    img = cv2.GaussianBlur(img, (3, 3), 0)  
    img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)  
    return img

def process_page(image, page_num):
    preprocessed_img = preprocess_image(image)  
    result = reader.readtext(preprocessed_img, detail=0)  
    print(f"Page {page_num + 1} OCR Result: {result}")  

    for text in result:
        if text and re.match(r"(?i)\bF[TA]*[ÖF]+[0-9a-zA-Z]*\b", text):  # Regex to allow for "FAFÖ2b", "FTF", etc.
            detected_windows.append(text)  

info = pdf2image.pdfinfo_from_path(pdf_path)
total_pages = info["Pages"]

for i in range(total_pages):
    print(f"Processing page {i+1} of {total_pages}")  
    images = pdf2image.convert_from_path(pdf_path, first_page=i+1, last_page=i+1, dpi=200)  
    process_page(images[0], i) 

df = pd.DataFrame(detected_windows, columns=["Window Type"])

if len(df) > 0:
    summary = df["Window Type"].value_counts()
    print("Window type counts:")
    print(summary)
    df.to_csv("window_report.csv", index=False)
else:
    print("No window types detected.")