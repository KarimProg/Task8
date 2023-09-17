# Import Module
from ultralytics import YOLO
import cv2

# Set dependency paths
model_path = r'C:\Users\karim\OneDrive\Desktop\Task 8\best.pt'
media_path = r'C:\Users\karim\OneDrive\Desktop\Task 8\coins002.jpg'

# Set model's path
model = YOLO(model_path)

img = cv2.imread(media_path)

# Calculate the new width while preserving the aspect ratio
target_height = 700  # Specify the desired height
aspect_ratio = img.shape[1] / img.shape[0]
target_width = int(target_height * aspect_ratio)

# Resize the image
resized_img = cv2.resize(img, (target_width, target_height))

# Use model on multimedia
img = model.predict(source=resized_img, classes= [0,1,2], show= True)

# Simple method to stop window from closing too fast, press Enter to close!!
input("Press Enter to close the window...")