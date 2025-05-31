# 3) VERIFICADOR DE SENHA
print("--- VERIFICADOR DE SENHA ---")
senha = input("Digite uma senha: ")

if len(senha) < 8:
    print("Senha muito curta! Precisa ter, pelo menos, 8 caracteres.")
else:
    tem_numero = False
    for letra in senha:
        if letra.isdigit():
            tem_numero = True
    
    if tem_numero:
        print("Senha forte e válida!")
    else:
        print("Senha fraca! Precisa ter pelo menos um número.")

