n = int(input("enter a num"))
total = 0
while n > 0:
    digit = n % 10
    total = total + digit
    n = n // 10
print(total)     