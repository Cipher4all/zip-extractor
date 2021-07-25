import zipfile, os
from pathlib import Path
file = input('Enter the zip file name:')
filename = zipfile.ZipFile(file, 'r')
filename.extractall('C:\\Users\\abhis\\OneDrive\\Desktop\\Python\color_detection')
filename.close()
