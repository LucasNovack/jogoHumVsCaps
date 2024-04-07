from character_files.second_soldier import second_soldier
from game.last_battle import last_battle
from endings.end_game import game_over_on_second_fight
from prints.second_fight import print_first_fight_result, print_second_fight_soldier_stats
from prints.capy_stats import print_capy_stats
from prints.attacks import print_attack_types
import battle_system.attacks as att
import utils.clear_terminal as cl

expected_options = ["1", "2", "3"]

def second_fight(capy: dict):
    cl.clear_terminal()
    print_first_fight_result()
    input("Aperte 'ENTER' para continuar")

    cl.clear_terminal()

    is_capy_alive = True
    is_second_soldier_alive = True

    while is_capy_alive and is_second_soldier_alive:
        print_second_fight_soldier_stats(second_soldier)
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
                second_soldier["health"] = att.heavy_attack(capy["strenght"], second_soldier["health"], "Capivara")
            case "2":
                second_soldier["health"] = att.light_attack(capy["strenght"], capy["speed"], second_soldier["defense"], second_soldier["health"], "Capivara")
            case "3":
                second_soldier["health"] = att.lucky_attack(capy["luck"], second_soldier["health"], "Capivara")
        
        is_second_soldier_alive = second_soldier["health"] > 0

        if is_second_soldier_alive:
                            capy["health"] = att.ia_random_attack(second_soldier["strenght"], second_soldier["speed"], 
                                            second_soldier["luck"], capy["defense"], capy["health"], "Soldado Raso")
        
        is_capy_alive = capy["health"] > 0

    match is_capy_alive:
        case True:
            last_battle(capy=capy)
        case False:
            game_over_on_second_fight()