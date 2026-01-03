from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from data_generator import get_generators
from model import build_model

EPOCHS = 25

train_data, val_data = get_generators()

model = build_model()
model.summary()

callbacks = [
    EarlyStopping(patience=5, restore_best_weights=True),
    ModelCheckpoint("models/leaf_disease_cnn.h5", save_best_only=True)
]

print("🔹 Training CNN model...")

model.fit(
    train_data,
    validation_data=val_data,
    epochs=EPOCHS,
    callbacks=callbacks
)

print("Model training completed")
