__author__ = 'Tony'

import requests
import csv

from os.path import basename
from os.path import exists

save_path = 'school_list.csv'
url = 'https://raw.github.com/moskytw/learning-python-from-data-examples/master/sql/schools.csv'

def save(url, path=None):
    if not path:
        path = basename(url)

    with open(path, 'w') as f:
        f.write(requests.get(url).content)

if __name__ == '__main__':
    if not exists(save_path):
        save(url, save_path)

    with open(save_path) as f:
        for row in csv.reader(f):
            print row