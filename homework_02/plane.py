"""
- в модуле `plane` создайте класс `Plane`
    - класс `Plane` должен быть наследником `Vehicle`
    - добавьте атрибуты `cargo` и `max_cargo` классу `Plane`
    - добавьте `max_cargo` в инициализатор (переопределите родительский)
    - объявите метод `load_cargo`, который принимает число, проверяет, что в сумме с текущим `cargo` не будет перегруза, и обновляет значение, в ином случае выкидывает исключение `exceptions.CargoOverload`
    - объявите метод `remove_all_cargo`, который обнуляет значение `cargo` и возвращает значение `cargo`, которое было до обнуления
"""

from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload
# from add import func_name


class Plane(Vehicle):

    cargo = 0
    max_cargo = 500

    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.max_cargo = max_cargo

    def load_cargo(self, addition):
        if self.max_cargo < self.cargo + addition:   
            raise CargoOverload("CRITICAL: the cargo is overloaded!")
        self.cargo += addition

    def remove_all_cargo(self):
        old_cargo = self.cargo
        self.cargo = 0
        return old_cargo
