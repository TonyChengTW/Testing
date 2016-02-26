from os.path import basename
import requests
#import os

url = 'https://raw.github.com/moskytw/learning-python-from-data-examples/master/sql/schools.csv'

def save(url, path=None):
    if not path:
        path = basename(url)

    with open(path, 'w') as f:
        f.write(requests.get(url).content)

#print 'os.getcwd=', os.getcwd()
#print os.getcwd().split('/')
#print basename(os.getcwd())

save(url)