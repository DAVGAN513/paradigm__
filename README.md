# paradigm__

# Context
In this days computer usage directories like downloads folder often become messy with hundreds of mixed files like images, documents or others things, organazing these files manually creating folders, selecting files and dragging them to their respective locations is very repetitive and time consuming task, for this evidence we will tackle the problem of file organization automation the goal for this is to build a computational solution that takes a disorganized directory and automatically sorts evry file into a specific sub folder based on their file extentions it can be .pdf, .jpg and .png

# Model
The scripting paradigm is the perfect fit for this problem because of this scripting is disegned to automate system level tasks and tie different existing components together without the need for heavy software architecture
Unlike object oriented programming that requires defining classses and objects or parallel programming that deals with thread management for heavy CPU tasks, a script executes sequentially to top to down 
The model follows a straightforward logic:
- Enviroment Setup we need to read the target directory
- State definition we need to define a dictionary mapping file extensions to their target folder names
- Sequential execution for this the iterate through every file in the directory one by one
- Procedural action we need to check the files extensions create the target folder if it does not exist and move the file
This model is light relies heavily on native input/output system libraries and executes exactly as a human would do it manually but in a fraction of a second

# Implementation 
In order to solve this problem we will to create a python script in which we can take a discorganized target directory and output a neatly organized folder structure for this code we will use the scripting paradigm to execute a sequential procedural workflow to automate the file moving process

- Module Import:

```python
import os
import shutil
```
This section imports the os module for interacting with the operating system and reading directories and the shutil module for high level file operations like moving files drom one place to another 

- Function organize_folder(target_directory):

```python
def organize_folder(target_directory):
    file_types = {
        "Images": ['.jpg', '.jpeg', '.png', '.gif'],
        "Documents": ['.pdf', '.docx', '.txt', '.xlsx'],
        "Videos": ['.mp4', '.mkv', '.mov']
    }
```
This function takes an input string trget_directory representing the path to clean up´, inside a directory file_types is initialized to map the desired target folder names to their corresponding list of file extensions

- Directory Validation and Reading:

```python
if not os.path.exists(target_directory):
    print("Directory does not exist.")
    return
```
This part verifies if the provided actually exists in the computer if it does it uses os.listdir to create a list named files containing the names of all the files and folders present inside thar target directory 

- Procedural Loop and Extnsion Extraction:

```python
for file in files:
    file_path = os.path.join(target_directory, file)
    
    if os.path.isdir(file_path):
        continue
        
    _, extension = os.path.splitext(file)
    extension = extension.lower()
```
The code loops through every item in the directory sequentially, it checks if the item is a folder and skips it if true, then it uses os.path.splitext to separate the file name from its extension, converting the extension to lowercase for an accurate comparison

- Folder Creation and File Moving:

```python
for folder_name, extensions_list in file_types.items():
    if extension in extensions_list:
        folder_path = os.path.join(target_directory, folder_name)
        
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        
        destination_path = os.path.join(folder_path, file)
        shutil.move(file_path, destination_path)
        print(f"Moved: {file} -> {folder_name}/")
        break
```
This nested loop checks if the files extention exists in our file_types dictionary, if a match is found it evaluates if the target folder exists if not it creates it using os.makedirs, finally it uses shutil.move to transfer the file to its new location and breaks the loop to proceed to the next file 

- Script Execution Block:

```python
if __name__ == "__main__":
    path_to_organize = "./my_messy_folder"
    organize_folder(path_to_organize)
```
This block ensures that the script runs automatically when executed from the terminal, defending the specific directory to be organized and calling the main function

# Testing 

To test this script ypu dont need a complex testing environment or web server, simply execute the script in th eterminal:
- Initial State:
  - report.pdf
  - vacation.jpg
  - budget.xlsx
  - meme.png
  - presentation.mp4
 
```text
Starting batch organization...
Moved: report.pdf -> Documents/
Moved: vacation.jpg -> Images/
Moved: budget.xlsx -> Documents/
Moved: meme.png -> Images/
Moved: presentation.mp4 -> Videos/
Script finished successfully!
```
- Final State:

The files are now messy placed inside the newly created documents, images and videos that have subdirectories, the script successfully automated a manual workflow

# Complexity Analysis

