# You Only Look Once
### What this program does:
Thhis task can identify different egyptian coins (0.25, 0.5, 1) through deep learning(YOLO).

### How this program works:
-   We first need to collect a large dataset of pictures of images of egyptian currencies and the images must have a lot of variance.

-   We now use the software `labelImg` to then select the coins from each image.

-   A folder is created with 2 sub folders (`train`, `val`), each with a further 2 subfolders (`images`, `labels`).

-   Our dataset of images is split between `train/images` and `val/images` while the text files resulting from `labelImg` are split between `train/labels` and `val/labels`.

-   We can now upload our split dataset as a zip file to google drive to be further exploited.

-   We can now start a [colab session](https://colab.google/) to train our model using the `YOLO` framework.

-   First, we need to change our session to use the T4 GPU given the computational power that we would need. Then, we have to mount our drive using `from google.colab import drive
drive.mount('/content/drive')` in the first cell.

-   Then we should check for installation of ultralytics using `!pip install ultralytics`.

-   We can now unzip our zip file in colab using `!unzip /filepath/`.

-   We then need to `%cd` into our desired folder so the runs are save on the drive rather than being saved on colab's ram which is volatile. (for eg. `%cd /content/drive/MyDrive/Coins/TheSet`)

-   We also need to make the file through which YOLO can interface with out dataset. This can be done by creating a yaml file and writing in it our val and train paths and also the names of the objects to be identified. For eg.
```
train : /filepath/
val : /filepath

names :
 0 : one
 1 : half
 2 : quarter
```

-   Finally, can start training our model by executing `!yolo task=detect mode=train data=/yaml file path/ epochs=500 imgsz=640`

-   We can aslo adjust epochs to change how accurate our model can be.

-   After the program is done training, we will be left with finished image detection model and some other helpful info

-   If we head into `runs/detect/train/` we will find a file called best.pt. This is our finished product that we can use to detect the coins.

-   There are also some `png` in `runs/detect/` with some info about our model's accuracy, recall, precision, etc.

### How we can use our model:
-   With the `.py` file available you could simply input the model's path and the multimedia's path to then have an image/video with the detected object.