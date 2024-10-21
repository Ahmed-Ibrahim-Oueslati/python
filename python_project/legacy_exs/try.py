age = 0
while age < 1 :
###
    x = input("ur age ?")
    try :
        age = int(x)
    except :
        age = -1 

 ###   
print("u 're ", age, " years old")