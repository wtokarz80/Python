co_input = input("Enter the co-ordinates of the three vertices of the triangle, separate them with a space: ")
    
co_split = co_input.split(" ")
num_list = []
for x in co_split:
    try:
        x = float(x)
        if x not in range(-100, 100):
            break
        num_list.append(x)
    except ValueError:
        break
if len(num_list) != 6:
    print("You entered wrong number of co-ordinates or value. Please try again.")
else:
    a, b, c, d, e, f = num_list[0], num_list[1], num_list[2], num_list[3], num_list[4], num_list[5]
    area = abs(((c-a)*(f-b) - (d-b)*(e-a))*0.5)
    print(f"Triangle area: {area}")
