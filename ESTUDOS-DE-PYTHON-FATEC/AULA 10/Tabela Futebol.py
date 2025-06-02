def exibe_tabela(T, L, C):
    for i in range(L):
        for j in range(C):
            print(T[i][j])
        print()

def preenche_tabela(T, L, campos):
    for i in range(L):
        registro = []
        for campo in campos:
            if campo == 'time':
                x = input(f'{campo}? ')
            else:
                x = int(input(f'{campo}? '))
            registro.append(x)
        print('-' * 30)
        T.append(registro)
            

def main():
    T = []
    campos = ['time', 'pontuação', 'qtd jogos', 'vitórias',
              'derrotas', 'empates']
    preenche_tabela(T, 3, campos)
    exibe_tabela(T, len(T), len(T[0]))

main()

# time | pontuação | qtd de jogos | vitórias | derrotas | empates
