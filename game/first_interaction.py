from menu_interactions.cli_prints import print_first_interaction_1, print_first_interaction_2, ran_away_and_survived
from endings.end_game import game_over_on_first_interaction 
from game.avange_or_surrender import avange_or_surrender
import utils.clear_terminal as cl

expected_options = ["1", "2"]

def first_interaction():
    cl.clear_terminal()
    print_first_interaction_1()
    input("Aperte 'ENTER' para continuar")
    cl.clear_terminal()
    print_first_interaction_2()
    choice = input()

    while choice not in expected_options:
        cl.clear_terminal()
        print_first_interaction_2()
        print("Por favor, escolha apenas algo válido.")
        choice = input()

    match choice:
        case "1": 
            game_over_on_first_interaction()
        case "2": 
            cl.clear_terminal()
            ran_away_and_survived()
            input("Aperte 'ENTER' para continuar")
            avange_or_surrender()
