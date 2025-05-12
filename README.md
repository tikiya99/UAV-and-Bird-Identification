# UAV-and-Bird-Identification
This repository consists of the codebase for the UAV and Bird identification model.

## Table of Contents

- [Intrduction](#introduction)
- [Dataset](#Dataset)
- [File Strcuture](#filestructure)
- [Screenshots](#screenshots)
- [Results](#results)
- [Installation](#installation)

## Introduction

The model here is trained to identify birds and UAVs (Drones) for safety purposes. The model proposed an accuracy above 90% in all classes and for Birds and UAVs separately. The ultimate goal of developing this model was to run it in real-time with lower inference time and better accuracy when compared to other lightweight models

## Dataset
This is a custom dataset that integrates multiple datasets for more scenarios.
The following are the data instances for each defect. <br>
          Images        Instances <br>
Birds       3581           22620  <br>
UAV         3334            3571 

## File Structure

UAVBirds/ <br>
├── merged/  <br>           
│   └── Images/ <br>
│   │   └── Test/ <br>  
│   │   ├── Train/ <br>   
│   │   └── Valid/ <br>     
│   ├── Labels/ <br>     
│   │   └── Test/ <br>      
│   │   ├── Train/ <br>    
│   │   └── Valid/ <br>      
│   └── data,yaml <br>         
├── Weights #best and last .pt files  <br>
└── README.md <br>        


## Screenshots

The following image is based on the model training. Training summary;
![Screenshot from 2025-05-12 11-27-10](https://github.com/user-attachments/assets/a78655c5-3de2-419c-8b1a-1a5f27a2ac70)


## Results

Training results; 
![results](https://github.com/user-attachments/assets/93a37212-09b1-4585-b3eb-71832391f320)


## Installation

```bash
# Clone the repository
git clone https://github.com/ultralytics/ultralytics
cd ultralytics

# Install dependencies (choose one)
pip install -r requirements.txt

## Download the model
https://github.com/tikiya99/UAV-and-Bird-Identification.git
