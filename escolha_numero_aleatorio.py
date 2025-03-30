# python.exe .\escolha_numero_aleatorio.py

import random
 
numero = random.randint(1, 10)
 
while True:
    palpite = int(input("Seu palpite: "))
    
    if palpite == numero:
        print("Uhuul! Você acertou!")
        break
 
    if palpite < numero:
        print( "Muito baixo, tente de novo")
    else:
        print("Muito alto, tente de novo")
 
print("Até mais!")