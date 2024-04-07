def print_first_fight_result():
    print(f"""
          
               _A
             .'`"`'.
            /   , , \ 
           |   <\^/> |
           |  < (_) >|
           /=========\\
          (.---._ _.-.)
           |/   a` a |
           (      _\ |
            \    __  ;
            |\   .  /
         _.'\ '----;'-.
     _.-'  O ;-.__.'\O `o.
    /o \      \/-.-\/|    \\
    |    ;,     '.|\| /


Você derrotou o primeiro soldado!
          
Dessa forma, você continua avançando pelo acampamento inimigo, desviando das maiores hordas,
sabotando as armas inimigas, envenenando suprimentos e causando um delicioso caos silencioso.

Após passar por cerca de 6 barracas, você se vê cada vez mais próximo do seu objetivo. Agora,
você se encontra a cerca de 30 metros da tenda do general, seu inimigo final.

Porém, você acaba tendo um descuido e é avistado por um dos guarda-costas do general, ao qual
você inicia uma luta corpo-a-corpo.

""")
    
def print_second_fight_soldier_stats(soldier):
    print(f"""

               _A
             .'`"`'.
            /   , , \ 
           |   <\^/> |
           |  < (_) >|
           /=========\\
          (.---._ _.-.)
           |/   a` a |
           (      _\ |
            \    __  ;
            |\   .  /
         _.'\ '----;'-.
     _.-'  O ;-.__.'\O `o.
    /o \      \/-.-\/|    \\
    |    ;,     '.|\| /

Nome do inimigo: Soldado raso.
Vida: {soldier["health"]}
Força: {soldier["strenght"]}
Velocidade: {soldier["speed"]}
Defesa: {soldier["defense"]}
Sorte: {soldier["luck"]}
""")