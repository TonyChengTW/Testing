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

class Person(object):
    def __init__(self, name = 'Default Name', age = 30):
        self._name = name
        self._age = age

    @property
    def age(self):
        print "enter into property"
        return self._age

    @age.setter
    def age(self, age):
        if 0 < age <= 150:
            self._age = age

    def __str__(self):
        return "print by __str__ - Person('%s',%d)" % (self._name, self._age)

a = ClassA()
a.say_hello("Tony")
print a

# --------------------
b = Person()
b._name = 'Emily'
b.age = 65
print "b.age = ", b.age

b.age = 200
print "b.age = (200)", b.age

c = Person()
print c