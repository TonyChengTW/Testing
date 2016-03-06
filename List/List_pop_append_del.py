__author__ = 'Tony'
list = [1, 2, 3, 4, 5, 6]
list.pop()
print list
print (list)
print "list (Mutable) object id (pop) = " + str(id(list)

list.append(7)
print list
print "list (Mutable) object id (append) = " + str(id(list)

del list[2]
print list
print "list (Mutable) object id (del) = " + str(id(list)


aaa = 123
print "aaa (Immutable) object id (123) = " + str(id(aaa))
aaa = 456
print "aaa (Immutable) object id (456) = " + str(id(aaa))