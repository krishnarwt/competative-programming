a= int(input("enter a num "))
for i in range(1, a+1):
    for j in range(1,i+1):
        if j%2==0:
            print("*",end=" ")
        else:
            print(j,end=" ")
    print()