# Pylog
###### Simple and Easy Logger lib for python

[![Pylog](https://img.shields.io/badge/build-passing-brightgreen.svg)]()
[![version](https://img.shields.io/badge/version-1.2.0-green.svg)]()
[![status](https://img.shields.io/badge/status-stable-brightgreen.svg)]()
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/677f082650b54782b947b429dd1c35ce)](https://www.codacy.com/project/alosh.othman55/Pylog/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=AI35/Pylog&amp;utm_campaign=Badge_Grade_Dashboard)
[![python](https://img.shields.io/badge/python-3-blue.svg)](http://www.python.org/download/)
[![windows](https://img.shields.io/badge/windows-tested-brightgreen.svg)]()
[![linux](https://img.shields.io/badge/linux-tested-brightgreen.svg)]()
[![license](https://img.shields.io/badge/license-GNU-blue.svg)](https://github.com/AI35/Python-Service/blob/master/LICENSE)

## REQUIREMENTS
- Python-3 --> http://www.python.org/download/

## Notes
- Now This lib is **Stable**.
- I am created this lib because i want use easy logging lib.
- ~~**Important(To Work --logfile)** : You need to put Pylog.py in same folder with your main file.~~
- ~~**Known Bug** : You need to place pylog.py next to the file that uses this lib.~~

## Installation

- Clone this repo:
	
	```
	$ git clone https://github.com/AI35/Pylog
	```

## Usage
- First you need import lib for your file and Set name :
  ```
    import Pylog
    
    Pylog.logname(__file__)
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
  	###### - This option work on --logfile without use --logging (if use --logging file write all level)
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
 - **in Version 1.1.2** : Fix DeprecationWarning:
  	###### - Fix warn function
	
 - **in Version 1.1.3** : Fix input msg:
  	###### - You can know input (int or any value) , example:
	```
	  Pylog.error(msg) ; msg = 10
	```
 - **in Version 1.2.0** : Important Fixes:
 	###### - You don't need to place pylog.py next to the file that uses this lib.
	###### - file level in logging.conf work on --logfile **without use --logging** (if use --logging file write all level)
	###### - V 1.2.0 is stable version and ready to use.
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
###### ALI .B .OTH - ORG : LinePY  
