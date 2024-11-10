fhand = open('done.py','r')
print(fhand)
"""for i in fhand:
    if i.startswith('print'):
        i = i.rstrip()
        print(i)
"""
"""
lines = fhand.read()
print(len(lines))
print(lines)
"""

for i in fhand:
    if 'num' in i:
        i = i.rstrip()
        print(i)