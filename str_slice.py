__author__ = 'Tony'
def get_ext(fname):
    '''Returns the extension of file fname
          '''
    dot = fname.rfind('.')
    if dot == -1:
        return ''
    else
        return fname[dot + 1:]

if __name__ == __main__:
