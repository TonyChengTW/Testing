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

    def __str__(self):
        return "name=%s" % self.name

p = Person2()
print "default:", p

p.name = 'Emily'
print "change: ", p
print dir(p)

#==========
print p._Person2__name