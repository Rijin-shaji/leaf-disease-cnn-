# Project Workflow

## Step 1: Data Collection
Leaf images are collected and organized into two classes:
- Healthy leaves
- Infected leaves

## Step 2: Dataset Splitting
The dataset is split into training, validation, and testing sets using a fixed ratio:
- 70% training
- 15% validation
- 15% testing

## Step 3: Data Preprocessing
- Resize images to 128 × 128
- Normalize pixel values
- Convert images to RGB format

## Step 4: Data Augmentation
Augmentation techniques are applied during training to increase data diversity:
- Rotation
- Zoom
- Shift
- Horizontal flip

## Step 5: Model Training
- A custom CNN model is trained using the training dataset
- Validation data is used to monitor performance
- Early stopping is applied to avoid overfitting
- Best model weights are saved

## Step 6: Model Evaluation
- Model performance is evaluated using validation accuracy
- Training behavior can be analyzed using logs

## Step 7: Prediction
- The trained model is used to predict the class of a single input image
- Output includes predicted class and confidence score

## Step 8: Deployment Ready
- The trained model can be integrated into:
  - Web applications
  - Mobile apps
  - Smart agriculture systems
