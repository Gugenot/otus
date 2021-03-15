"""
Домашнее задание №1
Функции и структуры данных
"""

# Задание № 1

def power_numbers(*args):
    return [x ** 2 for x in args]

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


FILTERS_MAP = {
    ODD: lambda n: n % 2 != 0,
    EVEN: lambda n: n % 2 == 0,
    PRIME: is_prime,
}


def filter_numbers(list_of_numbers, type_of_number):
    return list(filter(FILTERS_MAP[type_of_number], list_of_numbers))