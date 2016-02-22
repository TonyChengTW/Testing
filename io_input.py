__author__ = 'Tony'
import os

x = 0.9992132553123
print('%.6f' % x)

a, b, c = 'cat', 3.14, 6
s = 'there\'s %d %ss older than %.2f years' %(c, a, b)
print s

y = 'my {pet} has {prob}'.format (pet = 'dog', prob = 'fleas')
print y

print os.getcwd()
print os.listdir(os.getcwd())
print os.chdir('C:\\Users\\tony\\PycharmProjects')
print os.getcwd()
print os.path.isfile('C:\\Users\\tony\\PycharmProjects')