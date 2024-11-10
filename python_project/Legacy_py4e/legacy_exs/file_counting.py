import operator
fname = input("Enter file name: ")
fh = open(fname)
list = []
counts = dict()
for line in fh :
    names = line.split()
    list = list + names 
    for name in names:
        counts[name] = counts.get(name, 0) + 1 
print("words : \n", list , '\n')
print("counting...\n")
sorted_dict = dict(sorted(counts.items(), key=operator.itemgetter(1), reverse=True))
first_4_elements = dict([item for item in sorted_dict.items()][:4])
for i in first_4_elements:
    print(i, first_4_elements[i])
  
print(first_4_elements.keys())
print(first_4_elements.values())
print(first_4_elements.items())