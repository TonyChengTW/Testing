__author__ = 'Tony'

import os

filepath = 'D:/source/Testing/modules/os/path.py'
cwd = os.getcwd()
basename = os.path.basename(filepath)
abspath = os.path.abspath('../..')
print 'cwd= ' + cwd
print 'basename= ' + basename
print 'abspath = ' + abspath
print 'split = ' , os.path.split(filepath)
print 'dirname = ', os.path.dirname(filepath)
print 'commonprefix = ', os.path.commonprefix(['/home/td','/home/td/ff','/home/td/fff'])

