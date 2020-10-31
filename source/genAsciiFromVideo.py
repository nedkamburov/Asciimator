from genAscii import * 
from movieToJPGs import *
import glob
import os
import re
from natsort import natsorted
    
def getDigits(s):
    s = re.findall(r'\d+', s)
    num = int(s[0])
    return ("%03d" % num)

 ########### Convert each image in a folder to a text file #########
 
def fromImageToTxt(allFiles, cols):
    
    for fileName in allFiles:

        aimg = convertImageToAscii(fileName, cols, 0.48, True)

        outputFile = os.path.basename(fileName)
        outputFile = getDigits(outputFile)
        
        outFile = f"data/myasciiart_{outputFile}.txt"
        # open file
        f = open(outFile, 'w')

        # write to file
        for row in aimg:
        	f.write(row + '\n')
	
        print ("Converting frame " + outputFile)
            # cleanup
        f.close()
        print("ASCII art written to %s" % outFile)
        
 ########### Parser #########
def main():
    descriptionText = "This program JPGs to textfiles"

    parser = argparse.ArgumentParser(description=descriptionText)
    parser.add_argument("--movie", dest="movie", required=True)
    parser.add_argument("--cols", dest="cols", required=False)

    args = parser.parse_args()

    movieFile = args.movie
    
    if args.cols:
        cols = int(args.cols)
    else:
        cols = 80
        
    convertMovieToImages(movieFile)
    
    directory = "data"
    
    allFiles = natsorted(glob.glob(f'{directory}/*.*'))
    fromImageToTxt(allFiles, cols)
    print("")
    print("🎉🎉🎉🎉 All done. 🎉🎉🎉🎉🎉🎉")
       
if __name__=='__main__':
    main()
    


