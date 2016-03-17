classmates = ['Michael', 'Bob', 'Tracy']
classmates.insert(1,'Jack')
print classmates

classmates = ('Michael', 'Bob', 'Tracy')
classmates = ('Jack',)
print type(classmates)
print classmates

s = set([1, 2, 3])
s.add(4)
print s

s.remove(2)
print s

l = range(100)
print l

print l[1:10]
print l[:10]
print l[3:]
print l[-10:]
print l[:20:2]