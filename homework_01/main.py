"""
Домашнее задание №1
Функции и структуры данных
"""
# def power_numbers():
#     """
#     функция, которая принимает N целых чисел,
#     и возвращает список квадратов этих чисел
#     >>> power_numbers(1, 2, 5, 7)
#     <<< [1, 4, 25, 49]
#     """

def power_numbers(a, b, c, d):
    return print(list({a ** 2, b ** 2, c ** 2, d ** 2}))
power_numbers(1, 2, 5, 7)
# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def is_prime(prime):
    for q in range(2, int(prime ** 0.5) + 1):
        if prime % q == 0:
            return False
    return True
# def filter_numbers():
#     """
#     функция, которая на вход принимает список из целых чисел,
#     и возвращает только чётные/нечётные/простые числа
#     (выбор производится передачей дополнительного аргумента)
#
#     >>> filter_numbers([1, 2, 3], ODD)
#     <<< [1, 3]
#     >>> filter_numbers([2, 3, 4, 5], EVEN)
#     <<< [2, 4]
#     """
def filter_numbers(nums, name):
    if name == ODD:
        return print(list(filter(lambda q: (q % 2 == 1), nums)))
    if name == EVEN:
        return print(list(filter(lambda q: (q % 2 == 0), nums)))
    if name == PRIME:
        return print(list(filter(is_prime, nums)))


filter_numbers([1, 2, 3], ODD)
filter_numbers([2, 3, 4, 5], EVEN)
filter_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], PRIME)
