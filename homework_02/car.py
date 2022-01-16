"""
- в модуле `car` создайте класс `Car`
    - класс `Car` должен быть наследником `Vehicle`
    - добавьте атрибут `engine` классу `Car`
    - объявите метод `set_engine`, который принимает в себя экземпляр объекта `Engine` и устанавливает на текущий экземпляр `Car`
"""

from homework_02.base import Vehicle
# from add import func_name


class Car(Vehicle):

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def set_engine(self, new_engine):
        self.engine = new_engine
        # print("Engine", new_engine, "is added to the car")
