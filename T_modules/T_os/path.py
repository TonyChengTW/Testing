__author__ = 'Tony'

import os, time, datetime

filepath = '/root/Testing/T_modules/T_os/path.py'

print 'cwd= ' + os.getcwd()
print 'listdir = ' , os.listdir('/root/Testing')
print 'isfile = ' + str(os.path.isfile(filepath))
print 'isdir = ' + str(os.path.isdir(filepath))
print 'basename= ' + os.path.basename(filepath)
print 'abspath = ' + os.path.abspath('../..')
print 'split = ' , os.path.split(filepath)
print 'dirname = ', os.path.dirname(filepath)
print 'commonprefix = ', os.path.commonprefix(['/home/td','/home/td/ff','/home/td/fff'])
print 'exists = ', os.path.exists(filepath)

