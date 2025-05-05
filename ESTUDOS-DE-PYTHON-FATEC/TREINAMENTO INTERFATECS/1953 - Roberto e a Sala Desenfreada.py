while True:
    try:
        qtd_epr, qtd_ehd, qtd_intrusos = 0, 0, 0

        qtd_alunos = int(input())

        while qtd_alunos > 0:
            matricula, curso = input().split()
            if curso == 'EPR':
                qtd_epr += 1
            elif curso == 'EHD':
                qtd_ehd += 1
            else:
                qtd_intrusos += 1
            qtd_alunos -= 1

        print(f'EPR: {qtd_epr}')
        print(f'EHD: {qtd_ehd}')
        print(f'INTRUSOS: {qtd_intrusos}')
    except (EOFError, KeyboardInterrupt):
        break