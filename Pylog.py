# Created By : Ali B Othman
# V 1.1.1
# Simple log lib for python

import logging
from time import gmtime, strftime
import sys, os
import logging.config
from configparser import ConfigParser  

config = ConfigParser()

if not os.path.exists('logging.conf'):
	f = open("logging.conf","w+")
	f.write('''[logging_option]

;Change number to enable *log level (0, 10, 20, 30, 40, 50)* without --logging or --logfile
;(This option will enable console log without --logging)

level=50

;.......................................

;Change number to set *log level (0, 10, 20, 30, 40, 50)* with --logfile (Level for log file)

file_level=0

;.......................................

;Show Error info (Pylog.error(msg, exc_info))
;True or False or None
; * (None) means that exc_info takes the value entered from the user, example: Pylog.error(msg, exc_info=True)

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


Dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logs')
logFile = 'Log %s.log' % (strftime("%Y-%m-%d %Hh-%Mm-%Ss", gmtime()))
Dirfilelog = os.path.join(Dir, logFile)
filename = 'log.py'
name = 'Loglib'

logger = logging.getLogger(__name__)
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

except:
	pass

try:
	if '--logging' in sys.argv:
		logging.disable(0)
		logger.propagate = True
except:
	pass

def logname(fname = name):
	logname.name = fname

def warning(msg):
	logger.warning(logname.name+' : '+ msg)
def debug(msg):
	logger.debug(logname.name+' : '+ msg)
def info(msg):
	logger.info(logname.name+' : '+ msg)
def warn(msg):
	logger.warn(logname.name+' : '+ msg)
def critical(msg):
	logger.critical(logname.name+' : '+ msg)
def error(msg, exc_info = False):
	if exc == 'True':
		logger.error(logname.name+' : '+ msg, exc_info = True)
	elif exc == 'False':
		logger.error(logname.name+' : '+ msg, exc_info = False)
	else:
		logger.error(logname.name+' : '+ msg, exc_info = exc_info)

if __name__ == "__main__":

#   Test Logging
	logname(name)

	info('Start log')
	warning('Warning')
	debug('Debugging...')
	warn('End.')
	critical('Stopped !!')
	
	try:
		Test_Error
	except Exception as e:
		error('**Error**', exc_info = True)
