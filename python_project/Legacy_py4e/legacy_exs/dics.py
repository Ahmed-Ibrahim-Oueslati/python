"""dic = dict()
dic["title"] = "the prg"
dic["pages"] = 120 
print(dic)"""
counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
for key in counts:
    if counts[key] > 10:
        print(key, counts[key])