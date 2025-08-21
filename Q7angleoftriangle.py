A1=int(input("enter the number1"))
A2=int(input("enter the number2"))
A3=int(input("enter the number3"))
if A1+A2+A3==180 and A1>0 and A2>0 and A3>0:
    if A1==90 and A2==90 and A3==90:
        print("Right triangle")
    elif(A1>90 and A2>90 and A3>90):
        print("Obtuse triangle")
    else:
        print("Acute triangle")