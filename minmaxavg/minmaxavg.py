numbers = [-5, 23, 0, -9, 12, 99, 105, -43]


def max():
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    print(f'Max number: {max_number}')


def min():
    min_number = numbers[0]
    for number in numbers:
        if number < min_number:
            min_number = number
    print(f'Min number: {min_number}')


def avg():
    sum = 0
    for number in numbers:
        sum += number
    print(f'Avg number: {sum/len(numbers)}')


max()
min()
avg()
