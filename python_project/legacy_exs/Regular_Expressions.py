import re 
file_name = input ('give the file name :')
fh = open(file_name)
total = 0
for i in fh :
    line = i.rstrip()
    strings = re.findall('([0-9]+)',line)
    if len(strings) == 0 : continue 
    for y in strings:
        num = int(y)
        total = total + num
print(total)

