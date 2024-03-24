import utils.clear_terminal as cl
from prints.game_over import game_ended_on_first_menu_message, game_over_on_first_interaction, print_game_over_by_surrender
from prints.misc import print_logo

def game_ended_on_first_menu():
    cl.clear_terminal()
    print_logo()
    game_ended_on_first_menu_message()

def game_over_on_first_interaction():
    cl.clear_terminal()
    game_over_on_first_interaction()

def game_over_by_surrender():
    cl.clear_terminal()
    print_game_over_by_surrender()