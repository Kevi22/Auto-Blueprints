from ultralytics import YOLO

# Load the trained YOLO model
model = YOLO("yolov5su.pt")  # Directly use YOLO class

# Run inference to check if it works
results = model("data_warehouse/Kindergardens/Blåsväder6_19.png")  # Replace with an actual image path

# Print detected objects
for r in results:
    print(r.boxes)
