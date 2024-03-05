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
                print("Tentativas: {}" .format(tentativas_p))
                break
            jogador = 'c'
            print('-=-'*20)
            
        elif jogador == 'c':
            palpite_c = random.randint(1, 100)
            tentativas_c.append(palpite_c)

            if palpite_c < numero_secreto:
                print("O computador chutou {} e foi muito baixo." .format(palpite_c))
            elif palpite_c > numero_secreto:
                print("O computador chutou {} e foi muito alto.".format(palpite_c))
            else:
                print("O computador acertou o número secreto!")
                print("Tentativas do computador: {}" .format(tentativas_c))
                break
            jogador = 'p'
            print('-=-'*20)

adivinhar_numero()