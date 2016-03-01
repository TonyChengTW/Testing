__author__ = 'Tony Cheng'

import pymysql

def access_mysql():
    conn = pymysql.connect(host='localhost', port=3306,user='root', passwd='Abc12345', db='nova')
    cur.execute("SELECT * FROM nova limit 10")
    for r in cur:
        print("row_number:"+str(cur.rownumber))
        print "id:"+str(r[0])+"key:"+str(r[1])+" mean:"+str(r[2])
    cur.close()
    conn.close()

if __name__== '__main__':
    access_mysql()
