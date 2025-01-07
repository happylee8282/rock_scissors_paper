import os
import shutil
from random import shuffle

def split_data_by_ratio(source_dir, dest_dir, train_ratio=0.6, test_ratio=0.2, valid_ratio=0.2):
    """
    Splits data from source directory into train, test, and valid directories based on ratios.

    Parameters:
    source_dir (str): Path to the source directory containing .jpg and .txt files.
    dest_dir (str): Path to the destination directory to save split data.
    train_ratio (float): Ratio of files for the training set.
    test_ratio (float): Ratio of files for the test set.
    valid_ratio (float): Ratio of files for the validation set.
    """
    # Create destination directories
    train_dir = os.path.join(dest_dir, "train")
    test_dir = os.path.join(dest_dir, "test")
    valid_dir = os.path.join(dest_dir, "valid")
    
    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(test_dir, exist_ok=True)
    os.makedirs(valid_dir, exist_ok=True)
    
    # Collect all .jpg and .txt pairs
    files = [f for f in os.listdir(source_dir) if f.endswith('.jpg')]
    pairs = [(f, f.replace('.jpg', '.txt')) for f in files if os.path.exists(os.path.join(source_dir, f.replace('.jpg', '.txt')))]
    
    # Shuffle files to randomize data splitting
    shuffle(pairs)
    
    total_files = len(pairs)
    
    # Calculate counts based on ratios
    train_count = int(total_files * train_ratio)
    test_count = int(total_files * test_ratio)
    valid_count = total_files - train_count - test_count
    
    # Split data
    train_files = pairs[:train_count]
    test_files = pairs[train_count:train_count + test_count]
    valid_files = pairs[train_count + test_count:]
    
    # Helper function to move files
    def move_files(file_list, target_dir):
        for img, txt in file_list:
            shutil.move(os.path.join(source_dir, img), os.path.join(target_dir, img))
            shutil.move(os.path.join(source_dir, txt), os.path.join(target_dir, txt))
    
    # Move files to corresponding directories
    move_files(train_files, train_dir)
    move_files(test_files, test_dir)
    move_files(valid_files, valid_dir)
    
    print(f"Data successfully split and moved to {dest_dir}.")
    print(f"Train files: {len(train_files)}, Test files: {len(test_files)}, Validation files: {len(valid_files)}.")

# Parameters for the script
source_directory = "/path/to/your/source/folder"  # Replace with your source directory path
destination_directory = "/path/to/your/destination/folder"  # Replace with your destination directory path
train_ratio = 0.6  # 60% of the data for training
test_ratio = 0.2   # 20% of the data for testing
valid_ratio = 0.2  # 20% of the data for validation

# Run the function
split_data_by_ratio(source_directory, destination_directory, train_ratio, test_ratio, valid_ratio)
