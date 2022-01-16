"""
- доработайте базовый класс `base.Vehicle`:
    - добавьте атрибуты `weight`, `started`, `fuel`, `fuel_consumption` со значениями по умолчанию
    - добавьте инициализатор для установки `weight`, `fuel`, `fuel_consumption`
    - добавьте метод `start`. При вызове этого метода необходимо проверить состояние `started`. И если не `started`, то нужно проверить, что топлива больше нуля, 
      и обновить состояние `started`, иначе нужно выкинуть исключение `exceptions.LowFuelError`
    - добавьте метод `move`, который проверяет, 
      что топлива достаточно для преодоления переданной дистанции (вплоть до полного расхода), 
      и изменяет количество оставшегося топлива, иначе выкидывает исключение `exceptions.NotEnoughFuel`
"""

from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel

class Vehicle():
    
    weight = 1024
    started = False 
    fuel = 250
    fuel_consumption = 10

    def __init__(self, weight=weight, fuel=fuel, fuel_consumption=fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if self.started != True:
            if self.fuel <= 0:
                raise LowFuelError
            else:
                self.started = True

    def move(self, distance):
        if self.fuel < (distance * self.fuel_consumption):
            self.started = False
            raise NotEnoughFuel
        self.fuel -= self.fuel_consumption * distance
