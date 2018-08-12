# Created By : Ali B Othman
# Test V 1.1.3
# Simple Test File

from Pylog import *

########## very important ############
name = 'test.py'
logname(name)
######################
print('########### TEST DEBUG ###########')
debug('logs debug done')
print('########### TEST INFO ###########')
info('Start log')
print('########### TEST WARNING ###########')
warning('Warning')
print('########### TEST CRITICAL ###########')
critical('Stopped !!')
print('########### TEST INPUT int ###########')
info(1)
print('########### TEST INPUT float ###########')
debug(3.4)

print('########### TEST ERROR ###########')
try:
	Test_Error
except Exception :
	error('**Error**', exc_info = True)

