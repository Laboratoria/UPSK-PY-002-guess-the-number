import random

def adivinhar_numero():
    numero_secreto = random.randint(1, 100)
    tentativas_p = []
    tentativas_c = []
    
    jogador = 'p'
    
    while True:
        if jogador == 'p':
            palpite_p = int(input("Jogador, digite um número entre 1 e 100: "))
            tentativas_p.append(palpite_p)

            if palpite_p < numero_secreto:
                print("Palpite muito baixo. Tente novamente.")
            elif palpite_p > numero_secreto:
                print("Palpite muito alto. Tente novamente.")
            else:
                print("Parabéns! Você acertou o número secreto!")
                print("Tentativas:", tentativas_p)
                break
            jogador = 'c'
            
        elif jogador == 'c':
            palpite_c = random.randint(1, 100)
            tentativas_c.append(palpite_c)

            if palpite_c < numero_secreto:
                print("O computador chutou", palpite_c, "e foi muito baixo.")
            elif palpite_c > numero_secreto:
                print("O computador chutou", palpite_c, "e foi muito alto.")
            else:
                print("O computador acertou o número secreto!")
                print("Tentativas do computador:", tentativas_c)
                break
            jogador = 'p'
adivinhar_numero()