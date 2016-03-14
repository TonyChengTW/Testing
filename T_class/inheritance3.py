class A(object):
    def method1(self):
        print('A.method1')

    def method2(self):
        print('A.method2')

class B(A):
    def method3(self):
        print('B.method3')

class C(A):
    def method2(self):
        print('C.method2')

    def method3(self):
        print('C.method3')

class D(B, C):
    def method4(self):
        print('D.method4')

d = D()
d.method4()
d.method3()
d.method2()
d.method1()

print dir(d)