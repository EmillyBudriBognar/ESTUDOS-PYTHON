#Problema: Implementar um jogo onde o usuário tenta adivinhar um número sorteado.

import random
numero_secreto = random.randint(1, 100)
tentativas = 0

while True:
    palpite = int(input("Digite seu palpite (1-100): "))
    tentativas += 1
    
    if palpite == numero_secreto:
        print(f"Parabéns! Você acertou em {tentativas} tentativas.")
        break
    elif palpite < numero_secreto:
        print("Tente um número maior.")
    else:
        print("Tente um número menor.")