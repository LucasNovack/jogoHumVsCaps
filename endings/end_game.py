import utils.clear_terminal as cl
import prints.game_over as game_over
from prints.misc import print_logo

def game_ended_on_first_menu():
    cl.clear_terminal()
    print_logo()
    game_over.print_game_ended_on_first_menu()

def game_over_on_first_interaction():
    cl.clear_terminal()
    game_over.print_game_over_on_first_interaction()

def game_over_by_surrender():
    cl.clear_terminal()
    game_over.print_game_over_by_surrender()

def game_over_on_first_fight():
    cl.clear_terminal()
    game_over.print_game_over_on_first_fight()

def game_over_on_second_fight():
    cl.clear_terminal()
    game_over.print_game_over_on_second_fight()

def game_over_on_final_fight():
    cl.clear_terminal()
    game_over.print_game_over_on_final_fight()