__author__ = 'Tony'
def manuplate(d, key):
    print "print object d ID = " + str(id(d))
    def_d = d.copy()
    print "print object def_d (copy from d) ID = " + str(id(def_d))
    def_d.pop(key)
    print "print object d (after pop) ID = " + str(id(d))
    def_d2 = d.copy()
    return def_d, def_d2.keys(), def_d2.values(), def_d2.get(key), def_d2.popitem, def_d2.clear

if __name__ == '__main__':
    my_dict = {'tony' : 1, 'win' : 2, 'jackie' : 3}

    rd = manuplate(my_dict, 'tony')
    print rd
    #print ("rd=%s   rd2=%s\n") %(rd, rd2)
    #print 'rkey: 'rkey + '\n'
    #print 'rs: 'rs + '\n'
    #print 'rt: 'rt + '\n'