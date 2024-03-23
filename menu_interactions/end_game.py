from menu_interactions.cli_prints import print_logo, game_ended_on_first_menu_message
from utils.clear_terminal import clear_terminal

def game_ended_on_first_menu():
    clear_terminal()
    print_logo()
    game_ended_on_first_menu_message()


## IMPLEMENTAR OUTRAS FORMAS DE ENCERRAMENTO DO JOGO