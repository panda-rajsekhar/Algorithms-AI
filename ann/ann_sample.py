import tensorflow as tf

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import plot_model

import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


# Load dataset
iris = load_iris()

X, y = iris.data, iris.target

# One-hot encoding
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

# Build ANN model
model = Sequential([

    Dense(
        64,
        activation='relu',
        input_shape=(X_train.shape[1],),
        name='Hidden_Layer_1'
    ),

    Dense(
        32,
        activation='relu',
        name='Hidden_Layer_2'
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

# Model summary
model.summary()

# Save model diagram
plot_model(
    model,
    to_file='ann_model.png',
    show_shapes=True,
    show_layer_names=True
)

print("Model architecture saved as ann_model.png")

# Train model
history = model.fit(
    X_train,
    y_train,
    epochs=5,
    batch_size=16,
    validation_split=0.2,
    verbose=1
)

# Evaluate model
test_loss, test_accuracy = model.evaluate(
    X_test,
    y_test,
    verbose=0
)

print(f"\nTest Accuracy: {test_accuracy:.4f}")
print(f"Test Loss: {test_loss:.4f}")

# Plot graphs
plt.figure(figsize=(12, 5))

# Loss plot
plt.subplot(1, 2, 1)

plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')

plt.title('Training and Validation Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')

plt.legend()
plt.grid(True)

# Accuracy plot
plt.subplot(1, 2, 2)

plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')

plt.title('Training and Validation Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')

plt.legend()
plt.grid(True)

plt.tight_layout()

plt.show()
