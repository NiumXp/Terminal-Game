from game import Person, persons, decisions, Decision
from utils import counter, write, to_color, color
from time import sleep
from os import system

def atacar(author, target):
    author.attack(target)

def passar(author):
    print(f"{author.name} passou a vez?!")

def guard(author):
    if author.guard_delay <= 0:
        author.in_guard = True
        print(f"{author.name} entrou em guarda!")
        author.guard_delay = 2
    else:
        if author.in_guard:
            print(f"{author.name} se distraiu e abaixou a guarda!")
            author.in_guard = False
        else:
            print(f"{author.name} tropeceu e não entrou em guarda!")

decisions.add(Decision(name="Atacar", function=atacar))
decisions.add(Decision(name="Passar", function=passar))
decisions.add(Decision(name="Entrar em guarda", function=guard))

persons.add(Person(name="Nium", name_color=color.blue))
persons.add(Person(name="Goblin", name_color=color.green))

@persons.event
def on_damage(person, damage_value):
    print(f"{person.name} recebeu {to_color(str(damage_value), color.red)} de dano!", end="\n\n")

@persons.event
def on_defense(person, author_of_attack):
    print(f"{person.name} escorregou e fez {author_of_attack.name} errar o ataque!")

@persons.event
def on_attack(person, target):
    print(f"{person.name} está atacando {target.name}!", end="\n\n")

@persons.event
def on_make_decision(person, decisions):
    person.guard_delay -= 1

    if person._name[0] == "Goblin":

        decision = decisions.random()

        if decision._name == "Atacar":
            if person._name[0] == "Goblin":
                complement = persons[0]
            else:
                complement = persons[1]
            
            return decision, (person, complement)
    else:
        print(f"Faça sua jogada! Escolha uma {to_color('decisão', color.yellow)} pelo {to_color('número', color.magenta)}!", end="\n\n")

        for index, decision in enumerate(decisions):
            print(f"  -> [{to_color(str(index + 1), color.magenta)}] - {decision.name}")

        print(end='\n')
        number = input(f"{person.name}: Eu escolho o número ")

        number = int(number) - 1

        if str(number).isdigit() and number in range(len(decisions)):
            decision = decisions[number]

            if decision._name == "Atacar":
                return decision, (person, persons[1])
 
        else:
            print(f"{person.name} perdeu a vez por passar uma decisão inválida!")

    return decision, (person, )

@persons.event
def on_decision(decision):
    print("Decisão escolhida:", decision.name, end="\n\n")
    sleep(1)

@persons.event
def on_dead(person):
    print(f"{person.name} morreu! Fim de jogo!")

while persons.alive:
    system("cls || clear") # Clear terminal in Windows/Linux

    person = persons[counter()]

    print(f"Vez de {person.name} - {person.stats}!", end="\n\n")
    decision, arguments = person.make_decision(decisions)
    decision.action(*arguments)

    sleep(3)
