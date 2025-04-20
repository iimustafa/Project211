"""
Training script for the stadium crowd detection model.
This script loads the synthetic dataset and trains the fan detection model.
"""

import os
import tensorflow as tf
import matplotlib.pyplot as plt
from src.data_utils import StadiumDataset
from src.model import FanDetectionModel

# Set up GPU memory growth to avoid OOM errors
gpus = tf.config.experimental.list_physical_devices('GPU')
if gpus:
    try:
        for gpu in gpus:
            tf.config.experimental.set_memory_growth(gpu, True)
    except RuntimeError as e:
        print(e)

# Configuration
DATASET_DIR = 'stadium_dataset'  # Path to the dataset directory
MODEL_DIR = 'models'
BATCH_SIZE = 8
EPOCHS = 20
INPUT_SHAPE = (384, 512, 3)  # Height, width, channels

# Create model directory if it doesn't exist
os.makedirs(MODEL_DIR, exist_ok=True)

# Load and prepare the dataset
print("Loading dataset...")
dataset = StadiumDataset(DATASET_DIR, image_size=(512, 384))
dataset.load_annotations()

# Visualize a sample image
print("Visualizing a sample image...")
sample_id = dataset.image_ids[0]
dataset.visualize_sample(sample_id)

# Prepare datasets for training
print("Preparing datasets for training...")
train_dataset, val_dataset = dataset.prepare_detection_dataset(
    train_ratio=0.8, 
    batch_size=BATCH_SIZE
)

# Build and train the model
print("Building model...")
model = FanDetectionModel(input_shape=INPUT_SHAPE)
model.build_model()

# Define callbacks
callbacks = [
    tf.keras.callbacks.ModelCheckpoint(
        filepath=os.path.join(MODEL_DIR, 'fan_detection_model.h5'),
        save_best_only=True,
        monitor='val_loss'
    ),
    tf.keras.callbacks.EarlyStopping(
        patience=5,
        monitor='val_loss'
    ),
    tf.keras.callbacks.ReduceLROnPlateau(
        factor=0.2,
        patience=3,
        monitor='val_loss'
    ),
    tf.keras.callbacks.TensorBoard(
        log_dir=os.path.join(MODEL_DIR, 'logs'),
        histogram_freq=1
    )
]

# Train the model
print("Training model...")
history = model.train(
    train_dataset=train_dataset,
    val_dataset=val_dataset,
    epochs=EPOCHS,
    callbacks=callbacks
)

# Plot training history
plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(history.history['class_output_accuracy'], label='Class Accuracy')
plt.plot(history.history['team_output_accuracy'], label='Team Accuracy')
plt.plot(history.history['action_output_accuracy'], label='Action Accuracy')
plt.title('Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()

plt.tight_layout()
plt.savefig(os.path.join(MODEL_DIR, 'training_history.png'))

print(f"Model training completed. Model saved to {os.path.join(MODEL_DIR, 'fan_detection_model.h5')}")
