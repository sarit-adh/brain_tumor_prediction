from data_loader import *
import matplotlib.pyplot as plt


def validate_data():
    X, y = load_data(type=0)

    print(f"Number of examples: {len(X)} ")

    plt.imshow(X[0])  
    plt.axis('off')  
    plt.show()



if __name__=="__main__":
    validate_data()