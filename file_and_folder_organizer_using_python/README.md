# File Organizer For Your Computer
This is a simple python script that organizes files in a directory into folders based on their file extension. The script is written in Python 3.12.1 and should work on all versions of Python 3.x.

## How to use
1. Clone or Download this repository.
2. Open and navigate to the directory where you have cloned or downloaded this repository.
3. Run the file `main.py`.
4. Enter the path of the directory you want to organize.

script will organize the files in the directory into folders based on their file extension.
It contains mainly 5 folders:
1. **files** - to store the files like .pdf, .doc, .txt, etc.
2. **images** - to store the images like .jpg, .jpeg, .png, etc.
3. **videos** - to store the videos like .mp4, .mkv, .avi, etc.
4. **audios** - to store the audio files like .mp3, .wav, etc.
5. **others** - to store the files which are not in the above categories like .zip, other that are not given in the extention tuple.

## Note
- The script will not organize the files in the subdirectories of the given directory.
- and it will only organize the files in the given directory, not the directory in given directory.
- The script will not delete any files, it will only move the files to the respective folders.
- The script will not organize the files in the folders that are already present in the given directory.