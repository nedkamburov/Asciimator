import time
import argparse
import glob
import os
from natsort import natsorted


def animate(sourceFolder):
    allFiles = natsorted(glob.glob(f'{sourceFolder}/*.txt'))
    filenameTemplate = f"{sourceFolder}/myasciiart_%03d.txt"
    for j in range(4):
        for i in range(len(allFiles)-1):
            filename = filenameTemplate % i
            # print(filename)
            with open(filename) as f:
                data = f.read()
                print(chr(27) + "[2J")
                print(data)
                time.sleep(0.1)
                
def main():
    parser = argparse.ArgumentParser("Animate a sequence of ASCII text files")
    parser.add_argument("--folder", dest="folder", required=True)
    
    args = parser.parse_args()
    folder = args.folder
    
    # print(folder)
    animate(folder)
    print("Fin.")
    
if __name__ == "__main__":
	main()
