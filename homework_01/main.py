"""
Домашнее задание №1
Функции и структуры данных
"""
def power_numbers(nums):
    return list(x * x for x in nums)
power_numbers(1, 2, 5, 7)

ODD = "odd"
EVEN = "even"
PRIME = "prime"

def is_prime(prime):
    for q in range(2, int(prime ** 0.5) + 1):
        if prime % q == 0:
            return False
    return True

def filter_numbers(nums, filter_type):
    if filter_type == ODD:
        return list(filter(lambda q: (q % 2 == 1), nums))
    if filter_type == EVEN:
        return list(filter(lambda q: (q % 2 == 0), nums))
    if filter_type == PRIME:
        return list(filter(is_prime, nums))
