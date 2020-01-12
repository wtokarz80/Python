import random

first_input = input("How many units attack: ")
while first_input not in ["1", "2", "3"]:
    first_input = input("How many units attack: ")
second_input = input("How many units defend: ")
while second_input not in ["1", "2"]:
    second_input = input("How many units defend: ")

ask1 = int(first_input)
ask2 = int(second_input)
a_1 = random.randrange(1, 7)
a_2 = random.randrange(1, 7)
a_3 = random.randrange(1, 7)
d_1 = random.randrange(1, 7)
d_2 = random.randrange(1, 7)

if ask1 == 1 and ask2 == 1:

    print(f'''Dice:
        Attacker: {a_1}
        Defender: {d_1}''')
    if a_1 > d_1:
        print(f'''Outcome:
        Attacker: Lost 0 units
        Defender: Lost 1 unit''')
    else:
        print(f'''Outcome:
        Attacker: Lost 1 unit
        Defender: Lost 0 units''')
elif ask1 == 2 and ask2 == 1:
    print(f'''Dice:
        Attacker: {a_1}-{a_2}
        Defender: {d_1}''')
    a = [a_1, a_2]
    if max(a) > d_1:
        print(f'''Outcome:
        Attacker: Lost 0 units
        Defender: Lost 1 unit''')
    else:
        print(f'''Outcome:
        Attacker: Lost 1 unit
        Defender: Lost 0 units''')
elif ask1 == 3 and ask2 == 1:
    print(f'''Dice:
        Attacker: {a_1}-{a_2}-{a_3}
        Defender: {d_1}''')
    a = [a_1, a_2, a_3]
    if max(a) > d_1:
        print(f'''Outcome:
        Attacker: Lost 0 units
        Defender: Lost 1 unit''')
    else:
        print(f'''Outcome:
        Attacker: Lost 1 unit
        Defender: Lost 0 units''')
elif ask1 == 1 and ask2 == 2:
    print(f'''Dice:
        Attacker: {a_1}
        Defender: {d_1}-{d_2}''')
    d = [d_1, d_2]
    if a_1 > max(d):
        print(f'''Outcome:
        Attacker: Lost 0 units
        Defender: Lost 1 unit''')
    else:
        print(f'''Outcome:
        Attacker: Lost 1 unit
        Defender: Lost 0 units''')
elif ask1 == 2 and ask2 == 2:
    print(f'''Dice:
        Attacker: {a_1}-{a_2}
        Defender: {d_1}-{d_2}''')
    if a_1 > d_1 and a_2 > d_2:
        print(f'''Outcome:
        Attacker: Lost 0 units
        Defender: Lost 2 units''')
    elif a_1 > d_1 and a_2 <= d_2 or a_1 <= d_1 and a_2 > d_2:
        print(f'''Outcome:
        Attacker: Lost 1 unit
        Defender: Lost 1 unit''')
    else:
        print(f'''Outcome:
        Attacker: Lost 2 units
        Defender: Lost 0 units''')
elif ask1 == 3 and ask2 == 2:
    print(f'''Dice:
        Attacker: {a_1}-{a_2}-{a_3}
        Defender: {d_1}-{d_2}''')
    a = [a_1, a_2, a_3]
    d = [d_1, d_2]
    a.sort()
    d.sort()
    if a[2] > d[1] and a[1] > d[0]:
        print(f'''Outcome:
        Attacker: Lost 0 units
        Defender: Lost 2 units''')
    elif a[2] > d[1] and a[1] <= d[0] or a[2] <= d[1] and a[1] > d[0]:
        print(f'''Outcome:
        Attacker: Lost 1 unit
        Defender: Lost 1 unit''')
    else:
        print(f'''Outcome:
        Attacker: Lost 2 units
        Defender: Lost 0 units''')
