
from Error import Item, Category
from Random import Random

random = Random()

class Structure:
    def __init__(self, name, base=tuple):
        self.name = name
        self.base = base

class Power(object):
    def __init__(self):
            self.max = 0
            self.min = 0

    def up(self, *newvalues):
        self.max = max(newvalues[0])
        self.min = min(newvalues[0])

itens = {
    #NOME: ATRIBUTOS
    "gun": {"base": random.base("very_low")},
    "knife": {"base": random.base("low")},
    "axe": {"base": (5, 10)},
    "corrupt_axe": {"base": random.base("high")},
    "caneta_do_bolsonaro": {"base": random.base("very_high")},
    "pedaço_de_pau_do_lula":{"base":random.base("high")},
    "shield": None,
    "health_potion": {"base": (5, 10)},
    "great_health_potion": {"base": random.base("medium")},
    "critical_potion": {"base": random.base("very_low")}
}

class ItemStructure:
    def __init__(self, has, item = None):
        self.has = has
        self.item = item

class Defense:
    def __init__(self):
        self.shield = ItemStructure(False, itens["shield"])

class Attack:
    def __init__(self):
        self.gun = ItemStructure(False, itens["gun"])
        self.knife = ItemStructure(False, itens["knife"])
        self.caneta_do_bolsonaro = ItemStructure(False, itens["caneta_do_bolsonaro"])
        self.pedaço_de_pau_do_lula = ItemStructure(False,itens["pedaço_de_pau_do_lula"])

class Potions:
    def __init__(self):
        self.health = ItemStructure(False, itens["health_potion"])
        self.critical = ItemStructure(False, itens["critical_potion"])

class Items:
    def __init__(self):
        self.attack = Attack()
        self.defense = Defense()
        self.potions = Potions()

        self.__items_name__ = [key for key in itens]
        self.__categorys_name__ = ["defense", "attack", "potions"]

    def find_category(self, category):
        if not str(category) in self.__categorys_name__:
            raise Category(f"{category} not exist.")

#essa linha foi feita por Lrvgameplays#6172
    def find_item(self, name_item, item = False):
        if not str(name_item) in self.__items_name__:
            raise Item(f"{name_item} not exist.")
        else:
            #all_classes_itens = self.attack.__dir__() + self.defense.__dir__() + self.potions.__dir__()
            #all_itens = [x for x in all_classes_itens if not x.startswith("__") and not x.endswith("__")]

            try: eval("self.attack." + name_item + ".has, self.attack." + name_item + ".item")
            except: pass
            else: return eval("self.attack." + name_item + ".has, self.attack." + name_item + ".item")
            try: return eval("self.defense." + name_item + ".has, self.defense." + name_item + ".item")
            except: pass
            else: return eval("self.defense." + name_item + ".has, self.defense." + name_item + ".item")
            try: return eval("self.potions." + name_item + ".has, self.potions." + name_item + ".item")
            except: pass
            else: return eval("self.potions." + name_item + ".has, self.potions." + name_item + ".item")

    def remove_item(self, category, name_item):
        pass

    def add_item(self, category, item):
        pass

class PersonStructure(object):
    def __init__(self, life):
        self.life = 100 if life is "default" else int(life)
        self.items = Items()

    def lose_life(self, amount):
        self.life -= int(amount)
