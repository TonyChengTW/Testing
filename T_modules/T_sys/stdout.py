import sys
temp = sys.stdout
sys.stdout = open('log.txt', 'a')
print 'spam'
print 1,2,3
sys.stdout.close()
sys.stdout = temp

print 'back here'
print open('log.txt', 'r').read()
