from error import  Atribut, Operator, Iten as EIten, Base
from json import load
from random import randint


class Person:
    def __init__(self, life, name):
        self.name = name
        self.life = life.__int__()
        self.stamina = 100
        self.in_guard = False

    def __str__(self):
        return f"name: {self.name}\nlife: {self.life}\nstamina: {self.stamina}"

    @staticmethod
    def __atributs__():
        return ["life", "stamina"]

    def modify(self, atribut, operator, amount):
        if str(atribut) not in self.__atributs__():
            raise Atribut(f"{atribut} not exist.")
        elif operator not in ["-", "+"]:
            raise Operator(f'`operator` should not be other than "-" or "+".')
        else:
            try:
                exec(f"self.{atribut} {operator}= {amount}")
            except Exception as error:
                raise Exception(error)


class Iten:
    def __init__(self, name_iten):
        with open("./itens.json") as file:
            try:
                self._iten = load(file).get(str(name_iten))
            except:
                raise EIten(f"{name_iten}, not found.")

    @staticmethod
    def number(max=int):
        "Return a random number from 0 to `max`."
        return randint(0, int(max))

    @staticmethod
    def _damage(base):
        if len(base) != 2:
            raise Base("`base` must have only two values, X and Y.")
        else:
            return randint(base[0], base[1])

    def damage(self, stamina):
        damages = sorted([self._damage(self._iten["damage"]) for nothing in range(4)])
        if stamina >= 75:
            return damages[0]
        elif stamina >= 50:
            return damages[1]
        elif stamina >= 25:
            return damages[2]
        else:
            return damages[4]


class Human(Person):
    def __init__(self, name):
        Person.__init__(self, 100, name)
