def fibonacci():
    i = 0
    j = 1
    k = 0
    fib = 0
    fib_list = []
    while i < int(number):
        fib_list.append(fib)
        fib = j + k
        j = k
        k = fib
        i += 1
    max_n = max(fib_list)
    for z, e in enumerate(fib_list):
        z += 1
        print(f"{z}. " + str(e).rjust(len(str(max_n))))


keep_asking = True
while keep_asking:
    number = input("How many numbers of Fibonacci sequence do you want to print out?: ")
    if number.isdigit() and int(number) > 0:
        fibonacci()
        break
    else:
        ask = input("Invalid value, do you want to try again? [Y/N]: ")
        while ask not in ["Y", "y", "N", "n"]:
            ask = input("Invalid command, do you want to try again? [Y/N]: ")
        if ask == "N".lower():
            print("Bye, bye.")
            break
        elif ask == "Y".lower():
            keep_asking
