from data_loader import *
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.image import ImageDataGenerator


def validate_data():
    X, y = load_data(type=0)

    print(f"Number of examples: {len(X)} ")

    plt.imshow(X[0])
    plt.axis("off")
    plt.show()


def get_preprocessed_data():

    X, y = load_data(type=0)

    # Split dataset into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Data augmentation

    datagen = ImageDataGenerator(
        rotation_range=30,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode="nearest",
    )


    datagen.fit(X_train)

    train_aug = datagen.flow(X_train, y_train, batch_size=32)
    
    return train_aug, X_test, y_test
    
    


if __name__ == "__main__":
    validate_data()
