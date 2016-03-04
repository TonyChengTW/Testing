__author__ = 'Tony'
def get_ext(fname):
    '''Returns the extension of file fname
          '''
    dot = fname.rfind('a')
    if dot == -1:
        return ''
    else:
        return fname[dot + 1:]

if __name__ == '__main__':
    aa = get_ext('testing.tx')
    bb = '  12345678  '
    print '\'' + bb.rstrip() + '\''

    a1 = 123
    a2 = 'tony'
    a3 = ['item1','item2','item3']
    print 'a1=%d, a2=%s, a3=%s' % (a1, a2, a3)

    dict = {'d1': 10, 'd2': 20 , 'd3': 30}
    print 'dict = %(d1)s , %(d2)d , %(d3)s '% dict