#Problema: Verificar se três lados formam um triângulo válido.

a = float(input("Digite o primeiro lado: "))
b = float(input("Digite o segundo lado: "))
c = float(input("Digite o terceiro lado: "))
if a + b > c and a + c > b and b + c > a:
    print("Forma um triângulo.")
else:
    print("Não forma um triângulo.")