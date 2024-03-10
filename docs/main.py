import random


# função para sortear um número aleatório 
def adivinhar_numero():
    numero_secreto = random.randint(1, 100)
    return numero_secreto

# função para fazer um palpite
def fazer_palpite(jogador):
    palpite = 0
    if jogador["nome"] == "Computador":
        palpite = random.randint(1, 100)
        print(f'{jogador["nome"]} palpitou {palpite}')
    else:
        palpite = int(input(f'{jogador["nome"]}, faça seu palpite: '))
    return palpite

#armazenar os palpites no array palpite de cada jogador
def armazenar_palpite(jogador, palpite):
    if jogador["nome"] == "Computador":
        jogador["palpites_computador"].append(palpite)
    else:
        jogador["palpites_humano"].append(palpite)
        
#função para analisar o palpite e printar se foi alto ou baixo        
def analisar_palpite(numero_secreto, palpite): 
    if palpite > numero_secreto: 
        print("O palpite foi maior que o número sorteado" ) 
    elif palpite < numero_secreto: 
        print("O palpite foi menor que o número sorteado")  
    else: 
        print("Parabéns! Você acertou o número sorteado") 
        
#função para reiniciar caso o jogador queira
def reiniciar_jogo(jogadores):
    resposta = input("Deseja reiniciar o jogo? (s/n): ")

    if resposta.lower() == 's':
        roda_jogo(jogadores)
    else:
        print("Fim de jogo!")      
        
#função para printar tentativas do vencedor 
def printar_tentativas(jogador):
    if jogador["nome"] == "Computador":
        print(f"As tentativas do computador foram:{jogador['palpites_computador']}")
    else:
        print(f"Suas tentativas foram:{jogador['palpites_humano']}")
        

#função para alternar os jogadores 
def troca_jogadores(beterraba):
    if beterraba == 1:
        beterraba = 0
    else:
        beterraba = 1
    return beterraba

 
#loop para alternar entre jogadas do humano e computador
def roda_jogo(jogadores):   
    numero_secreto = adivinhar_numero()
    index = 1
    while True:
        jogador = jogadores[index]
        palpite = fazer_palpite(jogador)  
        armazenar_palpite(jogador, palpite)
        analisar_palpite(numero_secreto, palpite)
        
        if palpite == numero_secreto:
            printar_tentativas(jogador)
            reiniciar_jogo(jogadores)
            break    
        
        index = troca_jogadores(index)


        

    