import os
import shutil

def organize_folder(target_directory):
    if not os.path.exists(target_directory):
        print(f"Failed to find '{target_directory}'")
        print("Check the path and try again")
        return

    # read the files in the target directory
    files = os.listdir(target_directory)
    print(f"Starting organization in: {target_directory}\n")
    
    for file in files:
        file_path = os.path.join(target_directory, file)
        
        # if theres a directory, we skip it
        if os.path.isdir(file_path):
            continue
            
        # Get the file extension
        _, extension = os.path.splitext(file)
        
        # if the file has no extension, we skip it
        if not extension:
            continue
            
        # remove the dot and convert to uppercase to get the folder name
        folder_name = extension.replace(".", "").upper()
        
        # Create the folder if it doesn't exist
        folder_path = os.path.join(target_directory, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        
        # Move the file to the corresponding folder
        destination_path = os.path.join(folder_path, file)
        shutil.move(file_path, destination_path)
        
        print(f"Move: {file} -> Folder {folder_name}/")

if __name__ == "__main__":
    # The correct path to the folder you want to organize
    path_to_organize = r"C:\Users\Antonio\OneDrive\messy_" 
    
    organize_folder(path_to_organize)
    print("Organization finished!")