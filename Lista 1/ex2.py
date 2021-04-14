duracao = input() .split()
hora_inicial, hora_final = duracao
hora_inicial = int (duracao [0])
hora_final = int (duracao[1])


if (hora_inicial<hora_final):
    duracao = hora_final - hora_inicial
    print ('O JOGO DUROU {} HORA(S)' .format(duracao))
else:
    duracao = 24-(hora_inicial - hora_final)
    print ('O JOGO DUROU {} HORA(S)' .format(duracao))