def print_second_fight_result():
    print(f"""

     ----.
    "   _)
    "@   >
    |\   7
    / `-- _         ,-------,****
 ~    >o<  \---------o((___)-
/  |  \  /  ________/8'
|  |       /         "
|  /      |


Ufa!!! Depois de muita luta, você conseguiu eliminar o perigoso guarda-costas do general.
Essa luta provou que você está mais forte do que imagina, e agora, sua vingança é apenas
questão de tempo.
          
Agora, você olha para trás e consegue ver o caos que suas ações resultaram, soldados
estão atirando com armas que explodem sozinhas por mau funcionamento, soldados envenenados
atirando contra os próprios aliados e muitos outros desertando devido à bagunça.

Mesmo assim, você está aflito, já que sua próxima luta será contra o grande general inimigo,
o carrasco dos seus familiares, o monstro que destruiu sua vida.

Você sobe a colina e entra na tenda, esperando encontrar um ser musculoso de 2 metros de altura,
armado até os dentes e com a cara fechada.

Porém, não é isso que você encontra.......

""")

def print_general_revelation():
    print(f"""

               ......               
            .:||||||||:.            
           /            \           
          (   o      o   )          
--@@@@----------:  :----------@@@@--

Você entra na sala e descobre que a pessoa que causou toda a sua dor e sofrimento não
passa de um humano pequeno, mixuruca e medroso. A imagem que você encontra é de algo que
não passa de um ser totalmente acuado e retraído, escondido atrás de uma grande mesa de madeira
rara e extinta.

Você percebe então que esse é o reflexo dos humanos que você enfrentou, covardes e sem ética,
que realizam crueldades apenas para manter o ego inflado e se divertir com a dor alheia.

Sem tempo para lamentações, você parte para a luta final.

""")



def print_general_stats(general):
    print(f"""

               ......               
            .:||||||||:.            
           /            \           
          (   o      o   )          
--@@@@----------:  :----------@@@@--

Nome do inimigo: Soldado raso.
Vida: {general["health"]}
Força: {general["strenght"]}
Velocidade: {general["speed"]}
Defesa: {general["defense"]}
Sorte: {general["luck"]}
""")