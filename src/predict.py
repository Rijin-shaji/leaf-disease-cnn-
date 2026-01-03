import cv2
import numpy as np
import tensorflow as tf

IMG_SIZE = 128

def predict_leaf(image_path):
    model = tf.keras.models.load_model("models/leaf_disease_cnn.h5")

    img = cv2.imread(image_path)

    if img is None:
        print(" Error: Image not found")
        return

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)

    prediction = model.predict(img)[0][0]

    if prediction > 0.5:
        print(" Infected Leaf")
    else:
        print(" Healthy Leaf")

    print(f"Confidence Score: {prediction:.2f}")

predict_leaf(r"F:/11.JPG")
