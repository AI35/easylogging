# Created By : Ali B Othman
# V 1.1.2
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
critical('Stopped !!')

try:
	Test_Error
except Exception as e:
	error('**Error**', exc_info = True)

