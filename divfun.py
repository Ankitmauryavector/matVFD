import os
import re

import cv2

def sorted_nicely(l):
    """ Sorts the given iterable in the way that is expected.

    Required arguments:
    l -- The iterable to be sorted.

    """
    convert = lambda text: int(text) if text.isdigit() else text
    alphanum_key = lambda key: [convert(c) for c in re.split("([0-9]+)", key)]
    return sorted(l, key=alphanum_key)


def Function_new(path):
    if not os.path.exists('8x8'):
                    os.makedirs('8x8')
    
    for filename in sorted_nicely(os.listdir(path)):

        nRows = 8

        mCols = 8
        pathn = path + filename
        img = cv2.imread(pathn)
        sizeX = img.shape[1]
        sizeY = img.shape[0]
        newname = filename[-5::-1][::-1]
        for i in range(0, nRows):
            for j in range(0, mCols):
                roi = img[i * sizeY // nRows:i * sizeY // nRows + sizeY // nRows,
                      j * sizeX // mCols:j * sizeX // mCols + sizeX // mCols]
                os.system('cd 8x8')
                if not os.path.exists(f'EightXEight{str(i)+str(j)}'):
                    os.makedirs(f'EightXEight{str(i)+str(j)}')
                cv2.imwrite(f'EightXEight{str(i)+str(j)}/{newname}' + ".jpg", roi)

if __name__ == '__main__':
    # Calling the function
    Functiond("C:/Users/ankit/OneDrive/Desktop/")
