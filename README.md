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
