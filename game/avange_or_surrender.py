from prints.avange_or_survive import print_avange_or_surrender
from endings.end_game import game_over_by_surrender
from game.select_class import select_class
import utils.clear_terminal as cl

expected_options = ["1", "2"]

def avange_or_surrender():
    cl.clear_terminal()
    print_avange_or_surrender()

    choice = input()

    while choice not in expected_options:
        cl.clear_terminal()
        print_avange_or_surrender()
        print("Por favor, escolha apenas algo válido.")
        choice = input()
    
    match choice:
        case "1":
            game_over_by_surrender()
        case "2":
            select_class()