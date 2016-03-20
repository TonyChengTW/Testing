__author__ = 'Tony'

def odd():
    print 'step 1'
    yield 1
    print 'step 2'
    yield 2
    print 'step 3'
    yield 3
    print 'step 4'
    yield 4

for x in odd():
    print x