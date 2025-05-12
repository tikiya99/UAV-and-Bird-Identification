# UAV-and-Bird-Identification
This repository consists of the codebase for the UAV and Bird identification model.

## Table of Contents

- [Intrduction](#introduction)
- [Dataset](#Dataset)
- [File Strcuture](#filestructure)
- [Screenshots](#screenshots)
- [Results](#results)
- [Installation](#installation)
- [Conclusion](#conclusion)

## Introduction

The model here is trained to identify birds and UAVs (Drones) for safety purposes. The model proposed an accuracy above 95% in all classes and for Birds and UAVs separately. The ultimate goal of developing this model was to run it in real-time with lower inference time and better accuracy when compared to other lightweight models

## Dataset
This is a custom dataset that integrates multiple datasets for more scenarios.
The following are the data instances for each defect.
          Images        Instances
Birds       3581           22620
UAV         3334            3571 

## File Structure

UAVBirds/
├── merged/                 # Static assets (images, favicon, etc.)
│   └── Images/
│       └── Test/         # Reusable components
│       ├── Train/         # Reusable components
│       └── Valid/         # Reusable components
│   ├── Labels/         # Reusable components
│       └── Test/         # Reusable components
│       ├── Train/         # Reusable components
│       └── Valid/         # Reusable components
│   └── data,yaml              # Root component
├── README.md               # Project documentation
└── LICENSE                 # License file

ircraft_defect_yolov11/
├── scripts/
|    ├── inf.py
|    ├── script.py
|    ├── video_script.py
├── configs/
|    ├── data.yaml
├── models/
│    ├── best.pt
│    ├── yolo11s.pt
├── input/
│    ├── 3.jpg
│    ├── test_video.mp4
├── runs/detect/aircraft_defect_yolov1111/
│    ├── weights/
│    │    ├── best.pt
│    │    ├── last.pt
├── dataset/
│    ├── train/
│    │    ├── images/
│    │    ├── labels/
│    ├── valid/
│    │    ├── images/
│    │    ├── labels/
│    ├── test/
│    │    ├── images/
│    │    ├── labels/
├── requirements.txt
└── readme.md


## Screenshots

The following image is based on the model training. Training summary;



Test video;

## Results

## Installation

```bash
# Clone the repository
git clone https://github.com/ultralytics/ultralytics
cd ultralytics

# Install dependencies (choose one)
pip install -r requirements.txt

## Download the model

