from prints.prologue import prologue_1, prologue_2, read_prologue
from game.first_interaction import first_interaction
import utils.clear_terminal as cl

expected_options = ["1", "2"]

def game_igniter():

    cl.clear_terminal()

    read_prologue()
    choice = input()

    while choice not in expected_options:
        cl.clear_terminal()
        read_prologue()
        print("Por favor, escolha apenas algo válido.")
        choice = input()

    if choice == "1":
        cl.clear_terminal()
        prologue_1()
        input("Aperte 'ENTER' para continuar")
        cl.clear_terminal()
        prologue_2()
        input("Aperte 'ENTER' para continuar")

    first_interaction()