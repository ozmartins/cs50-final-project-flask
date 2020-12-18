def gerar_rodadas(jogadas):
    rodadas = []
    seq_rodada = 1
    pinos_derrubados_na_rodada = 0
    for pinos_derrubados in jogadas:
        pinos_derrubados_na_rodada += pinos_derrubados
        

        if seq_rodada < 10 and (pinos_derrubados == 10 or pinos_derrubados_na_rodada == 10):            
            if pinos_derrubados == 10:
                rodadas.append([seq_rodada, pinos_derrubados_na_rodada, 'strike'])
            elif pinos_derrubados_na_rodada == 10:
                rodadas.append([seq_rodada, pinos_derrubados_na_rodada, 'spare'])                
            seq_rodada += 1            
            pinos_derrubados_na_rodada = 0        
        
    rodadas.append([10, pinos_derrubados_na_rodada])

    return rodadas

def calcular_pontos(rodadas):
    pontos = 0
    bonus = 0
    index = 0
    for rodada in rodadas:        
        pontos += rodada[1]
        
        if index > 0 and rodadas[index-1][2] == 'spare':
            bonus += rodada[1]

        if index > 1 and rodadas[index-2][2] == 'strike':
            bonus += rodadas[index-1][1] + rodada[1]

        index += 1
    return pontos + bonus

print(calcular_pontos(gerar_rodadas([])))

#1, 4, 4, 5, 6, 4, 5, 5, 10, 0, 1, 7, 3, 6, 4, 10, 2, 8, 6  ==> 133

#0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 2, 3, 0, 0 ==> 20

#0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 8, 2, 3, 0,0 ==> 17

#10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10 ==> 300