class Person:
    def __init__(self, name = '', age = 0):
        self._name = name
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if 0 < age <= 100:
            self._age = age

    def display(self):
        print(self)

    def __str__(self):
        return "Person('%s',%d)" % (self._name, self._age)

    def __repr__(self):
        return str(self)


if __name__ == '__main__':
    p = Person('Tony',40)
    print p
    p.age = 55
    print p.age
    p.age = -4
    print p.age
