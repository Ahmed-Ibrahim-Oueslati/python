b = {'phmed' : 22 , 'marwa' : 7, 'khaled' : 17}
#turning the dic intou a list of tupels
k = b.items()
print(k)
#sorting the list with sorted 
o = sorted(k)
print(o)
ll = list()
for y , u in k:
    ll.append((u,y))

ll = sorted(ll, reverse=True)

print(ll)
