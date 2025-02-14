import torch
import cv2
import pytesseract
import numpy as np
from pdf2image import convert_from_path
from PIL import Image
from ultralytics import YOLO

# 🔹 Load YOUR trained YOLOv5 model
model = YOLO("yolov5su.pt")  

def pdf_to_images(pdf_path, dpi=150):
    pages = convert_from_path(pdf_path, dpi)
    image_paths = []
    for i, page in enumerate(pages):
        image_path = f"page_{i+1}.png"
        page.save(image_path, "PNG")
        image_paths.append(image_path)
    return image_paths

def extract_text_from_region(image, box):
    x1, y1, x2, y2 = map(int, box)
    roi = image[y1:y2, x1:x2]
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray, config="--psm 6")
    return text.strip()

def detect_windows(image_path):
    image = cv2.imread(image_path)
    results = model(image)
    windows = results.pandas().xyxy[0]

    detected_windows = []
    for _, row in windows.iterrows():
        x1, y1, x2, y2, confidence, cls = row[['xmin', 'ymin', 'xmax', 'ymax', 'confidence', 'name']]
        if confidence > 0.5:
            text = extract_text_from_region(image, (x1, y1, x2, y2))
            detected_windows.append({"box": (x1, y1, x2, y2), "text": text})
    
    return detected_windows

pdf_path = "data_lake/blueprints/bygg/6.4 Ritningar/6.4.1 Arkitekt ritningar.pdf"
image_paths = pdf_to_images(pdf_path)

all_windows = []
for img_path in image_paths:
    windows = detect_windows(img_path)
    all_windows.extend(windows)

for i, window in enumerate(all_windows):
    print(f"Window {i+1}:")
    print(f"  Bounding Box: {window['box']}")
    print(f"  Extracted Text: {window['text']}")
    print("--------------------------------------------------")
