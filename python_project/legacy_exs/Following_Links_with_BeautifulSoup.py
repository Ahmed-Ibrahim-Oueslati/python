# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
url = input('Enter - ')
countstring = input('Enter count:')
count = int(countstring)
positionstring = input('Enter position:')
position = int(positionstring)


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
# Retrieve all of the anchor tags
tags = soup('a')
print('Retrieving:',url)
new_url = tags[(position - 1)].get('href', None)
print('Retrieving:',new_url)

for i in range(count - 1):
    html = urllib.request.urlopen(new_url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    new_url = tags[(position - 1)].get('href', None)
    print('Retrieving:',new_url)

