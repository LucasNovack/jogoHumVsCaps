def print_logo():
    print(f"""
+===================================================+
|                                                   |
|                                                   |
|    _   _                                          |
|   | | | |_   _ _ __ ___   __ _ _ __   ___  ___    |
|   | |_| | | | | '_ ` _ \ / _` | '_ \ / _ \/ __|   |
|   |  _  | |_| | | | | | | (_| | | | | (_) \__ \   |
|   |_| |_|\__,_|_| |_| |_|\__,_|_| |_|\___/|___/   |
|                   __   __ ___                     |
|                   \ \ / / __|                     |
|                    \ V /\__ \                     |
|     ____            \_/ |___/                     |
|    / ___|__ _ _ __ (_)_   ____ _ _ __ __ _ ___    |
|   | |   / _` | '_ \| \ \ / / _` | '__/ _` / __|   |
|   | |__| (_| | |_) | |\ V / (_| | | | (_| \__ \   |
|    \____\__,_| .__/|_| \_/ \__,_|_|  \__,_|___/   |
|              |_|                                  |
|                                                   |
|                                                   |
+===================================================+                                         
""")
    
def game_ended_on_first_menu_message():
    print("""
Obrigado por testar a opção de encerrar o jogo pelo menu inicial.
          
O jogo está sendo encerrando, porém, seria uma boa jogar um pouquinho.
""")

def first_menu_choice():
    print_logo()
    print("""
Bem vindo(a) ao Humanos vs Capivaras
Escolha uma das opções abaixo para dar continuidade ao jogo.
          
1 - Iniciar o Jogo
2 - Sair          
""")
    