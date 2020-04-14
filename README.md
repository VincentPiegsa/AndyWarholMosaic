# AndyWarholMosaic
App that creates an Andy-Warhol-like mosaic out of an input image

## Installation
Download the <Image_Editor.py> file. Before you start the app, you first need to install the Python (www.python.org) interpreter as well as some additional modules:
1. numpy (python -m pip install numpy)
2. OpenCV (python -m pip install opencv-python)

## Instructions
Navigate to the app directory and start the terminal. Type in:

> python Image_Editor.py <image.jpg> --out=<output.jpg>

The --out statement is optional, however an input file is necessary. If the image is in a different directory, the full path has to be supplied. For example:

> python Image_Editor.py "C:\Desktop\image.jpg" --out="C:\Desktop\output.jpg"

The supported file formats are <.jpg> and <.png>.
