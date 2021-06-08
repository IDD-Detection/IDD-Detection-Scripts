# IDD-Detection-Scripts

This repository is basically focussed to improve the experience of all users of the IDD Dataset.

We highly encourage you to first have a look at the dataset as well as gain more information on it. 
This can be done by visiting it's website : https://idd.insaan.iiit.ac.in/ 

### Minor Flaw :

Each xml file has a foldername tag which consists of either Left or Right towards it's end. This basically denotes a left view and a right view of the same image.
This can also be verified if you visit the Images Folder and notice the imagenames. It basically contains 2 kinds of imagenames : one is just a number and other type is number with 'r' towards the end. 

Therefore, in xml file also the imagename should end with 'r'. However, if observed carefully, you will find out that none of the xml files contain imagename with 'r'. Hence, if you are extracting images just based on imagename, you will get incorrect results.

Hence, in order to resolve this, you can use the xml filename directly for extracting the images. 

Kindly refer to the script : 
[xml-images-selector.py](https://github.com/IDD-Detection/IDD-Detection-Scripts/blob/main/xml-images-selector.py)

### Utility Scripts :

1) Selection of only those xml files which contain a specific class : [xml-class-selector.py](https://github.com/IDD-Detection/IDD-Detection-Scripts/blob/main/xml-class-selector.py) 
2) Deletion of class tags from xml file which you may not require for your project : [xml-tag-remover.py](https://github.com/IDD-Detection/IDD-Detection-Scripts/blob/main/xml-tag-remover.py)
3) Selection of class tags based on size of bounding boxes : [xml-bb-checker.py](https://github.com/IDD-Detection/IDD-Detection-Scripts/blob/main/xml-bb-checker.py)
4) Deletion of bounding boxes of a particular class based on size : [xml-bb-checker-remover.py](https://github.com/IDD-Detection/IDD-Detection-Scripts/blob/main/xml-bb-checker-remover.py)


