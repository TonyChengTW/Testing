class Person:
    """ Class to represent a person
    """
    def __init__(self):
        self.name = ''
        self.age = 10

    def display(self):
        print("Person('%s', %d)" % (self.name, self.age))

p = Person()
p.name = 'Tony'
p.age = 39
a = rational(1)