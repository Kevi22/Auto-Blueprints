import os
import random
import shutil

# Define paths
image_dir = "data_warehouse/Kindergardens"  # Folder where all your images are
label_dir = "data_warehouse/txt_files"  # Folder where all your labels are

train_image_dir = "dataset/images/train"
val_image_dir = "dataset/images/val"
train_label_dir = "dataset/labels/train"
val_label_dir = "dataset/labels/val"

# Create directories if they don't exist
for d in [train_image_dir, val_image_dir, train_label_dir, val_label_dir]:
    os.makedirs(d, exist_ok=True)

# Get all image files
images = [f for f in os.listdir(image_dir) if f.endswith(".png") or f.endswith(".jpg")]

# Shuffle and split (80% train, 20% val)
random.shuffle(images)
split_index = int(0.8 * len(images))
train_images = images[:split_index]
val_images = images[split_index:]

# Move files
for img in train_images:
    label = img.replace(".png", ".txt").replace(".jpg", ".txt")

    if os.path.exists(os.path.join(label_dir, label)):
        shutil.move(os.path.join(image_dir, img), os.path.join(train_image_dir, img))
        shutil.move(os.path.join(label_dir, label), os.path.join(train_label_dir, label))
    else:
        print(f"No label found for {img}")

for img in val_images:
    label = img.replace(".png", ".txt").replace(".jpg", ".txt")

    if os.path.exists(os.path.join(label_dir, label)):
        shutil.move(os.path.join(image_dir, img), os.path.join(val_image_dir, img))
        shutil.move(os.path.join(label_dir, label), os.path.join(val_label_dir, label))
    else:
        print(f"no label found in {img}")

    

print("Dataset split completed!")
