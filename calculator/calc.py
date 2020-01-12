a = input("Enter first number (or a letter to exit): ")
operators = ['+', '-', '*', '/']
go_on = 1
try:
    val_a = float(a)
    go_on = 1
except ValueError:
    go_on = 0
if go_on == 1:
    oper = input("Enter an operator (+, -, *, /): ")
    while oper not in operators:
        oper = input("Enter correct operator (+, -, *, /): ")
    b = input("Enter another number (or letter to exit): ")
    try:
        val_b = float(b)
        go_on = 1
    except ValueError:
        go_on = 0
    if go_on == 1:
        if oper == "+":
            print(val_a + val_b)
        elif oper == "-":
            print(val_a - val_b)
        elif oper == "*":
            if val_a == 0 or val_b == 0:
                print("We cannot multiply by 0.")
            else:
                print(val_a * val_b)
        elif oper == "/":
            if val_a == 0 or val_b == 0:
                print("We cannot divide by 0.")
            else:
                print(val_a / val_b)
    elif go_on == 0:
        print("Bye, bye.")
elif go_on == 0:
    print("Bye, bye.")