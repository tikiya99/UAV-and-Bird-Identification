# UAV-and-Bird-Identification
This repository consists of the codebase for the UAV and Bird identification model.

## Table of Contents

- [Intrduction](#introduction)
- [Installation](#installation)
- [File Strcuture](#filestructure)
- [Screenshots](#screenshots)
- [Results](#results)
- [Conclusion](#conclusion)

## Introduction

The model here is trained for identifying birds and UAVs (Drones) for safety purposes. The model proposed an accuracy above 95% in all classes and for Birds and UAVs separately. The ultimate goal of developing this model was to run it in real-time with lower inference time and better accuracy when compared to other lightweight models

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

## Screenshots

The following image is based on the model training. Training summary;
![Screenshot from 2025-05-11 21-01-57](https://github.com/user-attachments/assets/088cd9c9-5df8-4b07-8e20-7011a45f0c9d)


Test video;



## 🛠 Installation

```bash
# Clone the repository
git clone https://github.com/ultralytics/ultralytics
cd ultralytics

# Install dependencies (choose one)
pip install -r requirements.txt

## Download the model

