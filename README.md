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

To validate the scripting paradigm implementation a functional test was conducted on a local directory named messy_ the test was designed to evaluate the scripts ability to dynamically identify file extensions generate appropriate directories, and relocate the files automatically 

- Initial State
This is the before of all, the target directory contains a mix of unorganized files a word document, an excel spreadsheet, and two pdf files
<img width="1920" height="1080" alt="Captura de pantalla 2026-06-06 155252" src="https://github.com/user-attachments/assets/1e987294-81b2-4a23-8efe-4cd764ca1518" />













The execution phase is that python script was execute using the VScode integrate terminal the console output successfully traced the automation process, confirming that the script evaluated each file extracted its specific extension and routed it to a newly designated folder
<img width="1863" height="278" alt="Captura de pantalla 2026-06-07 145222" src="https://github.com/user-attachments/assets/6d26774a-305d-4b6f-baae-e63d3467f1a1" />


- Final State
The after of this execution is that the script successfully created the exact uppercase directories correspinding to the file extension present in the root folder: DOCX, PDF and XLSX all files were accurately sorted into their respective folders validating the efficiency and accuracy of the automation script
<img width="1902" height="607" alt="image" src="https://github.com/user-attachments/assets/bf28257c-43ea-47cc-90a4-364658e3762a" />



# Complexity Analysis

The simplicity of the scripting paradigm also reflects in its computational complexity 

- Time Complexity
  O(N) the algorithm iterates exactly once through the n files that present in the directory, for each file the operation performed on the extracting of the file extension, formatting the string and checking if the destination folder exists creating it if it neccessary and moving the file are all of this in constant time operations, o(n) scaling directly with the total number of files in the directory
  
- Space Complexity
  O(1) the script only stores a few strings in memory regardless of how large the actual files are, it doesny load files into RAM to move them meaning the momory footprint remains constant and extremely low


# Other implementation
Another way to solve this file organization problem would be through using C++ instead of python 
for c++ the main differences would be in the way we interact with os file system using th efilesystem library. 
In python the interation is handled dynamically using the os module, and strings are sliced natively with built in methods 

```python
files = os.listdir(target_directory)

for file in files:
    if os.path.isdir(os.path.join(target_directory, file)):
        continue

    _, extension = os.path.splitext(file)
    folder_name = extension.replace(".", "").upper()
```

C++ uses the std::filesystem namespace wich requires explicit type of checking and manual transformation loops to archieve uppercase formating

```cpp
#include <filesystem>
#include <algorithm>
#include <string>

namespace fs = std::filesystem;

for (const auto& entry : fs::directory_iterator(target_directory)) {
    if (entry.is_regular_file()) {
        std::string ext = entry.path().extension().string();

        if (!ext.empty()) {
            ext.erase(0, 1); // Removes the "." from ".pdf"
            std::transform(ext.begin(), ext.end(), ext.begin(), ::toupper);
        }
    }
}
```

Creating folders and moving files in python usues the high level functions from the shutil and os modules to manage directories and recolate files 

```python
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

destination_path = os.path.join(folder_path, file)
shutil.move(file_path, destination_path)
```

C++ uses filesystem methods like create_directory and relies on reneme to change teh files path that with that effectively moves it

```cpp
fs::path target_folder = target_directory / ext;

if (!fs::exists(target_folder)) {
    fs::create_directory(target_folder);
}

// Moving the file by renaming its absolute path
fs::rename(entry.path(), target_folder / entry.path().filename());
```

Both python and c++ have an O(n) time complexity in their algorith where the n represents the number of files inside the folder of the directory, as both programs must iterate through every item exactly once, because of this the simplicity, of the scripting paradigm python offers us a more direct solution that runs more intuitive across any os without compilation, while c++ couls potencially execute the file movement faster, it requires a more complex setup for that is better to use the python script that is more optimal and nature fit for automated os tasks 




# Refences

GeeksforGeeks. (2026, June 3). Introduction of programming paradigms. GeeksforGeeks. https://www.geeksforgeeks.org/system-design/introduction-of-programming-paradigms/
Važan, R., & Važan, R. (2023, August 6). Scripting as a programming paradigm. Robert’s blog. https://blog.machinezoo.com/Scripting_as_a_programming_paradigm
Codecademy. (n.d.). How to build a Python Script: A Beginner’s guide to Python Scripting. Codecademy. https://www.codecademy.com/article/python-scripting
