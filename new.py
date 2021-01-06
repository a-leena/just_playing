print("Hello there! This repo is just for playing with GIT and GITHUB. Have fun!!!")
def intro (a,b):
    return "Hey!! My name is {} and I'm here {}.".format(a,b)
print(intro(input("Name: "), input("Purpose: ")))
n=int(input("Let's make some patterns! Enter a random number: "))
if n%2==0:
    m=n//2
    m1=m+1
else:
    m=n//2+1
    m1=m
for r in range(1,m):
    for c in range(0,r):
        print("*",end='')
    print()
for i in range(m1,n+1):
    for j in range(0,(n+1-i)):
        print("*",end='')
    print()
