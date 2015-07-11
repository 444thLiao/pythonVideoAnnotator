# Python Video Annotator

The software is a standalone application written in python, which intend to provide a GUI for users to take notes of events occurred in the videos.

[![Video](/docs/video.png)](https://www.youtube.com/watch?v=IE_mtCHc9bQ)


### Developers

* Ricardo Ribeiro - collaborator of the [Scientific Software Platform](http://neuro.fchampalimaud.org/en/research/platforms/staff/Scientific%20Software/) of the [Champalimaud Foundation](http://fchampalimaud.org).
* Hugo Cachitas working - collaborator of the [Innate Behavior Lab](http://neuro.fchampalimaud.org/en/research/investigators/research-groups/group/Vasconcelos/) of the [Champalimaud Foundation](http://fchampalimaud.org).


![Video annotator screenshot](/docs/screencapture.png?raw=true "Screen")

## Installation & Running

The application was developed and tested with Ubuntu 12.04 and 14.

### Dependencies

* Python 2.7
* PyQt4: ```sudo apt-get install pyqt4-dev-tools python-qt4 python-qt4-gl```
* Numpy: ```sudo apt-get install python-numpy```
* PyOpenGL: ```sudo pip install pyopengl```
* Python OpenCV: ```sudo apt-get install python-opencv```
* Scipy: ```sudo apt-get install python-scipy```
* PyForms: ```sudo pip install git+git://github.com/UmSenhorQualquer/pyforms.git```

### Run

From the Terminal run:

```
python VideoAnnotationEditor.py
```


### Collaboration

This project was initially developed in collaboration with the [Innate Behavior Lab](http://neuro.fchampalimaud.org/en/research/investigators/research-groups/group/Vasconcelos/) to correct the result of a Computer Vision software to track flies in an arena