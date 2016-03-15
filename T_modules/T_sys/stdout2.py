__author__ = 'Tony'

with open('printfile.txt', 'w') as f:
    print >> f, 'testing'
    print >> f, 1,2,3
