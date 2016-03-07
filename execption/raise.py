__author__ = 'Tony'
def get_age():
    while True:
        try:
            age = int(raw_input('How old are u?'))
            return age
        except ValueError:
            print('Please enter an integer value')
        finally:
            print "the job is done"
if __name__ == '__main__':
    print get_age()

