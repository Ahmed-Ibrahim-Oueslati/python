score = input("Enter Score: ")
x = float(score)
s = "p"
if x >= 0.9 : 
    s = 'A'
    print(s)

elif x >= 0.8 : 
    s = 'B'
    print(s)
elif x >= 0.7 : 
    s = 'C'
    print(s)
elif x >= 0.6 : 
    s = 'D'
    print(s)
elif x < 0.6 : 
    s = 'F'
    print(s)
else : print ("please enter a valid score")
