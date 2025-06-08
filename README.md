# MoonfallAnimated

## Overview
This is a Rainmeter skin that animates a computer background, 
while also updating with the time of day. To minimize latency, 
it calls a python script once an hour to construct the queue of 
backgrounds for that hour. Then a lua script in conjunction with 
Rainmeter is used to update and animate the background.

## Setup
As Rainmeter is required to run this program, if you are not on a Windows 
device or some other device that can run Rainmeter, you will not be able
to use this program.
Both python and the Rainmeter application are required for this 
program to run. If you don't have one or both of them installed, 
you can download python at [python.org](https://www.python.org/downloads/) 
and Rainmeter at [rainmeter.net](https://www.rainmeter.net).

Once you have both Rainmeter and python installed, you will need to
download and run the MoonfallAnimated_1.0.rmskin file in this repository. 
This will open up the Rainmeter Skin Installer where you should follow the
steps to install this skin.

There is only one modification you will need to make before the program
is ready to run. Navigate to the WallpaperController.ini file and open it 
in the text editor of your choosing. In the section marked "[PythonRunner]"
update the file path to the path to your installed instance of python.exe.
Then load the WallpaperController file to test that everything is working.
If your background shows an animated pixel art wallpaper, you have completed
the setup.

## Customization 
I created this library specifically to allow for a wide range of 
customization. The first level of customization is simply replacing the
default background animation with your own 4-frame animations. To do this,
navigate to Wallpaper/Resources. In this folder you will find 24 folders, 
labeled by hour 0 to 23. To edit the frames for a specific hour, replace 
the image files in that folder with new images, making sure to rename the
new images to 1, 2, 3, and 4 in order.

For further customization to the number of frames in an hour or how they
are displayed, you will need to use the AniControlJsonGenerator.py script 
in the Wallpaper folder. First, move your image files into the appropriate
folder. Then move the AniControlJsonGenerator.py file into the same folder
and run it. This will help you set up that folder to function properly.

You can also add other folders into the hour folders. Make sure to set
them up properly with AniControlJsonGenerator.py as well.

## Disclaimer
Generative was used to assist me in the creation of this program. However,
this was largely for technical issues and bug fixing. All the algorithms
and core concepts were designed by me.

If you use this code as a base or in any way in any published projects, 
please link to this repo to give me credit. Thanks!