def consumo(distancia, combustivel):
    return distancia / combustivel

distancia = int(input())
combustivel = float(input())
print(f'{consumo(distancia, combustivel):.3f} km/l')
