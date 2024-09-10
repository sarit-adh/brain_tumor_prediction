from modeling import Model
from preprocessing import get_preprocessed_data
from argparse import ArgumentParser

def main():
    
    # Create the argument parser and parse the arguments
    parser = ArgumentParser()
    parser.add_argument("--model", type=str, default="vgg16", help="Base Model Name (default: vgg16)")
    parser.add_argument("--epochs", type=int, default=10, help="Number of epochs (default: 10)")
    parser.add_argument("--task", type=str, choices=["train", "load"], default="load", help="Task : 'train' trains the model and saves the trained model, 'load' loads the saved model and performs evaluation")
    parser.add_argument("--data_dir", type=str, default="../data/raw/", 
                        help="Folder to load the data from (default: ../data/raw/)")
    parser.add_argument("--model_dir", type=str, default="../trained_models/", 
                        help="Folder to save or load the model (default: ../trained_models/)")
    
    
    
    args = parser.parse_args()
    
    base_model = args.model
    epochs = args.epochs
    task = args.task
    data_folder = args.data_dir
    trained_model_folder = args.model_dir
    
    model = Model(base_model, epochs)
    train_aug, X_test, y_test = get_preprocessed_data(data_folder)
    
    if task=="train":
        # Train and save the model
        model.create_model(train_aug, X_test, y_test)
        model.evaluate_model(X_test, y_test)
        model.persist_model(trained_model_folder)
        
    if task=="load":
        # Load the trained model
        model.load_model(trained_model_folder)
        model.evaluate_model(X_test, y_test)
    
    
    
if __name__=="__main__":
    main()