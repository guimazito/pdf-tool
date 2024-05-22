# -*- coding: utf-8 -*-

import os
import shutil
import subprocess

VER = '1.0.0'
TOOL_NAME = 'Pdf_Tool_{}'.format(VER)
PATH = os.path.dirname(os.path.abspath(__file__))
MAIN_FILE = 'main.py'
PYTHON_PATH = r'C:\Users\claudio\AppData\Local\Programs\Python\Python311-32\Lib\site-packages'

with open(MAIN_FILE, 'r') as f:
    data = f.read()

with open(MAIN_FILE, 'w') as f:
    f.write(data.replace('{VERSION}', VER))

# Generate EXE
subprocess.call(['pyinstaller', '--path', PYTHON_PATH,'--hidden-import', 'win32timezone', '--onefile', os.path.join(MAIN_FILE)])

with open(os.path.join(MAIN_FILE), 'w') as f:
    f.write(data.replace(VER, '{VERSION}'))

shutil.copytree(os.path.join(PATH, 'files'), os.path.join(PATH, 'dist', 'files'))

# Removing unecessary folders and files
os.remove(os.path.join(PATH, MAIN_FILE.replace('py', 'spec')))
shutil.rmtree(os.path.join(PATH, 'build'))

# Renaming exe folder
os.rename(os.path.join(PATH, 'dist'), os.path.join(PATH, TOOL_NAME))
os.rename(os.path.join(PATH, TOOL_NAME, 'main.exe'), os.path.join(PATH, TOOL_NAME, '{}.exe'.format(TOOL_NAME)))