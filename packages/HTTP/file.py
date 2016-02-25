__author__ = 'Tony'
save_path = 'school_list.csv'

with open(save_path, 'w') as f:
    f.write(requests.get(url).content)

with open(save_path) as f:
    print f.read()

with open(save_path) as f:
    for line in f:
        print line
