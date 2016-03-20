__author__ = 'Tony'
a = [x*x for x in range(1,10) if x != 5]
print type(a)
print a

b = (x*x for x in range(1,10) if x != 5)
print type(b)

print b.next()
print b.next()
print b.next()
print b.next()
print b.next()