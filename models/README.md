# Models Directory

## Overview
This folder contains the trained deep learning models generated during the training phase of the project.

All models saved here are used for inference and evaluation without retraining.

---

## Stored Model

### `leaf_disease_cnn.h5`
- Trained Convolutional Neural Network (CNN) model
- Used to classify leaf images as **Healthy** or **Infected**
- Saved automatically during training using ModelCheckpoint
- Represents the best-performing model based on validation accuracy

---

## Model Format
- File format: **HDF5 (.h5)**
- Framework: **TensorFlow / Keras**

---

## How the Model Is Used
- Loaded during inference for single-image prediction
- Used in `src/predict.py`
- Can be integrated into web or mobile applications

---

## Reproducibility
If the model file is not present:
1. Run the dataset splitting script
2. Train the model using `src/train.py`
3. The trained model will be saved automatically in this folder

---

## Notes
- Model files can be large and may be ignored in Git using `.gitignore`
- Recommended to upload models using Git LFS if pushing to GitHub
