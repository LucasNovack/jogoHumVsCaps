from game.game_igniter import game_igniter
from endings.end_game import game_ended_on_first_menu
from prints.first_menu import first_menu_choice

import utils.clear_terminal as cl

expected_options = ["1", "2"]

def start_menu():
    first_menu_choice()
    user_menu_choice = input()

    while user_menu_choice not in expected_options:
        cl.clear_terminal()
        first_menu_choice()
        print("Por favor, escolha apenas algo válido.")
        user_menu_choice = input()

    match user_menu_choice:
        case "1":
                game_igniter()
        case "2": 
                game_ended_on_first_menu()
