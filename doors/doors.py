doors = "1" * 100
doors_lst = list(doors)
ar = []
i = 0
j = 0
while i < 100:
    while j < len(doors_lst):
        if doors_lst[j] == "1":
            doors_lst.insert(j, "0")
            doors_lst.pop(j+1)
        elif doors_lst[j] == "0":
            doors_lst.insert(j, "1")
            doors_lst.pop(j+1)
        j = j + 1 + i
    i += 1
    j = i
print(doors_lst)

result = []
e = 0
while e < len(doors_lst):
    if doors_lst[e] == "0":
        result.append(str(e + 1))
    e += 1
print(f"The following doors are open:  {', '.join(result)}")
