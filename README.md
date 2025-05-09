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


Test video;


##


## 🛠 Installation

```bash
# Clone the repository
git clone https://github.com/[USERNAME]/[REPO-NAME].git
cd [REPO-NAME]

# Install dependencies (choose one)
npm install
# or
pip install -r requirements.txt

## 🛠 Installation
