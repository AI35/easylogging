# Created By : Ali B Othman
# V 1.2.0
# Simple log lib for python

import logging
from time import gmtime, strftime
import sys, os
import logging.config
from configparser import ConfigParser

def logname(dname = __file__):
	logname.dname = dname
	d = dname.split("\\")
	dn = d[:-1]
	logname.name = d[-1]
	run()

def warning(msg):
	run.logger.warning(logname.name+' : '+ str(msg))
def debug(msg):
	run.logger.debug(logname.name+' : '+ str(msg))
def info(msg):
	run.logger.info(logname.name+' : '+ str(msg))
def critical(msg):
	run.logger.critical(logname.name+' : '+ str(msg))
def error(msg, exc_info = False):
	if exc == 'True':
		run.logger.error(logname.name+' : '+ str(msg), exc_info = True)
	elif exc == 'False':
		run.logger.error(logname.name+' : '+ str(msg), exc_info = False)
	else:
		run.logger.error(logname.name+' : '+ str(msg), exc_info = exc_info)



config = ConfigParser()

if not os.path.exists('logging.conf'):
	f = open("logging.conf","w+")
	f.write('''[logging_option]

;Change number to enable *log level (0, 10, 20, 30, 40, 50)* without --logging or --logfile
;(This option will enable console log without --logging)

level=50

;.......................................

;Change number to set *log level (0, 10, 20, 30, 40, 50)* with --logfile (Level for log file)
;This option work on --logfile without use --logging (if use --logging file write all level)

file_level=0

;.......................................

;Show Error info (easylogging.error(msg, exc_info))
;True or False or None
; * (None) means that exc_info takes the value entered from the user, example: easylogging.error(msg, exc_info=True)

exc_info=None''')
	f.close()

config.read('logging.conf')
prop = config.get('logging_option', 'file_level')
prop = int(prop)

level = config.get('logging_option', 'level')
level=int(level)

exc = config.get('logging_option', 'exc_info')
formated = '%(asctime)s - %(levelname)s - %(message)s'

logging.basicConfig(level = logging.DEBUG, format=formated)

def run():
	Dir = os.path.join(os.path.dirname(os.path.abspath(logname.dname)), 'logs')
	logFile = 'Log %s.log' % (strftime("%Y-%m-%d %Hh-%Mm-%Ss", gmtime()))
	Dirfilelog = os.path.join(Dir, logFile)


	logger = logging.getLogger(__name__)
	run.logger = logger
	logging.disable(level)
	if level < 50:
		logger.propagate = True
	else:
		logger.propagate = False

	try:
		if '--logfile' in sys.argv:
			if not os.path.exists('logs'):
				os.makedirs('logs')
			handler = logging.FileHandler(Dirfilelog)
			handler.setLevel(logging.DEBUG)
			formatter = logging.Formatter(formated)
			handler.setFormatter(formatter)
			logger.addHandler(handler)
			logging.disable(prop)

	except Exception:
		pass

	try:
		if '--logging' in sys.argv:
			logging.disable(0)
			logger.propagate = True
	except Exception:
		pass
