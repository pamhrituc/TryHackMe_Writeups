import json
import urllib3

http = urllib3.PoolManager()
url = 'http://10.10.169.100:3000'
req = http.request('GET', url)
res = json.loads(req.data.decode('utf-8'))
flag = ""
while res['next'] != 'end':
    req = http.request('GET', url + '/' + res['next'])
    res = json.loads(req.data.decode('utf-8'))
    print(res)
    if res['value'] != 'end':
        flag += res['value']

print("flag: " + flag)
