name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
count = dict()
for i in handle:
    if i.startswith('From '):
        chunk = i.split()
        count[chunk[5][:2]] = count.get(chunk[5][:2], 0) + 1 
nn = sorted([(k,v) for k,v in count.items()])
for k , v in nn:
    print(k,v)


