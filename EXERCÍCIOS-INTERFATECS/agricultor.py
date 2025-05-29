def julgamento(temperatura, umidade, previsao):
    if previsao == 1:
        return 'NAO REGAR'
    elif temperatura > 30.0 and umidade < 50.0:
        return 'REGAR'
    else:
        return 'NAO REGAR'

def main():
    qtd_leituras = int(input())
    for i in range(qtd_leituras):
        temperatura, umidade, previsao = input().split()
        temperatura = float(temperatura)
        umidade = float(umidade)
        previsao = int(previsao)
        print(julgamento(temperatura, umidade, previsao))

main()
