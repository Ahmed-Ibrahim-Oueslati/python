fname = input("Enter file name: ")
fh = open(fname)
counts = dict()
for line in fh :
    names = line.split()
    for name in names:
        counts[name] = counts.get(name, 0) + 1 
wcount = None
word = None

for w,c in counts.items():
    if wcount is None or wcount < c:
        wcount = c
        word = w
print("the word is :",word,"\nthe count is : ",wcount)