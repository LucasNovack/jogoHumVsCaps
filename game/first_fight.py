from character_files.first_soldier import first_soldier
from prints.attacks import print_attack_types
from prints.capy_stats import print_capy_stats
from prints.first_fight import print_first_fight_1, print_first_fight_2, print_first_fight_soldier_stats
from endings.end_game import game_over_on_first_fight
import battle_system.attacks as att
import utils.clear_terminal as cl

expected_options = ["1", "2", "3"]

def first_fight(capy: dict, class_name: str):
    cl.clear_terminal()
    print_first_fight_1(class_name)
    input("Aperte 'ENTER' para continuar")

    cl.clear_terminal()
    print_first_fight_2()
    input("Aperte 'ENTER' para continuar")

    cl.clear_terminal()

    is_capy_alive = True
    is_first_soldier_alive = True

    while is_capy_alive and is_first_soldier_alive:
        print_first_fight_soldier_stats(first_soldier)
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
                first_soldier["health"] = att.heavy_attack(capy["strenght"], first_soldier["health"], "Capivara")
            case "2":
                first_soldier["health"] = att.light_attack(capy["strenght"], capy["speed"], first_soldier["defense"], first_soldier["health"], "Capivara")
            case "3":
                first_soldier["health"] = att.lucky_attack(capy["luck"], first_soldier["health"], "Capivara")
        
        is_first_soldier_alive = first_soldier["health"] > 0

        if is_first_soldier_alive:
                            capy["health"] = att.ia_random_attack(first_soldier["strenght"], first_soldier["speed"], 
                                            first_soldier["luck"], capy["defense"], capy["health"], "Soldado Raso")
        
        is_capy_alive = capy["health"] > 0

    match is_capy_alive:
        case True:
            print("Parabéns, derrotou o primeiro soldado.")
        case False:
            game_over_on_first_fight()
        
        
