import os
import subprocess
import zipfile
from dotenv import load_dotenv

def set_kaggle_credentials():
    # Load environment variables from .env file
    load_dotenv()

    # Check if Kaggle credentials are present in the environment
    kaggle_username = os.getenv('KAGGLE_USERNAME')
    kaggle_key = os.getenv('KAGGLE_KEY')
    
    if not kaggle_username or not kaggle_key:
        raise EnvironmentError("Kaggle API credentials not found. Please set them in the .env file.")
    
    # Set them as environment variables in the current session
    os.environ['KAGGLE_USERNAME'] = kaggle_username
    os.environ['KAGGLE_KEY'] = kaggle_key

def download_kaggle_dataset(dataset, data_path):
    # Ensure Kaggle CLI is installed
    try:
        subprocess.run(['kaggle', '--version'], check=True)
    except subprocess.CalledProcessError:
        raise EnvironmentError("Kaggle CLI is not installed. Run 'pip install kaggle' to install it.")
    
    # Download dataset using Kaggle API
    command = ['kaggle', 'datasets', 'download', '-d', dataset, '-p', data_path]
    
    try:
        subprocess.run(command, check=True)
        print(f"Dataset downloaded successfully and saved to {data_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error downloading dataset: {e}")

def find_zip_file(directory):
    # Find the zip file in the specified directory
    for file in os.listdir(directory):
        if file.endswith('.zip'):
            return os.path.join(directory, file)
    return None

def unzip_file(file_path, extract_to):
    # Unzip the file
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print(f"File {file_path} unzipped successfully to {extract_to}")

if __name__ == "__main__":
    # Load Kaggle API credentials from .env file
    set_kaggle_credentials()

    # Specify dataset name (e.g., 'username/dataset-name') and path to download data
    dataset_name = 'navoneel/brain-mri-images-for-brain-tumor-detection'  # Replace with actual dataset identifier
    download_path = './data/raw'

    # Create download directory if it doesn't exist
    os.makedirs(download_path, exist_ok=True)

    # Download the dataset
    download_kaggle_dataset(dataset_name, download_path)
    
    # Find the downloaded zip file
    downloaded_zip_file = find_zip_file(download_path)
    
    if downloaded_zip_file:
        unzip_file(downloaded_zip_file, download_path)
    else:
        print(f"No zip file found in {download_path}.")