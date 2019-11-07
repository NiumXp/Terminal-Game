from random import randint
from time import sleep

_counter = 0
def counter():
    global _counter
    return (_counter := (_counter + 1) * - 1)

def to_color(string: str, color: int, bold: bool=True):
    return "\033[{};{}m".format(int(bold), color) + string + "\033[0m"


class color:
    black = 30
    red = 31
    green = 32
    yellow = 33
    blue = 34
    magenta = 35
    cyan = 36
    white = 37

    @property
    def random(self):
        return randint(30, 37)


class EventHandler:
    def __init__(self, *names):

        def simple_function(*args, **kwargs):
            return args, kwargs

        self._itens = [names, [simple_function  for _ in range(len(names))]]

    @property
    def names(self):
        return self._itens[0]

    @property
    def functions(self):
        return self._itens[1]

    def exists(self, function_name: str):
        return function_name in self._itens[0]

    def take(self, function_name: str):
        if self.exists(function_name):
            return self._itens[1][self._itens[0].index(function_name)]
        else:
            raise NameError("function name not exists")

    def call(self, function_name: str, *args, **kwargs):
        return self.take(function_name)(*args, **kwargs)

    def __call__(self, function: object):
        if self.exists(function.__name__):
            self._itens[1][self._itens[0].index(function.__name__)] = function
        else:
            raise NameError("function name not exists")

def write(*message, separator: str=' ', delay: float=10):
    for letter in separator.join(message):
        print(end=letter, flush=True)
        sleep(delay / 1000)
