__author__ = 'Tony'
class ClassA(object):
    def __init__(self):
        print "Hello Python"

    def __del__(self):
        print "Goodbye Python"

    def __str__(self):
        return "This is Class A %s" % self.say_hello('Tony1')

    def say_hello(self, words):
        print "Hello,", words

    def do_nothing(self):
        pass

a = ClassA()
#a.say_hello("Tony")
print a

