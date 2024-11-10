fname = input("Enter file name: ")
fh = open(fname)
lst = list()

for line in fh:
    p = line.split()
    for i in p:
        if i not in lst :
            lst.append(i)
lst.sort()
print(lst)