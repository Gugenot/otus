"""
Домашнее задание №1
Функции и структуры данных
"""

# Задание № 1

def my_map(func, list_of_values):
    return (func(value) for value in list_of_values)


def process_numbers(list_of_numbers):
    return [num ** 2 for num in list_of_numbers]


def power_numbers(*args):
    return list(my_map(process_numbers, args))

# Задание № 2

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(n):
   if n <= 1 or n % 1 > 0:
      return False
   for i in range(2, n):
      if n % i == 0:
         return False
   return True


def filter_numbers(list_of_numbers, type_of_number):
    return {
        ODD: list(filter(lambda x: x % 2 != 0, list_of_numbers)),
        EVEN: list(filter(lambda x: x % 2 == 0, list_of_numbers)),
        PRIME: list(filter(lambda x: is_prime(x), list_of_numbers))
    }[type_of_number]
