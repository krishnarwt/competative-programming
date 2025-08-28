a = int(input("enter num "))
for i in range(1, a+1):
    print("_"*(a-i), end=" ")
    for j in range(i):
        print("*", end=" ")
    print()
