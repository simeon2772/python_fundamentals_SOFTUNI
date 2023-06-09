def positive_numbers(number):
    return [i for i in number if int(i) >= 0]


def negative_numbers(number):
    return [i for i in number if int(i) < 0]


def even_numbers(number):
    return [i for i in number if int(i) % 2 == 0]


def odd_numbers(number):
    return [i for i in number if int(i) % 2 != 0]


numbers = input().split(', ')
print(f"Positive: {', '.join(positive_numbers(numbers))}")
print(f"Negative: {', '.join(negative_numbers(numbers))}")
print(f"Even: {', '.join(even_numbers(numbers))}")
print(f"Odd: {', '.join(odd_numbers(numbers))}")