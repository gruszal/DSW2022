text_with_numbers = '2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67'

str_numbers = text_with_numbers.split()

print(str_numbers)

numbers = [int(number) for number in str_numbers]

print(numbers)
print(type(numbers[0]))
