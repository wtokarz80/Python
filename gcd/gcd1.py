a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a == 0:
    print(b)
else:
    while b != 0: 
        if a > b:
            a = a - b
        else:
            b = b - a
    print(a)