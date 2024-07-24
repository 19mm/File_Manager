# Python File Manager

## Overview
"Python File Manager" is a Python script designed to organize files in a directory into specific folders based on their file extensions. This script will create folders for images, documents, media files, applications, and other files, and then move the files to their respective folders. It uses the `colorama` library to enhance the terminal output with colors, making the process more visually appealing.

## Features
- Automatically creates folders if they do not exist.
- Moves files into the respective folders based on their file extensions.
- Provides real-time feedback with colored terminal output.
- Introduces a delay between moving files for better visualization.

## How It Works
- The script lists all files in the current directory.
- It categorizes the files into:
      Images (.png, .jpg, .jpeg)
      Documents (.docx, .doc, .pdf, .txt)
      Media (.mp4, .mp3, .flv)
      Applications (.exe)
      Others (files that do not fit into the above categories)
- It creates folders for each category if they do not already exist.
- It moves the files into their respective folders and prints the progress in the terminal.

## Usage
- Clone this repository or download the script "main.py"
- Place the "main.py" script in the directory you want to organize.
  Run the script: python main.py
