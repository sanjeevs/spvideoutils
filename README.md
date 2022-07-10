# Overview
Utilities to handle video from camera. Contains various utilites that crop and split the video files.

# Installation
In your virtual env do
```
$ pip install spvideoutils
```

# Scripts
The following scripts are provided by the package.
* video_capture.py
  * Captures a video from a camera to mp4 file on disk.
* video_split.py
  * Splits a mp4 file into frames stored as png file on output dir.
* video_merge.py
  * Merges the frames in png file from dir to a video file.
* video_crop.py
  * Crops a video file from frame number i to j.

# Developing VideoUtils
This involves 
* Creating a python virtual env.
* Downloading the source code from [GitHub](https://github.com/sanjeevs/spvideoutils)
* Installing all the dependencies
* Installing the package in dev mode.

For example these are steps I typically do on my windows machine.
```commandline
python -m venv venv_dev_spvideoutils  
env_spvideoutils\Scripts\activate
git clone https://github.com/sanjeevs/spvideoutils.git
cd spvideoutils
pip install -r requirements.txt
pip install -e . 
```
I can check that the env is correctly setup by invoking any of the scripts above from the same window.
```commandline
>video_capture
usage: video_capture [-h] [--index INDEX] [--time TIME] outfile
video_capture: error: the following arguments are required: outfile

```

# Creating a distribution package
Check the resource [packaging.python.org](http://packaging.python.org) on  how to build the
distribution. Since this is a pure python project, I need to just build the bdist_wheel distribution.

* Bump the version of the software in setup.py
* 
* Run the script to create the distribution in a new folder called *dist*.
```commandline
python setup.py bist_wheel
```
* Use twine to upload the source distribution. This will ask for username and password. 

>**_NOTE:_** My pypi username is my git hub username and the password is the same (common).

```commandline
twine upload dist/*
```
