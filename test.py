# Created By : Ali B Othman
# V 1.0.0
# Simple Test File

from Pylog import *

########## very important ############
name = 'test.py'
logname(name)
######################

debug('logs debug done')
info('Start log')
warning('Warning')
debug('Debugging ..')
warn('End.')
critical('Stopped !!')

try:
	Test_Error
except Exception as e:
	error('**Error**', exc_info = True)

