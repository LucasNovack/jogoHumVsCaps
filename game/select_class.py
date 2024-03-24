from prints.select_class import print_select_class
from character_files.build_types import warrior, scout, lucky
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
            print(warrior["strenght"])
        case "2":
            print(**scout)
        case "3":
            print(**lucky)
    