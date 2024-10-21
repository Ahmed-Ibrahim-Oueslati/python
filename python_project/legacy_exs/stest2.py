import urllib.request, urllib.parse, urllib.error

fh = urllib.request.urlopen('https://www.dr-chuck.com/page1.htm')
for line in fh:
    print(line.decode().strip())