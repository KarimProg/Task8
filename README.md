# Classical View
## What this program does:
This program can identify red and blue balls in images and label their colors.

## How this program works:
-   First, the image is loaded in using opencv and is also resised and some features such as brightness and the percentage presence of the color blue are obtained as this helps identify some properties that can be used to set some parameters to be used in the filtration process. 

![color filtration](doc_imgs\pic4.png)

-   It is then converted to an appropriate colorspace where we can black out objects that are not either red or blue.

![color filtration](doc_imgs\pic.png)

-   The program then passes the image through a series of filters accordingly which include:
    -   Mean filter
    -   Gaussian filter
    -   Adaptive Thresholding
    -   Erosion
    -   Dilation

![color filtration](doc_imgs\pic2.png)

-   The program then passes the image through hough transform to identify the circles, this returns the circles' (x,y) coordinates and radii.

-   The final part of the filtration process is to check if the centers obtained from hough transform actually lie on appropriate colors whether its is red or blue.

-   Finally the circle is printed onto the image along with text to describe the color.

![color filtration](doc_imgs\pic3.png)