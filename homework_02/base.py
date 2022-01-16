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
# from add import func_name

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
        if self.started != True: # проверяем, что мы находимся не в состоянии движения и сразу же количество оставшегося топлива
            if self.fuel <= 0:
                raise LowFuelError("WARNING: the fuel is very low ...") # выбрасываем исключение о том, что топлива осталось мало (если его количество меньше или равно нуля)
            else:
                self.started = True # включаем двигатель (если он еще не включен и количество оставшегося топлива больше нуля)

    def move(self, distance):
        if self.fuel < (distance * self.fuel_consumption): # сравниваем количество оставшегося топлива с произведением расхода топлива и оставшихся единиц дистанции
            self.started = False # выключаем двигатель, так как ехать машина более не может (топливо кончилось)
            raise NotEnoughFuel("CRITICAL: the fuel is not enough ...") # выбрасываем исключение о недостаточном количестве топлива
        self.fuel -= self.fuel_consumption*distance # сокращаем топливо на обычный расход за единицу дистанции

    def __str__(self):
        return f"{self.__class__.__name__} module is called"
