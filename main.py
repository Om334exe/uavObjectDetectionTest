#install ultralytics #pip install ultralytics
from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n.yaml")  # build a new model from scratch

# Use the model
#To make the model better more and more data should be finetuned to the PretrainedModel
results = model.train(data="config.yaml", epochs=50)  # train the model
#After training for testing the object detection we can pass any video or image
#results = model(source = "test.mp4" , show = True , conf = 0.4 , save = True)
