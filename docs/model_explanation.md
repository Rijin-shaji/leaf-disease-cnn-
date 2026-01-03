# Model Explanation

## Model Type
The project uses a **Custom Convolutional Neural Network (CNN)** designed for binary image classification.

## Why CNN?
CNNs are well suited for image-based tasks because they:
- Capture spatial features
- Learn patterns such as edges, textures, and shapes
- Perform well on visual classification problems

## Model Architecture
The CNN architecture consists of:

1. **Input Layer**
   - Image size: 128 × 128 × 3 (RGB)

2. **Convolution Block 1**
   - Conv2D (32 filters, 3×3)
   - ReLU activation
   - MaxPooling (2×2)

3. **Convolution Block 2**
   - Conv2D (64 filters, 3×3)
   - ReLU activation
   - MaxPooling (2×2)

4. **Convolution Block 3**
   - Conv2D (128 filters, 3×3)
   - ReLU activation
   - MaxPooling (2×2)

5. **Fully Connected Layers**
   - Flatten layer
   - Dense layer (128 neurons, ReLU)
   - Dropout (0.5) to reduce overfitting

6. **Output Layer**
   - Dense (1 neuron)
   - Sigmoid activation for binary classification

## Loss Function
- **Binary Cross-Entropy**

## Optimizer
- **Adam Optimizer**

## Evaluation Metric
- **Accuracy**

## Model Output
- Output value > 0.5 → Infected leaf
- Output value ≤ 0.5 → Healthy leaf
