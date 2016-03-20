#coding:utf-8

def deco(func):  #第一次执行func时会打印，后面再执行就不会打印了
    print "before called"
    return func


def deco1(func): #每次执行func都会打印
    def wrapper():
        print "before called"
        return func()
    return wrapper

def deco2(func): #带参数的func
    def wrapper(*args, **kw):
        print "before called"
        return func(*args, **kw)
    return wrapper

def deco3(func): #多层定义
    def wrapper(*args,**kw):
        print "wrapper"
        def wrapper1():
            print "wrapper1"
            def wrapper2():
                print "wrapper2"
                return func(*args,**kw)
            return wrapper2()
        return wrapper1()
    return wrapper

def deco4(arg): #带参数的生成器,打印可变参数
    def _deco(func):
        def wrapper(*args, **kw):
            print ("*********%s**********" % arg)
            return func(*args, **kw)
        return wrapper
    return _deco

@deco
def myfunc():
    print("*********%s**********" % myfunc.__name__)

@deco2
def myfunc1(a):
    print ("*********%s**********" % a)

@deco4("mymodule")
def myfunc2(a):
    print ("*********%s**********" % a)
    
for x in range(3):
    myfunc()