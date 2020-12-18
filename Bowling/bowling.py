def calcula_bonus(rodada_atual, index, jogadas):
    if index > 1 and index < (len(jogadas) - 1):
        if jogadas[index-2] == 10:
            return jogadas[index] + jogadas[index-1]
        elif jogadas[index-2] + jogadas[index-1] == 10:
            return jogadas[index]
    return 0

def calcular_pontuacao(jogadas): 
    rodada_atual = 1
    jogada_atual = 0    
    index = 0
    pontos = 0
    pinos_deburrados_na_rodada = 0

    for pinos_derrubados in jogadas:        
        jogada_atual += 1        

        bonus = calcula_bonus(rodada_atual, index, jogadas)        

        print('rodada_atual {} jogada_atual {} bonus {}'.format(rodada_atual, jogada_atual, bonus))

        pontos += pinos_derrubados + bonus

        pinos_deburrados_na_rodada += pinos_derrubados
        
        if pinos_deburrados_na_rodada >= 10 or jogada_atual > 1:
            pinos_deburrados_na_rodada = 0
            if rodada_atual < 10:
                rodada_atual += 1
                jogada_atual = 0        

        index += 1        

    return pontos

print(calcular_pontuacao([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 8, 2, 3, 0,0]))