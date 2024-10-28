import re 
import sqlite3
import urllib.request
from urllib.error import URLError, HTTPError

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')


url = input('Enter a URL: ')

# Add a User-Agent header to mimic a browser request
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
req = urllib.request.Request(url, headers=headers)
list_8 = list()
try:
    uh = urllib.request.urlopen(req)
    for line in uh:
        list_8.append(line.decode('utf-8').strip())
except HTTPError as e:
    print("HTTP error:", e.code, e.reason)
except URLError as e:
    print("URL error:", e.reason)



for line in list_8:
    if not line.startswith('From: '): continue
    org = re.findall('@(.+)',line)
    domain = org[0]
    
    
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (domain,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (domain,)) 
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (domain,))
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()