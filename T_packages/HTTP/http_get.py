__author__ = 'Tony'
import requests

#url = 'http://stats.moe.gov.tw/files/school/101/u1_new.csv'
url = 'https://raw.github.com/moskytw/learning-python-from-data-examples/master/sql/schools.csv'
#print requests.get(url).content
print requests.get(url).text