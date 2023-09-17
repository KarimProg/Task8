# Import Module
from ultralytics import YOLO

# Set model's path
model = YOLO('')

# Use model on multimedia
model.predict(source='', classes= [0,1,2], show= True)