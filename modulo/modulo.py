# Write a program which prints the top 25 three-digit natural numbers divisible by 7 or by 9
# Each number should be displayed in a separate line.

number = 999
numbers = []

while number > 7:
    if number % 9 == 0 or number % 7 == 0:
        numbers.append(number)
    number -= 1
    if len(numbers) >= 25:
        break
for e in numbers:
    print(e)
