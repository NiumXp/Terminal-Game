from structures import Person, Human, Iten
from random import randint, choice
from os import system, name
from time import sleep

if __name__ != "__main__":
    print("Este script deve ser executado no terminal."); exit()

def clear():
    command = "cls" if name == "nt" else "clear"
    return system(command)

def machine_action(
    machine_object: Person,
    person_object: Person
    ):
    
    _choice = choice([True, True, True, False]) # 25% to defense
    if _choice:
        if person_object.in_guard:
            print(f"{person_object.name}, defendeu-se de, {machine_object.name}\n")
            person_object.in_guard = False
        else:
            knife = Iten("knife")
            damage = knife.damage(machine.stamina)
            person_object.modify("stamina", "-", randint(3, 7))
            person_object.modify("life", "-", damage)
            print(f"{machine_object.name}, causou {damage} de dano em, {person_object.name}.\n")
    else:
        print(f"{machine_object.name}, está em guarda agora.\n")
        machine_object.in_guard = True

machine = Person(120, "Nium")
player = Human(input("Qual será o nome do seu personagem? ").title())

executing = True

clear()
while executing:
    if machine.life <= 0 or player.life <= 0:
        executing = False
    else:
        print(f"Vez da/do {machine.name}.\n")
        machine_action(machine, player)

        sleep(3)
        clear()

        print(f"Vez do {player.name}.\n")
        decision = "nothing"
        while decision not in ["a", "d"]:
            decision = input(" [A] - Atacar.\n [D] - Entrar em guarda.\n\n > ").lower()
        if decision == "a":
            if machine.in_guard:
                print(f"\n{machine.name}, defendeu-se de, {player.name}.")
                machine.in_guard = False
            else:
                knife = Iten("knife")
                damage = knife.damage(player.stamina)
                player.modify("stamina", "-", randint(3, 7))
                machine.modify("life", "-", damage)
                print(f"\n{player.name}, causou {damage} de dano em, {machine.name}.")
        else:
            print(f"\n{player.name}, está em guarda agora.")
            player.in_guard = True
        sleep(3)
        clear()
