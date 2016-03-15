class FooParent(object):
    def __init__(self):
        self.parent = 'I am parent.'
        print 'Parent'

    def bar(self, message):
        print message, 'from Parent'


class FooChild(FooParent):
    def __init__(self):
        FooParent.__init__(self)
        print 'Child'

    def bar(self, message):
        FooParent.bar(self, message)
        print 'Child bar D_function.'
        print self.parent

if __name__ == '__main__':
    fooChild = FooChild()
    fooChild.bar('Hello World')