# Created By : Ali B Othman
# Test V 1.2.0
# Simple Test File

from easylogging import *

########## very important ############
logname(__file__)
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
	error('**Error : exc_info = True**', exc_info = True)

print('########### TEST ERROR ###########')
try:
	Test_Error
except Exception :
	error('**Error : exc_info = False**', exc_info = False)
