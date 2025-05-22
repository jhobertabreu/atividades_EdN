# Calculadora de Consumo de Combustível
# Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:

# * Distância percorrida: 300 km
# * Combustível gasto: 25 litros
# O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, incluindo o resultado final arredondado para duas casas decimais.


distancia = 300
combustivel = 25
consumo_medio = distancia / combustivel

print("~~~~ Consumo de Combustível ~~~~")
print("Distância percorrida:", distancia, "km")
print("Combustível gasto:", combustivel, "L")
print("~~~~~~~~~~~~~~~~~~~~~~")
print("Consumo médio:", round(consumo_medio, 2), "km/L")