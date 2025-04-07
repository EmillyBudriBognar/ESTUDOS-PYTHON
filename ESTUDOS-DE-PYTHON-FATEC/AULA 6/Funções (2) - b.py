def cabecalho():
    print('Fatec Diadema')

cont_linha = 5

for i in range(16):
    if cont_linha > 4:
        cabecalho()
        cont_linha = 1
    print('Testando a função cabecalho')
    cont_linha += 1
