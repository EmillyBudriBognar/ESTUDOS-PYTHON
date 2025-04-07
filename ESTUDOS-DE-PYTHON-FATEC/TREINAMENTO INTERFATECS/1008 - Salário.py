def exibicao(numero, qtd_horas, valor_hora):
    print(f'NUMBER = {numero}')
    print(f'SALARY = U$ {qtd_horas * valor_hora:.2f}')

numero = int(input())
qtd_horas = int(input())
valor_hora = float(input())
exibicao(numero, qtd_horas, valor_hora)
