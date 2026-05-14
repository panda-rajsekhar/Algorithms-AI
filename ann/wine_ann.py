import tensorflow as tf

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, BatchNormalization
from tensorflow.keras.utils import plot_model

import matplotlib.pyplot as plt
import numpy as np

from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report


# Load Wine Dataset
wine = load_wine()

X = wine.data
y = wine.target


# Convert labels to categorical
# 3 output classes

y = tf.keras.utils.to_categorical(y, num_classes=3)


# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Feature scaling
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


# Build Advanced ANN
model = Sequential([

    Dense(
        128,
        activation='relu',
        input_shape=(X_train.shape[1],),
        name='Input_Hidden_Layer'
    ),

    BatchNormalization(),

    Dropout(0.3),


    Dense(
        64,
        activation='relu',
        name='Hidden_Layer_2'
    ),

    BatchNormalization(),

    Dropout(0.3),


    Dense(
        32,
        activation='relu',
        name='Hidden_Layer_3'
    ),


    Dense(
        3,
        activation='softmax',
        name='Output_Layer'
    )

])


# Compile model
model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)


# Show model summary
model.summary()


# Save model architecture image
plot_model(
    model,
    to_file='wine_ann_model.png',
    show_shapes=True,
    show_layer_names=True
)

print("Wine ANN architecture saved as wine_ann_model.png")


# Train model
history = model.fit(
    X_train,
    y_train,
    epochs=25,
    batch_size=16,
    validation_split=0.2,
    verbose=1
)


# Evaluate model
loss, accuracy = model.evaluate(
    X_test,
    y_test,
    verbose=0
)

print(f"\nTest Accuracy: {accuracy:.4f}")
print(f"Test Loss: {loss:.4f}")


# Predictions
predictions = model.predict(X_test)

predicted_classes = np.argmax(predictions, axis=1)
actual_classes = np.argmax(y_test, axis=1)


# Classification Report
print("\nClassification Report:\n")
print(classification_report(actual_classes, predicted_classes))


# Plot graphs
plt.figure(figsize=(12, 5))


# Loss Plot
plt.subplot(1, 2, 1)

plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')

plt.title('Training vs Validation Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')

plt.legend()
plt.grid(True)


# Accuracy Plot
plt.subplot(1, 2, 2)

plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')

plt.title('Training vs Validation Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')

plt.legend()
plt.grid(True)


plt.tight_layout()
plt.show()
