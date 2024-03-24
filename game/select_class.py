from character_files.build_types import warrior, scout, lucky
from game.first_fight import first_fight
from prints.select_class import print_select_class
import utils.clear_terminal as cl

expected_options = ["1", "2", "3"]

def select_class():
    cl.clear_terminal()
    print_select_class()

    choice = input()

    while choice not in expected_options:
        cl.clear_terminal()
        print_select_class()
        print("Por favor, escolha apenas algo válido.")
        choice = input()

    match choice:
        case "1":
            first_fight(warrior, "Guerreiro")
        case "2":
            first_fight(scout, "Guerreiro")
        case "3":
            first_fight(lucky, "Guerreiro")
    