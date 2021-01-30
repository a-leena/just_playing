def computepay(h,r):
    if h<=40:
        pay=h*r
    else:
        pay=40*r + (h-40)*1.5*r
    return pay
h=float(input("Hours: "))
r=float(input("Hourly rate: "))
x=computepay(h,r)
print ("Pay ",x)
