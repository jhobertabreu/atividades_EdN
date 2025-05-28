# EXERCÍCIO PRÁTICO 3
# Crie uma função que calcule a idade de uma pessoa em dias, baseada no ano de nascimento.

def calcular_idade_em_dias(ano_nascimento):
    ano_atual = 2025    
    idade_em_anos = ano_atual - ano_nascimento    
    # não vou considerar anos bissextos
    idade_em_dias = idade_em_anos * 365
    
    return idade_em_dias

ano = int(input("Digite o ano  em que você nasceu: "))
dias = calcular_idade_em_dias(ano)
print(f"Você tem, aproximadamente, {dias} dias de vida.")
