import os

def list_directory_contents(path):
    for root, dirs, files in os.walk(path):
        print(f"Directory: {root}")
        for dir_name in dirs:
            print(f"  Subdirectory: {os.path.join(root, dir_name)}")
        for file_name in files:
            print(f"  File: {os.path.join(root, file_name)}")

# Main directory
path = "https://6705d510ccb9cc8cdd97ce15--fancy-phoenix-90386a.netlify.app/"

# Subdirectories
subdir = "https://6705d510ccb9cc8cdd97ce15--fancy-phoenix-90386a.netlify.app/about"
subdir1 = "https://6705d510ccb9cc8cdd97ce15--fancy-phoenix-90386a.netlify.app/contact"

# Print main directory and subdirectories
print(f"Main Directory: {path}")
print(f"Subdirectory 1: {subdir}")
print(f"Subdirectory 2: {subdir1}")

# List contents of the main directory
list_directory_contents(path)