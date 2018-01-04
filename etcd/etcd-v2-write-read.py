#!/usr/bin/python

import etcd, time, ast

etcd_compute_key = '/cc-iaas/nodes/compute/tony-ctrl3'

client = etcd.Client(host='192.168.141.50', port=2379)

aaa = client.read(etcd_compute_key).value
bbb = ast.literal_eval(aaa)
#i = 0
#for each_aaa in aaa:
#    print("each_aaa[{}]={}").format(i, each_aaa)
#    i += 1

print("etcd_compute_key:{0} ,  value:{1}").format(etcd_compute_key, bbb)
print(type(bbb))
