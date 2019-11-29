# ConvertingColorToGrayscale
Converting color to grayscale with Python

If you want to simply covert color to grayscale in a single file, use the following code from [gray_single.py](https://github.com/elibooklover/ConvertingColorToGrayscale/blob/master/gray_single.py):

```
import cv2

directory1 = r'resized/' # Source Folder
directory2 = r'gray/' # Destination Folder

image = cv2.imread(directory1+'image1.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imwrite(directory2+'image1_gray.png', gray)

cv2.waitKey(0)
cv2.destroyAllWindows()

```

If you want to covert color to grayscale in multiple files, use the following code from [gray_multiple.py](https://github.com/elibooklover/ConvertingColorToGrayscale/blob/master/gray_multiple.py):

```
import cv2
import os,glob
from os import listdir,makedirs
from os.path import isfile,join

path = 'resized/' # Source Folder
dstpath = 'gray/' # Destination Folder

try:
    makedirs(dstpath)
except:
    print ("The directory already exists, so the images will be written in the same folder")

files = [f for f in listdir(path) if isfile(join(path,f))]

for image in files:
    try:
        img = cv2.imread(os.path.join(path,image))
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        dstPath = join(dstpath,image)
        cv2.imwrite(dstPath,gray)
    except:
        print ("{} is not converted".format(image))

for fil in glob.glob("*.png"):
    try:
        image = cv2.imread(fil)
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(os.path.join(dstpath,fil),gray_image)
    except:
        print('{} is not converted')
```

![Color](https://github.com/elibooklover/ConvertingColorToGrayscale/blob/master/image1.jpg)
![Gray](https://github.com/elibooklover/ConvertingColorToGrayscale/blob/master/image1_gray.jpg)
