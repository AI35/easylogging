# easylogging
###### Simple and Easy Logger lib for python

[![easylogging](https://img.shields.io/badge/build-Stopped-red.svg)]()
[![version](https://img.shields.io/badge/version-1.2.0-green.svg)]()
[![status](https://img.shields.io/badge/status-stable-brightgreen.svg)]()
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/677f082650b54782b947b429dd1c35ce)](https://www.codacy.com/project/alosh.othman55/Pylog/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=AI35/Pylog&amp;utm_campaign=Badge_Grade_Dashboard)
[![python](https://img.shields.io/badge/python-3-blue.svg)](http://www.python.org/download/)
[![windows](https://img.shields.io/badge/windows-tested-brightgreen.svg)]()
[![linux](https://img.shields.io/badge/linux-tested-brightgreen.svg)]()
[![license](https://img.shields.io/badge/license-GNU-blue.svg)](https://github.com/AI35/easylogging/blob/master/LICENSE)
# This library has returned with a new version (easylogging2) --> https://github.com/AI35/easylogging2
- (v1.3 stopped development) This lib is very simple and poor so its need a lot of development and time to become useful in full projects.
- v1.2.5 More stable but will not be Published.
- End : 9 October 2018 , v1.2.0
- This library **may** come back someday better and more useful.
## REQUIREMENTS
- Python-3 --> http://www.python.org/download/

## Notes
- Now This lib is **Stable**.
- I am created this lib because i want use easy logging lib.
- ~~**Important(To Work --logfile)** : You need to put easylogging.py in same folder with your main file.~~
- ~~**Known Bug** : You need to place easylogging.py next to the file that uses this lib.~~

## Installation

- Clone this repo:
	
	```
	$ git clone https://github.com/AI35/easylogging
	```
- Using pip:
	
	```
	$ pip install easylogging
	```

## Usage
- First you need import lib and Set name :
  ```
    import easylogging
    
    easylogging.logname(__file__)
  ```
- Use the functions you need:
  - easylogging.critical(msg)
  - easylogging.error(msg, exc_info) **default: exc_info=False**
  - easylogging.warning(msg)
  - easylogging.info(msg)
  - easylogging.debug(msg)
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
  	###### - This option work on --logfile without use --logging (if use --logging file write all level)
  	```
   	  file_level=0
  	```
 - **in Version 1.1.0** : Now you can show and hide error info from **logging.conf** :
  	###### - Show Error info (easylogging.error(msg, exc_info))
	###### - True or False or None
	###### - * (None) means that exc_info takes the value entered from the user, example: easylogging.error(msg, exc_info=True)
  	```
  	  exc_info=None
  	```
 - **in Version 1.1.2** : Fix DeprecationWarning:
  	###### - Fix warn function
	
 - **in Version 1.1.3** : Fix input msg:
  	###### - You can know input (int or any value) , example:
	```
	  easylogging.error(msg) ; msg = 10
	```
 - **in Version 1.2.0** : Important Fixes:
 	###### - You **don't** need to place easylogging.py next to the file that uses this lib.
	###### - File level in logging.conf work on --logfile **without use --logging** (if use --logging file write all level).
	###### - V 1.2.0 is stable version and ready to use.
	###### - You can install lib from pip.
	###### - Change lib name from pylog to easylogging Because pylog already exists in pip.
- Level table :

    | Level  | Numeric value |
    | ------------- | ------------- |
    | CRITICAL  | < 50  |
    | ERROR  | < 40  |
    | WARNING  | < 30  |
    | INFO  | < 20  |
    | DEBUG  | < 10  |
    | NOTSET  | 0  |
    
- You can see test file **test.py** to know how this lib is work.


  
## LICENSE
```
Copyright 2018 LinePY - ALI B OTHMAN(AI35), Inc.

easylogging

   Licensed under the GNU License , you may not use this
   file except in compliance with the License.
   You may obtain a copy of the License at :

   https://github.com/AI35/easylog/blob/master/LICENSE
```
###### ALI .B .OTH - ORG : LinePY  
