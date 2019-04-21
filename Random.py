from random import randint
from Error import Base

class Random:

    @staticmethod
    def number(max=int):
        "Return a random number from 0 to `max` parameter."
        return randint(0, int(max))

    @staticmethod
    def _damage(self, base=tuple):
        if len(base) != 2:
            raise Base("`base` must have only two values, X and Y.")
        else:
            base = sorted(base)
            if base[0] <= 0:
                base = self.base("low")
            return randint(base[0], base[1])

    def base(self, type):
        types = {
            "very_low": (0, 5), "low": (0, 10),
            "medium": (5, 15),
            "high": (10, 20), "very_high": (10, 25),
        } #5 -> 10 -> 10 -> 10 -> 15
        if str(type) not in types:
            raise Base("The `type` of `base` must be `very_low`, `low`, `medium`, `high` or `very_high`.")
        else:
            return types[str(type)]

    def damage(self, critical_chance, item):
        pass
