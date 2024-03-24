import utils.clear_terminal as cl
import menu_interactions.cli_prints as prints

def game_ended_on_first_menu():
    cl.clear_terminal()
    prints.print_logo()
    prints.game_ended_on_first_menu_message()

def game_over_on_first_interaction():
    cl.clear_terminal()
    prints.game_over_on_first_interaction()

def game_over_by_surrender():
    cl.clear_terminal()
    prints.print_game_over_by_surrender()