__author__ = 'Tony'

class Person2(object):
    def __init__(self):
        self.__name = 'Tony'

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, realname):
        self.__name = realname


p = Person2()
print "default name :", p.name

p.name = 'Emily'
print "change name : ", p.name
print dir(p)

#==========
print p._Person2__name