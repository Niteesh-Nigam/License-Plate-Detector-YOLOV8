# License Plate Recognition System Using YOLOv8
# Project Overview
This project develops a robust license plate recognition system utilizing the YOLOv8 deep learning model. This repository contains training scripts, detailed configuration files, and extensive documentation about the dataset sourced and processed through Roboflow.

To access any of my trained models contact me at niteesh.nigam99@gmail.com

# Repository Contents
YOLO_Resume.py: Script to resume training the YOLO model from the last saved checkpoint.
LP_Train.py: Script for initial training of the YOLO model on license plate images.
plate.yaml: Configuration file used for setting up dataset paths and training parameters.
args.yaml: Contains hyperparameters and settings for training the YOLO model.
Visualization Images: Includes confusion matrices, F1 curves, precision-recall curves, etc. (Images will need to be manually uploaded to GitHub by the repository manager)
README.dataset.txt and README.roboflow.txt: Documentation files describing the dataset and its source.

# Model Configuration and Training
# Configuration
The model uses configuration settings specified in plate.yaml which define the dataset paths:

Train: ../train/images
Validation: ../valid/images
Test: ../test/images
Classes: 1 (License Plate)
Additional settings from args.yaml include:

Batch size: 16
Image size: 640x640
Epochs: 2 for initial training, 65 for resumed training
Augmentations: Detailed in README.roboflow.txt

# Training Scripts
LP_Train.py: Initiates a new training session from scratch or from a pre-trained model, as specified by the path to weights/last.pt.
YOLO_Resume.py: Continues training from a partially trained model state, enabling extended training sessions.
Dataset
The dataset used in this project is sourced from multiple Roboflow projects, compiled into a comprehensive set of 24,242 annotated images for license plate recognition.

# Preprocessing and Augmentation
As detailed in README.roboflow.txt, the images undergo several preprocessing steps:

Auto-orientation of pixel data with EXIF-orientation stripping
Resize to 640x640 pixels (Stretch)
Augmentations applied to each source image include:

50% probability of horizontal flip
Random cropping between 0 and 15 percent of the image
Random rotation between -10 and +10 degrees
Random brightness and exposure adjustments
Installation and Usage
Instructions on setting up the environment and running the training scripts are provided.

# Visualization of Results
![confusion_matrix](https://github.com/Niteesh-Nigam/License-Plate-Detector-YOLOV8/assets/164087550/e3e47b75-ef7a-4bf4-8b65-28ed968bc38f)
![confusion_matrix_normalized](https://github.com/Niteesh-Nigam/License-Plate-Detector-YOLOV8/assets/164087550/4adacf76-9160-4ccb-ac62-9482568349e1)
![F1_curve](https://github.com/Niteesh-Nigam/License-Plate-Detector-YOLOV8/assets/164087550/659971c4-2877-4384-888c-7359947c763a)
![labels](https://github.com/Niteesh-Nigam/License-Plate-Detector-YOLOV8/assets/164087550/61b6a7a0-a9b0-4da3-8444-40dd0680e43a)
![labels_correlogram](https://github.com/Niteesh-Nigam/License-Plate-Detector-YOLOV8/assets/164087550/3e0d99c1-9b83-4e01-b3e3-441b8b669c1c)
![P_curve](https://github.com/Niteesh-Nigam/License-Plate-Detector-YOLOV8/assets/164087550/2071960f-7b5f-403e-99dd-e8be66c3c128)
![PR_curve](https://github.com/Niteesh-Nigam/License-Plate-Detector-YOLOV8/assets/164087550/1374ff9a-042e-4b33-aac2-fe521a0414d9)
![R_curve](https://github.com/Niteesh-Nigam/License-Plate-Detector-YOLOV8/assets/164087550/0580f185-f727-469d-8550-5c364f611821)
![results](https://github.com/Niteesh-Nigam/License-Plate-Detector-YOLOV8/assets/164087550/be29a0a2-ac1c-4cfd-a518-465d64172108)

