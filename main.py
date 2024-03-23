import cliPrints
import rollTheDice


cliPrints.printLogo()
userMenuChoice = "0"

while userMenuChoice != "2":
    print("""
Bem vindo(a) ao Humanos vs Capivaras
Escolha uma das opções abaixo para dar continuidade ao jogo.
          
1 - Iniciar o Jogo
2 - Sair          
""")
    userMenuChoice = input()

print("""
No Humanos vs Capivaras, você pode escolher uma entre as três classes abaixo:
      
1 - Guerreiro: Forte como uma muralha, lento como uma lesma e sortudo como um torcedor do Vasco.
2 - Batedor: Rápido como uma flecha, frágil como um Peugeot e uma sorte +/-.
3 - Sortudo: Nunca foi sorte, sempre foi Deus!
      
""")