fname = input("Enter file name: ")
fh = open(fname)
counts = dict()
for line in fh:
    if line.startswith('From '):
        p = line.split()
        counts[p[1]] = counts.get(p[1], 0) + 1 
sender = None
scount = None
for w,c in counts.items():
    if wcount is None or wcount < c:
        scount = c
        sender = w
print(sender,scount)
