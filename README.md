# Image to Header File Converter for Arduino

This project provides a simple tool to convert images into C/C++ header files that can be used with Arduino.\
The generated header file contains the image data in a format suitable for rendering on displays such as OLED, TFT, or other graphical LCDs.

## Features
- Converts images (e.g., BMP, PNG, JPG) into a C/C++ header file.
- Generates an array of pixel data for easy integration with Arduino projects.
- A Graphic user interface was added for easy use.

## Requirements
- Python 3.x


## Usage

1. Install dependencies:
   Ensure you have Python 3.x or latest. Then, install the required library:
   ```
   pip install pyqt5
   pip install pillow
   ```
   or for a faster method just run the `run.bat` file instead

2. Run:
   After running you can specify the option to customize the output:
   - `Size`: set the screen size of your project.
   - `Output name`: set the name for the header file or output.
   - `Choose format`: set the format colour to use (e.g., `B&W`, `RGB565`, `RGB888`).
