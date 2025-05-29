M = []

qtd_alunos = int(input('Quantos alunos? '))
qtd_notas = int(input('Quantas notas? '))

for i in range(qtd_alunos):
    aluno = []
    print(f'{i+1}º Aluno\n')
    for j in range(qtd_notas):
        nota = float(input(f'{j+1}º Nota? '))
        aluno.append(nota)
    print('-' * 20)
    M.append(aluno)
