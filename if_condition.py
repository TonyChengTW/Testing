__author__ = 'Tony'
pwd = raw_input('what is the password? ')
if pwd == 'apple':
    print('Loggin on ...')
else:
    print('Incorrect password')
print('done first condition!')

age = raw_input('How old are you? ')
if age <= 2:
    print " free"
elif 2 < age < 13:
    print " child fare"
else:
    print " adult fare"