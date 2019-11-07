from getpass import getuser
from utils import EventHandler, to_color, color
from random import randint, choice


class EqTypeList:
    def __init__(self, _type, *values):
        self._values = [value for value in values if type(value) == _type]

    def __getitem__(self, item):
        return self._values[item]

    def __iter__(self):
        return (item for item in self._values)

    def __len__(self):
        return len(self._values)


class Person:
    __slots__ = ("_name", "life", "in_guard", "guard_delay")

    def __init__(self, *, life: float=100, name: str=getuser(), name_color: int=color.white):
        self.life = Life(value=life)
        self._name = (name, name_color)
        self.guard_delay = 2
        self.in_guard = False

    @property
    def stats(self):
        life = int(self.life)
        _color = color.red if life <= 33 else color.yellow if life <= 66 else color.green
        return f"{to_color(str(life), _color)}/{to_color('100', color.green)}"

    @property
    def name(self):
        return to_color(*self._name)

    @property
    def dead(self):
        return self.life._value <= 0

    def attack(self, target):
        if target.in_guard:
            persons.event.call("on_defense", target, self)
        else:
            persons.event.call("on_attack", self, target)
            target.life.decrease(damage := randint(1, 15))
            persons.event.call("on_damage", target, damage)

        if target.dead:
            persons.event.call("on_dead", target)

    def make_decision(self, decisions):
        return persons.event.call("on_make_decision", self, decisions)


class Persons(EqTypeList):
    def __init__(self, *persons):
        super().__init__(Person, persons)
        self.event = EventHandler("on_damage", "on_defense", "on_attack", "on_dead", "on_decision", "on_make_decision")

    def add(self, person):
        self._values.append(person)

    @property
    def alive(self):
        return all(not person.dead for person in self._values)


persons = Persons()


class Decision:
    def __init__(self, *, name, function):
        self._name = name
        self.function = function

    @property
    def name(self):
        return to_color(self._name.title(), color.yellow)

    def action(self, *args):
        persons.event.call("on_decision", self)
        return self.function(*args)


class Decisions(EqTypeList):
    def add(self, decision):
        self._values.append(decision)

    def random(self):
        return choice(self._values)

decisions = Decisions(Decision)


class Life:
    def __init__(self, *, value: float):
        self._value = value

    def decrease(self, value: float):
        self._value -= +abs(value)

    def __str__(self):
        return str(self._value)

    def __int__(self):
        return int(self._value)
