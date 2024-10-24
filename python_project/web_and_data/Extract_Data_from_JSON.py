import json
import urllib.request

url = input('Enter location: ')
if len(url) < 1 : 
    url = 'http://py4e-data.dr-chuck.net/comments_42.xml'

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved',len(data),'characters')

info = json.loads(data)
print('User count:', len(info))
nums = list()
for item in info['comments']:
    
    nums.append(int(item['count']))
print('count',len(nums))
print('sum',sum(nums))
    