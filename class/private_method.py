__author__ = 'Tony'
class ClassA:
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

class Person:
    def __init__(self, name = 'Default Name', age = 30):
        self.name = name
        self.age = age

    def __str__(self):
        return "print by __str__ - Person('%s',%d)" % (self.name, self.age)

a = ClassA()
a.say_hello("Tony")
print a

# --------------------
b = Person()
b.name = 'Emily'
b.age = 65
print b

c = Person()
print c