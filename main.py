import cv2

# Load the original blueprint
img = cv2.imread("/Users/kevin/Documents/Github/Auto-Blueprints/data_warehouse/Kindergardens/Rose_0210.png")

# Get height and width
h, w, _ = img.shape

# Crop bottom center area for scale info
scale = img[h-150:h, w//4:3*w//4]
cv2.imwrite("test.png", scale)

print("✅ Cropped scale legend saved to test.png")
