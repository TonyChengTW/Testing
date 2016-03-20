__author__ = 'Tony'

d1 = dict(a='tony', b='jimmy', c='emily', d='lucy')
print d1

print d1.pop('d')
print d1

if d1.has_key('c') is True:
    print "have 'c'\n"
else:
    print "no 'c' is exist\n"

for i in d1:
    print "d1.[i]" + d1[i]
