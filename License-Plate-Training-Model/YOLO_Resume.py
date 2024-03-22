from ultralytics import YOLO
import os


new_directory = '/home/nitzz/PycharmProjects/Vehicle-Profiling-YOLOV8/License-Plate-Detector-YOLOV8/License-Plate-Training-Model/runs/detect/train2/'
os.chdir(new_directory)

# Load a model
model = YOLO('weights/last.pt') # load a partial

# Resume training
results = model.train(resume=True, epochs=65)

