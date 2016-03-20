__author__ = 'Tony'

def decorator(func):
    print "execute something in decorator func"
    return(func)

def func1(*args, **kwargs):
    pargs = args
    pkwargs = kwargs
    print "pargs=", pargs
    print "pkwargs=", pkwargs
    return

func1(1, 2, 3, 4, Tony=38, Emily=65)
decorator(func_obj)
