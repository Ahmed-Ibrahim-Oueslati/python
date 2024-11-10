counts = dict()
names = ["hameda","salma","oumaima", "salma"]
for name in names:
    counts[name] = counts.get(name, 0) + 1 
    """
    if name not in counts:
        counts[name] = 1
    else :
        counts[name] = counts[name] + 1 """
     
print(counts)
x = counts.get("hjem", 0)
print(x)
print(counts)