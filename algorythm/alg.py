numbers = input("Enter the list of numbers to sort, separate them by coma: ")
print("")
my_list = numbers.split(",")
new_str_list = []
new_list = []

for x in my_list:
    z = x.strip()
    new_str_list.append(z)

for z in new_str_list:
    if z.isdigit():
        e = int(z)
        new_list.append(e)
        go_on = 1
    else:
        go_on = 0
        break

if go_on == 1:
    print("Your list to sort: ")
    print(new_list)
    print("")
    n = len(new_list)
    i = 1
    while i < n:
        j = 0
        while j <= n - 2:
            if new_list[j] > new_list[j + 1]:
                temp = new_list[j + 1]
                new_list[j + 1] = new_list[j]
                new_list[j] = temp
            else:
                j += 1
        i += 1
    else:
        print("Your sorted list: ")
        print(new_list)
else:
    print("Your list contains invalid value, you have to enter only numbers.")
    print(new_str_list)
