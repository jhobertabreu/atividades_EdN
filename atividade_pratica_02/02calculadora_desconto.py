# Calculadora de Desconto
# Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

# * Nome do produto: "Camiseta"
# * Preço original: R$ 50.00
# * Porcentagem de desconto: 20%
# O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.

nome_produto = "Camiseta"
preco_original = 50.00
porcentagem_desconto = 20

valor_desconto = (porcentagem_desconto / 100) * preco_original

preco_final = preco_original - valor_desconto

print("~~~~~ Calculadora de Desconto ~~~~~")
print(" ")
print("Produto: ", nome_produto)
print("Preço original: R$", round(preco_original, 2))
print("Desconto: ", porcentagem_desconto, "%")
print("Valor do desconto: R$", round(valor_desconto, 2))
print("Preço Final: R$", round(preco_final, 2))