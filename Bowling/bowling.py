def gerar_rodadas(jogadas):    
    rodadas = []
    seq_rodada = 1
    pinos_derrubados_na_rodada = []
    for pinos_derrubados in jogadas:
        pinos_derrubados_na_rodada.append(pinos_derrubados)        

        if seq_rodada < 10 and (pinos_derrubados == 10 or len(pinos_derrubados_na_rodada) == 2):            
            rodadas.append({'rodada': seq_rodada, 'pinos_derrubados': pinos_derrubados_na_rodada})
            seq_rodada += 1
            pinos_derrubados_na_rodada = []
        
    rodadas.append({'rodada': 10, 'pinos_derrubados': pinos_derrubados_na_rodada})

    return rodadas

def spare(rodada):
    return sum(rodada['pinos_derrubados']) == 10 and rodada['pinos_derrubados'][0] != 10 and rodada['pinos_derrubados'][1] != 10

def strike(rodada):
    return rodada['pinos_derrubados'][0] == 10 or rodada['pinos_derrubados'][1] == 10

def calcular_proximas_rodadas(rodadas, rodada_atual, quantidade_rodadas):
    bonus = 0
    contador = 0

    for rodada in range(len(rodadas)):
        if rodada > rodada_atual:
            for jogada in rodadas[rodada]['pinos_derrubados']:
                bonus += jogada
                contador += 1
                if contador == quantidade_rodadas:
                    return bonus
    
    return bonus

def calcular_pontos(rodadas):
    pontos = 0
    bonus = 0
    index = 0
    for rodada in rodadas:        
        pontos += sum(rodada['pinos_derrubados'])
        
        if spare(rodada):
            bonus += calcular_proximas_rodadas(rodadas, index, 1)
        if strike(rodada):
            bonus += calcular_proximas_rodadas(rodadas, index, 2)

        index += 1
    return pontos + bonus

print(calcular_pontos(gerar_rodadas([1, 4, 4, 5, 6, 4, 5, 5, 10, 0, 1, 7, 3, 6, 4, 10, 2, 8, 6])))
print(calcular_pontos(gerar_rodadas([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 2, 3, 0, 0])))
print(calcular_pontos(gerar_rodadas([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 8, 2, 3, 0,0])))
print(calcular_pontos(gerar_rodadas([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10])))

#1, 4, 4, 5, 6, 4, 5, 5, 10, 0, 1, 7, 3, 6, 4, 10, 2, 8, 6  ==> 133

#0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 2, 3, 0, 0 ==> 20

#0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 8, 2, 3, 0,0 ==> 17

#10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10 ==> 300