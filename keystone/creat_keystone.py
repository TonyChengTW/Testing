from httplib2 import *
import json

ENDPOINT = 'http://10.89.151.11:35357/v2.0'
ENDPOINT2 = 'http://10.89.151.11:35357/v3'

names = ['admin', 'bao1-vpn1','baotest1']

class HttpHelper:

    def do_request(self, url, method):

        uri = ENDPOINT + '/' + url
        header = {
            'Content-Type': 'application/json',
            "X-Auth-Token": self.X_AUTH_TOKEN
        }
        response = Http().request(uri, method, headers=header)
        return response


    def create_token(self):
        url = ENDPOINT + '/' + 'tokens'
        method = 'POST'
        header ={
            'Content-Type': 'application/json'
        }
        body = '{"auth": {"tenantName": "admin", "passwordCredentials": { "username": "admin", "password": "Abc12345" }}}'
        response = Http().request(url, method=method, headers=header, body=body)
        #print response , type(response)
        tonken = json.loads(response[1])
        #print tonken , type(tonken)
        self.X_AUTH_TOKEN = tonken['access']['token']['id']

    def user_list(self):
         self.create_token()
         url = 'users'
         method = 'GET'
         result = self.do_request(url, method)
         users = result[1]
         # print users , type(users)
         users = json.loads(users)
         # print users , type(users)
         userlist = users['users']
         for i in xrange(len(userlist)):
             name = users['users'][i]['username']
             if name in names:
                print name


    def create_project(self):
        self.create_token()
        url = ENDPOINT + '/' + 'tenants'
        method = 'POST'
        header = {
            'Content-Type': 'application/json',
            "X-Auth-Token": self.X_AUTH_TOKEN
        }
        body = '{"tenant": {"enabled": true, "name": "baobaotest13", "description": "baobaotest"}}'
        response = Http().request(url, method=method, headers=header, body=body)
        print response , type(response)
        tenant = json.loads(response[1])
        print tenant , type(tenant)
        self.project_id = tenant['tenant']['id']
        #print self.project_id

    def delete_project(self):
        #self.create_token()
        self.create_project()
        url = ENDPOINT2 + '/' + 'projects'+'/'+self.project_id
        print url , type(url)
        method = 'DELETE'
        header = {
            'Content-Type': 'application/json',
            "X-Auth-Token": self.X_AUTH_TOKEN
        }
        response = Http().request(url, method=method, headers=header)
        print response , type(response)
        result = response[0]
        print result , type(result)

        status = result.__getattribute__('status')
        if status >= 400:
           print 'please send again'
           return None


    def create_role(self):
        self.create_token()
        url = ENDPOINT + '/' + 'OS-KSADM'+'/'+'roles'
        method = 'POST'
        header = {
            'Content-Type': 'application/json',
            "X-Auth-Token": self.X_AUTH_TOKEN
        }
        body = '{"role": {"id": "c7aba54110a7481293644efe65ae7407", "name": "hahaha6887"}}'
        response = Http().request(url, method=method, headers=header, body=body)
        print response , type(response)
        tenant = json.loads(response[1])
        print tenant , type(tenant)
        self.role_id = tenant['role']['id']
        print self.role_id

    def delete_role(self):
        #self.create_token()
        self.create_role()
        url = ENDPOINT2 + '/' + 'roles'+'/'+self.role_id
        print url , type(url)
        method = 'DELETE'
        header = {
            'Content-Type': 'application/json',
            "X-Auth-Token": self.X_AUTH_TOKEN
        }
        response = Http().request(url, method=method, headers=header)
        print response , type(response)
        result = response[0]
        print result , type(result)

        status = result.__getattribute__('status')
        if status >= 400:
           print 'please send again'
           return None

    def create_user(self):
        self.create_token()
        url = ENDPOINT2 + '/' + 'users'
        method = 'POST'
        header = {
            'Content-Type': 'application/json',
            "X-Auth-Token": self.X_AUTH_TOKEN
        }
        body = '{"user": {"default_project_id": "a06fa3bf747345ecbb3c91b6d1819033","description": "James Doe user",' \
               '"email": "jdoe@example.com","enabled": true,"name": "baobao8099000", "password": "123t"}}'
        response = Http().request(url, method=method, headers=header, body=body)
        print response , type(response)
        tenant = json.loads(response[1])
        print tenant , type(tenant)
        self.user_id = tenant['user']['id']
        print self.user_id

    def delete_user(self):
        #self.create_token()
        self.create_user()
        url = ENDPOINT2 + '/' + 'users'+'/'+self.user_id
        print url , type(url)
        method = 'DELETE'
        header = {
            'Content-Type': 'application/json',
            "X-Auth-Token": self.X_AUTH_TOKEN
        }
        response = Http().request(url, method=method, headers=header)
        print response , type(response)
        result = response[0]
        print result , type(result)

        status = result.__getattribute__('status')
        if status >= 400:
           print 'please send again'
           return None

if __name__ == "__main__":
    HttpHelper().delete_user()
