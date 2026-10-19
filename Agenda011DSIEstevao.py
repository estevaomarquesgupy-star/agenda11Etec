import math

resultado = math.sqrt(25)
print(resultado)

#

import random
numero = random.randint(1, 10)
print(numero)


#Pondo em prática etapa 1

participantes = ["João", "Maria", "Pedro", "Ana", "Lucas"]
print ("Participantes do sorteio:")
for participante in participantes:
    print("-", participante)
    
    import random
    sorteado = random.choice(participantes)

print("\nResultado do sorteio:")
print("O participante sorteado foi:", sorteado)


#Atividade ETEC em prática

niveis = ["Nivel 1", "Nivel 2", "Nivel 3", "Nivel 4", "Nivel 5"]
print ("Níveis do reservatório")
for nivel in niveis:
    print("-", nivel)
    
    import random
    niveis = random.choice(niveis)
    
    from colorama import Fore, Style

print (Fore.RED + "\nMuito baixo!")
print (Fore.YELLOW + "\nBaixo!")
print (Fore.GREEN + "\nNormal!")
print (Fore.CYAN + "\nAlto!")
print (Fore.BLUE + "\nMuito alto!")



