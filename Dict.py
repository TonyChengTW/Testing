__author__ = 'Tony'
def manuplate(d, key):
    """
    Testing Dict
    :param key:
    :param s:
    :param t:
    :return:
    """
    def_d = d.copy()
    def_d.pop(key)
    def_d2 = d.copy()
    return def_d, def_d2.keys(),

if __name__ == '__main__':
    my_dict = {'tony' : 1, 'win' : 2, 'jackie' : 3}

    rd = manuplate(my_dict, 'tony')
    print type(rd)
    #print ("rd=%s   rd2=%s\n") %(rd, rd2)
    #print 'rkey: 'rkey + '\n'
    #print 'rs: 'rs + '\n'
    #print 'rt: 'rt + '\n'