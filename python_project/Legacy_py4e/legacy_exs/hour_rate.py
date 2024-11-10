hrs = input("Enter Hours:")
h = float(hrs)

rate = input("Enter rate")
r = float(rate)
extra_pay = 0
p = 0
if h > 40 :
    p = h - 40
    h = h - p
extra_pay  = 1.5 * r * p
print ((h * r) + extra_pay)