def print_first_fight_1(class_name: str):
    print(f"""
                   ____            ____            ____
                  /....\          /....\          /....\\
          .-.    |::::::|    .-. |::::::|    .-. |::::::|
          | |    |::::::|    | | |::::::|    | | |::::::|
          | |    (`:'':')    | | (`:'':')    | | (`:'':')
          | |   _--|__|--__  | |.--|__|--__  | |_--|__|--__
          | |  |   ________|_|_|_  ________|_|_|_  ________|_____
          | | /    |            |  |            |  |            |
          | |/  /  |            |  |            |  |            |
          |_| |/|  |            |  |            |  |            |
         (===)| |  |            |  |            |  |            |
         `==='  |`-|            |`-|            |`-|            |
          | |   |`-|            |`-|            |`-|            |
          |_|   |  |            |  |            |  |            |
                |  |            |  |            |  |            |
                |  |            |  |            |  |            |
                |`-|            |`-|            |`-|            |
                |__|            |__|            |__|            |
                /_ |            |_ |            |_ |            |
               |___`-__________-'__`-__________-'__`-__________-'

Você escolheu a classe de {class_name}!

Você passa um ano completo aprimorando suas habilidades, sempre motivado
pelo rancor e pelas lembranças dos seus familiares.

Eventualmente, você se torna um mestre em sua arte e decide que já está na hora de
começar o plano que lhe acompanha desde o início do seu treinamento.

Você está planejando invadir o quartel do maior acampamento humano, onde estão localizadas
as maiores armas e as mais importantes tropas humanas envolvidas no conflito.
          
""")
    
def print_first_fight_2():
    print("""

                      ________________
                      \      __      /         __
                       \_____()_____/         /  )
                       '============`        /  /
                        #---\  /---#        /  /
                       (# @\| |/@  #)      /  /
                        \   (_)   /       /  /
                        |\ '---` /|      /  /
                _______/ \\_____// \____/ o_|
               /       \  /     \  /   / o_|
              / |           o|        / o_| \\
             /  |  _____     |       / /   \ \\
            /   |  |===|    o|      / /\    \ \\
           |    |   \@/      |     / /  \    \ \\
           |    |___________o|__/----)   \    \/
           |    '              ||  --)    \     |
           |___________________||  --)     \    /
                |           o|   ''''   |   \__/
                |            |          |


Ao caminhar por longos dias, se escondendo das fortes patrulhas, desviando das rotas movimentadas,
você finalmente chega ao quartel. Você é forte, mas não é nenhum louco sem noção. Você percebe a
quantidade exorbitante de soldados e decide que a melhor abordagem será se esgueirar entre as
barricadas e entrar sem fazer nenhum barulho.

Lentamente, você consegue passar pelos primeiros muros e já se encontra dentro do acampamento.
No topo de uma colina, você consegue verificar uma tenda enfeitada com crânios de todos os animais
já extintos pelos humanos. Logo, você percebe que é lá onde está o general responsável pela guerra.

Confiantemente, você caminha em direção à colina, flanqueando as tropas.

Porém, ao completar metade do trajeto, um soldado raso lhe encontra e vocês entram em combate.
""")
    
def print_first_fight_soldier_stats(soldier):
    print(f"""

                      ________________
                      \      __      /         __
                       \_____()_____/         /  )
                       '============`        /  /
                        #---\  /---#        /  /
                       (# @\| |/@  #)      /  /
                        \   (_)   /       /  /
                        |\ '---` /|      /  /
                _______/ \\_____// \____/ o_|
               /       \  /     \  /   / o_|
              / |           o|        / o_| \\
             /  |  _____     |       / /   \ \\
            /   |  |===|    o|      / /\    \ \\
           |    |   \@/      |     / /  \    \ \\
           |    |___________o|__/----)   \    \/
           |    '              ||  --)    \     |
           |___________________||  --)     \    /
                |           o|   ''''   |   \__/
                |            |          |

Nome do inimigo: Soldado raso.
Vida: {soldier["health"]}
Força: {soldier["strenght"]}
Velocidade: {soldier["speed"]}
Defesa: {soldier["defense"]}
Sorte: {soldier["luck"]}
""")