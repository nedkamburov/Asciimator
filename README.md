# ASCIImator

Turn a video into frames then each frame to ASCII txt file.

Dependecies:
OpenCV, numpy, PIL

![Showcase of the asciimator in practice](asciimator-demo.gif)

### How to use
*Install dependancies*

`pip install opencv-python numpy pillow`

*Distill video frames from --movie nameOfMovie.mp4. Optionally you can specify with--cols how many columns to generate the ASCII. Default is 80.*

`python genAsciiFromMovie.py --movie nameOfMovie.mp4`

*Play the ASCII animation with txt files from a folder. The default is 'data'*

`python playAscii.py --folder data`

#### genAsciiFromMovie.py

This script generates a folder with frames and txt files from these frames.
It can be used with anything that OpenCV supports. It has been tested with .gif, .mp4, .avi.

The --movie argument selects which file you want to transform.

The --cols argument selects how many columns to generate the ascii text files in.

#### playAscii.py

This script 'plays' what you have already distilled from your movie.

The --folder argument specifies from which folder to play the animation 

