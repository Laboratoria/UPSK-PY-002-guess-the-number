import random

def adivinhar_numero():
    numero_secreto = random.randint(1, 100)
    tentativas_p = []
    tentativas_c = []
    
    while True:
        jogador = input("Digite 'p' para jogador ou 'c' para computador: ")

        if jogador == 'p':
            palpite_p = int(input("Digite um número entre 1 e 100: "))
            tentativas_p.append(palpite_p)

            if palpite_p < numero_secreto:
                print("Palpite muito baixo. Tente novamente.")
            elif palpite_p > numero_secreto:
                print("Palpite muito alto. Tente novamente.")
            else:
                print("Parabéns! Você acertou o número secreto!")
                print("Tentativas:", tentativas_p)
                break
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
        else:
            print("Escolha inválida. Digite 'p' para jogador ou 'c' para computador.")

adivinhar_numero()