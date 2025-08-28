a = int(input("enter num "))
for i in range(a,0, -1):
    print("_"*(a-i), end=" ")
    for j in range(i):
        print("*", end=" ")
    print()
