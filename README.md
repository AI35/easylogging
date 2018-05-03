# Pylog
###### Simple and Easy Logger lib for python

[![Pylog](https://img.shields.io/badge/build-passing-brightgreen.svg)]()
[![version](https://img.shields.io/badge/version-1.1.1-green.svg)]()
[![status](https://img.shields.io/badge/status-Beta-yellowgreen.svg)]()
[![python](https://img.shields.io/badge/python-3-blue.svg)](http://www.python.org/download/)
[![windows](https://img.shields.io/badge/windows-tested-brightgreen.svg)]()
[![linux](https://img.shields.io/badge/linux-tested-brightgreen.svg)]()
[![license](https://img.shields.io/badge/license-GNU-blue.svg)](https://github.com/AI35/Python-Service/blob/master/LICENSE)

## REQUIREMENTS
- Python-3 --> http://www.python.org/download/

## Notes
- This is beta version.
- **Important(To Work --logfile)** : You need to put Pylog.py in same folder with your main file.
- Maybe later I'm thinking of adding more features.
- I am created this lib because i want use easy logging lib.

## Installation

- Clone this repo:
	
	```
	$ git clone https://github.com/AI35/Pylog
	```

## Usage
- First you need import lib for your file and Set name :
  ```
    import Pylog
    
    Pylog.logname('Filename.py')
  ```
- Use the functions you need:
  - Pylog.critical(msg)
  - Pylog.error(msg, exc_info) **default: exc_info=False**
  - Pylog.warning(msg) **or** Pylog.warn(msg)
  - Pylog.info(msg)
  - Pylog.debug(msg)
- You can start logging from Cmd or PowerShell :
  ```
    $ Python yourfile.py --logging --logfile
    
    usage: youefile.py [--logging] [--logfile]
    
    optional arguments:
      --logging            Display log in Console
      --logfile            Create log file
  ```
- After first run you will see new file **logging.conf** :
  - Change **level** number to display log in console **without** --logging (0 display all level).
  	```
  	  level=50
  	```
  - Change **file_level** number to set level in log file **with** --logfile (50 hide all level).
  	```
   	  file_level=0
  	```
  - **in Version 1.1.0** : Now you can show and hide error info from **logging.conf** :
  	###### - Show Error info (Pylog.error(msg, exc_info))
	###### - True or False or None
	###### - * (None) means that exc_info takes the value entered from the user, example: Pylog.error(msg, exc_info=True)
  	```
  	  exc_info=None
  	```
- Level table :

    | Level  | Numeric value |
    | ------------- | ------------- |
    | CRITICAL  | 50  |
    | ERROR  | 40  |
    | WARNING  | 30  |
    | INFO  | 20  |
    | DEBUG  | 10  |
    | NOTSET  | 0  |
    
- You can see test file **test.py** to know how this lib is work.


  
## LICENSE
```
Copyright 2018 LinePY - AI35, Inc.

Pylog

   Licensed under the GNU License , you may not use this
   file except in compliance with the License.
   You may obtain a copy of the License at :

   https://github.com/AI35/Pylog/blob/master/LICENSE
```
###### ALI .B .OTH - ORG : LinePY �
