from ultralytics import YOLO
import os


new_directory = '/home/nitzz/PycharmProjects/Vehicle-Profiling-YOLOV8/License-Plate-Detector-YOLOV8/License-Plate-Training-Model/'
os.chdir(new_directory)


# Load a model
model = YOLO("runs/detect/train2/weights/last.pt")  # build a new model from scratch
# model = YOLO("yolov8s.pt")  # load a pretrained model (recommended for training)

# Use the model
results = model.train(data="plate.yaml", epochs=2)  # train the model
metrics = model.val()  # evaluate model performance on the validation set
# results = model("https://ultralytics.com/images/bus.jpg")   # predict on an image
