def area_triangulo(base, altura):
    return (base * altura) / 2

def area_circulo(raio):
    return 3.14159 * raio**2

def area_trapezio(base_menor, base_maior, altura):
    return (base_menor + base_maior) * altura / 2

def area_quadrado(lado):
    return lado**2

def area_retangulo(base, altura):
    return base * altura

a, b, c = input().split()
a, b, c = float(a), float(b), float(c)

print(f'TRIANGULO: {area_triangulo(a, c):.3f}')
print(f'CIRCULO: {area_circulo(c):.3f}')
print(f'TRAPEZIO: {area_trapezio(a, b, c):.3f}')
print(f'QUADRADO: {area_quadrado(b):.3f}')
print(f'RETANGULO: {area_retangulo(a, b):.3f}')
