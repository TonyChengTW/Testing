__author__ = 'Tony'
import requests

save_path = 'school_list.csv'
url = 'https://raw.github.com/moskytw/learning-python-from-data-examples/master/sql/schools.csv'

with open(save_path, 'w') as f:
    f.write(requests.get(url).content)

with open(save_path) as f:
    print f.read()

with open(save_path) as f:
    for line in f:
        print line
