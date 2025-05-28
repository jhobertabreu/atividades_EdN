# EXERCÍCIO PRÁTICO 1

# Enunciado: Crie uma função que calcule a gorjeta a ser deixada em um restaurante, baseada no valor total da conta e na porcentagem de gorjeta desejada.
# Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.
# Parâmetros:
# valor_conta (float): O valor total da conta
# porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 15 paгa 15%)
# Parâmetros:
# valor_conta (float): O valor total da conta
# porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 15 paгa 15%)

def calcular_gorjeta(valor_conta, porcentagem_gorjeta):    
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta

valor = float(input("Valor da conta: "))
porcentagem = float(input("Porcentagem da gorjeta: "))
valor_gorjeta = calcular_gorjeta(valor, porcentagem)

print(f"O valor da gorjeta é de R$ {valor_gorjeta:.2f}")
