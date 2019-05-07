# Asciimator
Turn a video into frames and txt files from each frame.

Dependecies:
OpenCV

genAsciiFromMovie.py
--------------------------
This script generates a folder with frames and txt files from these frames.
It can be used with anything that OpenCV supports. It has been tested with .gif, .mp4, .avi;
It takes a --movie argument to select which file you want to transform.

playAscii.py
--------------------------
This script "plays" what you have already distilled from your movie.
It takes a --folder argument and it looks only for the .txt files.
