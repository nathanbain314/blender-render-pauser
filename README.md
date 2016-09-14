# blender-render-pauser
This is a script that allows you to stop blender renders, save the result, and later continue the render
#Use
Open up a terminal and run 

**blender -b file.blend -P pause.py**

When you are done abort the process by pressing control-c. The program will then ask the last tile worked on. Type in the number of the tile that is shown on the terminal. A file named *data.csv* will then be saved with some metadata and a file named *out.png* will be saved that contains the progress so far. To start up the render again just run the same command and quit in the same way. This will create *rows.png* with the new render progress. Combine these two files to *out.png* by running the command

**blender -b -P combine.py**

