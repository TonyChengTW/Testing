#!/usr/bin/python

import etcd3, time, ast

value = {
   "hostname": "tony-7878",
   "role": "AAA",
   "msg": "asd",
   "last_modified": time.time()
}

updated_value = {
   "role": "BBB",
   "msg": "def",
   "last_modified": time.time()
}

value.update(updated_value)

#etcd_compute_key = '/cc-iaas/nodes/compute/tony7878'
etcd_compute_key = '/cc-iaas/nodes/compute/tony-ctrl78'

client = etcd3.client(host='192.168.141.50', port=2379)
client.put(etcd_compute_key, str(value))

aaa = client.get(etcd_compute_key)
#i = 0
#for each_aaa in aaa:
#    print("each_aaa[{}]={}").format(i, each_aaa)
#    i += 1
bbb = ast.literal_eval(aaa[0])
print bbb

print("etcd_compute_key:{0} ,  value:{1}").format(etcd_compute_key, bbb)
print(type(bbb))
