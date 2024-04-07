from character_files.general import general
from game.final_game import final_game
from endings.end_game import game_over_on_final_fight
from prints.last_battle import print_general_stats, print_second_fight_result, print_general_revelation
from prints.capy_stats import print_capy_stats
from prints.attacks import print_attack_types
import battle_system.attacks as att
import utils.clear_terminal as cl

expected_options = ["1", "2", "3"]

def last_battle(capy: dict):
    cl.clear_terminal()
    print_second_fight_result()
    input("Aperte 'ENTER' para continuar")

    cl.clear_terminal()
    print_general_revelation()
    input("Aperte 'ENTER' para continuar")

    cl.clear_terminal()

    is_capy_alive = True
    is_general_alive = True

    while is_capy_alive and is_general_alive:
        print_general_stats(general)
        print("==========")
        print_capy_stats(capy)
        print_attack_types()
        choice = input()
        
        cl.clear_terminal()

        while choice not in expected_options:
            print("Por favor, escolha apenas algo válido.")
            print_attack_types()
            choice = input()
            cl.clear_terminal()
        
        match choice:
            case "1":
                general["health"] = att.heavy_attack(capy["strenght"], general["health"], "Capivara")
            case "2":
                general["health"] = att.light_attack(capy["strenght"], capy["speed"], general["defense"], general["health"], "Capivara")
            case "3":
                general["health"] = att.lucky_attack(capy["luck"], general["health"], "Capivara")
        
        is_general_alive = general["health"] > 0

        if is_general_alive:
                            capy["health"] = att.ia_random_attack(general["strenght"], general["speed"], 
                                            general["luck"], capy["defense"], capy["health"], "Soldado Raso")
        
        is_capy_alive = capy["health"] > 0

    match is_capy_alive:
        case True:
            final_game()
        case False:
            game_over_on_final_fight()
