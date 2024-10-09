import os

def list_directory_contents(path):
    try:
        # Check if the provided path is a directory
        if os.path.isdir(path):
            print(f"Contents of directory '{path}':")
            for root, dirs, files in os.walk(path):
                for name in dirs:
                    print(f"Directory: {os.path.join(root, name)}")
                for name in files:
                    print(f"File: {os.path.join(root, name)}")
        else:
            print(f"The path '{path}' is not a valid directory.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Prompt the user for the directory path
    directory_path = input("Enter the directory path: ")
    list_directory_contents(directory_path)