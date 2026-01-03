# leaf-disease-cnn-
A CNN-based image classification system to detect healthy and diseased leaves using computer vision and deep learning.

#  Leaf Disease Detection using CNN

Deep learning–based plant leaf disease classification system using Convolutional Neural Networks (CNN) to identify infected and healthy leaves from images for early crop disease detection.

---

## Leaf Disease Detection – CNN-Based Image Classification System

### Overview
This project implements a computer vision–based deep learning system to automatically detect plant leaf diseases from images.  
A custom-built Convolutional Neural Network (CNN) is trained to classify leaf images into **Healthy** or **Infected**, helping farmers and researchers identify plant diseases at an early stage.

---

## Objectives
- Classify leaf images as **Healthy** or **Infected**
- Improve model performance using image augmentation
- Train a custom CNN for binary image classification
- Enable single-image prediction for real-world usage
- Build a clean and scalable machine learning pipeline

---

## Model Used
- **Custom Convolutional Neural Network (CNN)**
  - Convolution + MaxPooling layers
  - Fully connected layers with Dropout
  - Sigmoid activation for binary classification

---

## Tech Stack
- Python  
- TensorFlow / Keras  
- OpenCV  
- NumPy  

---

## Project Structure
leaf-disease-cnn/
│
├── README.md                  # Project overview and instructions
├── requirements.txt           # Python dependencies
├── .gitignore                 # Files ignored by Git
│
├── data/
│   ├── raw/
│   │   └── leaf/
│   │       ├── infected/      # Original infected leaf images
│   │       └── good/          # Original healthy leaf images
│   │
│   └── processed/
│       └── dataset_split/
│           ├── train/         # Training images
│           ├── val/           # Validation images
│           └── test/          # Test images
│
├── src/
│   ├── data_split.py          # Dataset splitting logic
│   ├── data_generator.py      # Image augmentation & generators
│   ├── model.py               # CNN architecture
│   ├── train.py               # Model training pipeline
│   └── predict.py             # Single image prediction
│
├── models/
│   └── leaf_disease_cnn.h5    # Trained CNN model
│
├── results/
│   └── training_logs.txt      # Training metrics (optional)
│
└── docs/
    └── system_architecture.png # End-to-end pipeline diagram


---

## Results
- Accurate classification of leaf images
- Improved generalization using data augmentation
- Successful single-image prediction
- Modular and reusable deep learning pipeline

---

## Installation & Usage

### Clone the Repository
```bash
git clone https://github.com/Rijin-shaji/leaf-disease-cnn.git
cd leaf-disease-cnn

