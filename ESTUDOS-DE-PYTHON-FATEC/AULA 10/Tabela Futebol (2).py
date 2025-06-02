def exibe_tabela(T, L, C):
    for i in range(L):
        for j in range(C):
            print(T[i][j])
        print()

def preenche_tabela(T, L, campos):
    for i in range(L):
        registro = []
        for campo, tipo in campos:
            x = tipo(input(f'{campo}? '))
            registro.append(x)
        print('-' * 30)
        T.append(registro)     

def main():
    T = []
    campos = [('time',      str),
              ('pontuação', int),
              ('qtd jogos', int),
              ('vitórias',  int),
              ('derrotas',  int),
              ('empates',   int)]
    preenche_tabela(T, 3, campos)
    exibe_tabela(T, len(T), len(T[0]))

main()

# time | pontuação | qtd de jogos | vitórias | derrotas | empates
