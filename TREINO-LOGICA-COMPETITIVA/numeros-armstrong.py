#Problema: Verificar se um número é Armstrong (soma dos cubos dos dígitos é igual ao número).

num = int(input("Digite um número: "))
digitos = [int(d) for d in str(num)]
soma_cubos = sum(d ** 3 for d in digitos)
print(f"{num} é Armstrong." if soma_cubos == num else "Não é Armstrong.")