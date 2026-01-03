# Data Description

## Dataset Overview
The dataset consists of plant leaf images collected for detecting leaf diseases.
Each image belongs to one of two classes representing the health condition of the leaf.

## Classes
- **good** → Healthy leaf images
- **infected** → Diseased leaf images

## Data Organization
Raw images are stored class-wise and later split into training, validation, and testing sets.


## Dataset Split
The dataset is split automatically using a Python script:

- **Training set:** 70%
- **Validation set:** 15%
- **Test set:** 15%


## Image Preprocessing
- Images are resized to **128 × 128**
- Pixel values are normalized to range **[0, 1]**
- Color space converted from **BGR to RGB**

## Data Augmentation
To improve model generalization and reduce overfitting, the following augmentations are applied:
- Rotation
- Zoom
- Width & height shift
- Horizontal flip

---

## Purpose of the Dataset
This dataset is used to train a Convolutional Neural Network (CNN) to automatically identify leaf diseases from images, supporting early disease detection in agriculture.

