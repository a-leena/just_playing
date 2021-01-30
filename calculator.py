#A simple calculator
while True:
    print("Choices-\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Done")
    print("Note: Enter '=' when done")
    oper=input("Choice: ")
    try:
        op=int(oper)
        if op==1:
            print("Enter the numbers to be added")
            sum=0
            while True:
                num=input(" ")
                try:
                    n=float(num)
                    sum+=n
                except:
                    if num=="=":
                        break
                    else:
                        print("error!")
                        continue
            print(sum)
            print("")
            continue
        elif op==2:
            diff=0
            print("Enter the numbers to be subtracted")
            for i in range(0,1):
                num1=input(" ")
                try:
                    n1=float(num1)
                    diff=n1-diff
                    break
                except:
                    print("error!")
                    continue
            for i in range(0,1):
                num2=input(" ")
                try:
                    n2=float(num2)
                    diff-=n2
                    break
                except:
                    if num2=="=":
                        break
                    else:
                        print("error!")
                        continue
            print(diff)
            print("")
            continue
        elif op==3:
            print("Enter the numbers to be multiplied")
            prod=1
            while True:
                num=input(" ")
                try:
                    n=float(num)
                    prod=prod*n
                except:
                    if num=="=":
                        break
                    else:
                        print("error!")
                        continue
            print(prod)
            print("")
            continue
        elif op==4:
            quo=1
            print("Enter the numbers to be divided")
            for i in range(0,1):
                num=input(" ")
                try:
                    n=float(num)
                    quo=n
                    break
                except:
                    print("error!")
                    continue
            for i in range(0,1):
                den=input(" ")
                try:
                    d=float(den)
                    quo=quo/d
                    break
                except:
                    if den=="=":
                        break
                    else:
                        print("error!")
                        continue
            print(quo)
            print("")
            continue
        else:
            print("Exiting")
            exit()
    except:
        print("error!")
        continue
