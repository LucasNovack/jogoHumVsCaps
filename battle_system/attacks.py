from battle_system.roll_the_dice import roll_d10, roll_d3

def heavy_attack(attacker_strenght: int, attacked_health: int, name: str):
    sucess_rate = roll_d10()
    print(f"{name} realiza um ataque pesado!")
    return round(attacked_health - (attacker_strenght * sucess_rate))

def light_attack(attacker_strenght: int, attacker_speed: int, attacked_defense: int, attacked_health: int, name: str):
    sucess_rate = roll_d10()
    print(f"{name} realiza um ataque leve!")
    return round(attacked_health - ((attacker_strenght + attacker_speed - attacked_defense) * sucess_rate))

def lucky_attack (attacker_luck: int, attacked_health: int, name: str):
    sucess_rate = roll_d10()
    print(f"{name} realiza um ataque de sorte!")
    return round(attacked_health - (attacker_luck * sucess_rate))

def ia_random_attack(attacker_strenght: int, attacker_speed: int, attacker_luck: int, attacked_defense: int, attacked_health: int, name: str):
    attack_type = roll_d3()
    match attack_type:
        case 1:
            return heavy_attack(attacker_strenght, attacked_health, name)
        case 2:
            return light_attack(attacker_strenght, attacker_speed, attacked_defense, attacked_health, name)
        case 3:
            return lucky_attack(attacker_luck, attacked_health, name)