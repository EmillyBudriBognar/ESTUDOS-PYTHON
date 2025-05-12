#Problema: Verificar se um CPF tem 11 dígitos (validação simplificada).

cpf = input("Digite o CPF (apenas números): ")
if len(cpf) == 11 and cpf.isdigit():
    print("CPF válido (formato).")
else:
    print("CPF inválido.")