from os.path import basename
import requests
#import T_os

url = 'https://raw.github.com/moskytw/learning-python-from-data-examples/master/sql/schools.csv'

def save(url, path=None):
    if not path:
        path = basename(url)

    with open(path, 'w') as f:
        f.write(requests.get(url).content)

#print 'T_os.getcwd=', T_os.getcwd()
#print T_os.getcwd().split('/')
#print basename(T_os.getcwd())

save(url)