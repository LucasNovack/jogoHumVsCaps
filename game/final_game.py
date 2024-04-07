import utils.clear_terminal as cl
from prints.final import last_battle_sucess, moment_of_realization, the_end

def final_game():
    cl.clear_terminal()
    last_battle_sucess()
    input("Aperte 'ENTER' para continuar")

    cl.clear_terminal()
    moment_of_realization()
    input("Aperte 'ENTER' para continuar")

    cl.clear_terminal()
    the_end()
    input("Aperte 'ENTER' para encerrar o jogo")