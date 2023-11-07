import os
import time
import mimetypes

def list_file_types(directory_path):
    if not os.path.exists(directory_path) or not os.path.isdir(directory_path):
        print("Error: Directory does not exist or is not a valid directory.")
        return

    file_types = set()

    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            mime_type, _ = mimetypes.guess_type(file_path)
            if mime_type:
                file_type = mime_type.split('/')[0]  # Extract the top-level file type
                file_types.add(file_type)

    return file_types

while True:
    folder_path = input("Enter a path: ")

    if os.path.exists(folder_path):
        print(f"Folder '{folder_path}' exists.")
        break  # Exit the loop if a valid folder path is provided
    else:
        print("Error, Folder Not Found. Please enter a valid folder path.")

time.sleep(2)  # Pause for 2 seconds
print(f"Folder '{folder_path}' Scanning....")
file_types = list_file_types(folder_path)

if file_types:
    print("File types found in the directory:")
    for file_type in file_types:
        print(file_type)
else:
    print("No files found in the directory.")


