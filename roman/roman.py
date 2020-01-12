a = input("Enter a natural number from 1 to 4000: ")
a_list = []
go_on = True
while go_on:
    try:
        x = int(a)
        if x <= 0 or x > 4000:
            a = input("Enter a natural number from 1 to 4000: ")
        else:
            go_on = False
    except ValueError:
        a = input("Enter a natural number from 1 to 4000: ")
arr = ["I", "V", "X", "L", "C", "D", "M"]
a_list = [int(e) for e in a]
a_list.reverse()
r_list = []
j = 0
i = 0
if a == "4000":
    print("MMMM")
else:
    while i < len(a_list):
        if a_list[i] in range(1, 4):
            r_list.insert(i, arr[j]*a_list[i])
        elif a_list[i] == 4:
            r_list.insert(i, arr[j]+arr[j+1])
        elif a_list[i] == 5:
            r_list.insert(i, arr[j+1])
        elif a_list[i] == 6:
            r_list.insert(i, arr[j+1] + arr[j])
        elif a_list[i] == 7:
            r_list.insert(i, arr[j+1] + arr[j]*2)
        elif a_list[i] == 8:
            r_list.insert(i, arr[j+1] + arr[j]*3)
        elif a_list[i] == 9:
            r_list.insert(i, arr[j] + arr[j+2])
        i += 1
        j += 2
r_list.reverse()
print("".join(r_list))
