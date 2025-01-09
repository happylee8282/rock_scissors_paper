import os
import shutil

def separate_images_and_labels(dataset_dir):
    # Paths for the new directories
    images_dir = os.path.join(dataset_dir, "images")
    labels_dir = os.path.join(dataset_dir, "labels")
    
    # Create the new directories if they don't exist
    os.makedirs(images_dir, exist_ok=True)
    os.makedirs(labels_dir, exist_ok=True)

    # Move files into the respective directories
    for file in os.listdir(dataset_dir):
        file_path = os.path.join(dataset_dir, file)
        if file.endswith(".jpg"):
            shutil.move(file_path, os.path.join(images_dir, file))
        elif file.endswith(".txt"):
            shutil.move(file_path, os.path.join(labels_dir, file))
    
    print(f"Finished separating images and labels in {dataset_dir}.")

# Path to the dataset directory
dataset_directory = "/home/happy/Desktop/rocky/project_me/test"  h

# Run the separation
separate_images_and_labels(dataset_directory)
