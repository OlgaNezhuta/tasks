def separate_numbers(number):
    first_digit = number // 100000
    second_digit = (number - (first_digit * 100000)) // 10000
    third_digit = (number - (first_digit * 100000) - (second_digit * 10000)) // 1000
    sixth_digit = number % 10
    fifth_digit = number % 100 // 10
    fourth_digit = number % 1000 // 100
    return first_digit, second_digit, third_digit, fourth_digit, fifth_digit, sixth_digit


def is_happy(separate_numbers):
    return True if sum(separate_numbers[:3]) == sum(separate_numbers[3:]) else False


count = 0
for i in range(1, 1000000):
    numbers_tuple = separate_numbers(i)
    if is_happy(numbers_tuple):
        print(numbers_tuple)
        count += 1

print(count)

