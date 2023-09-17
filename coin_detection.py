# Import Module
from ultralytics import YOLO

# Set dependency paths
model_path = ''
media_path = ''

# Set model's path
model = YOLO(model_path)

# Use model on multimedia
model.predict(source=media_path, classes= [0,1,2], show= True)