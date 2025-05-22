# Conversor de Temperatura
# Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin. 
# O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.

print("Conversor de Temperatura")
print("Unidades disponíveis: C (Celsius), F (Fahrenheit), K (Kelvin)")

temperatura = float(input("Digite a temperatura: "))
unidade_origem = input("Unidade de origem (C/F/K): ").upper()
unidade_destino = input("Converter para (C/F/K): ").upper()

if unidade_origem == 'C':
    celsius = temperatura
elif unidade_origem == 'F':
    celsius = (temperatura - 32) * 5/9
elif unidade_origem == 'K':
    celsius = temperatura - 273.15

if unidade_destino == 'C':
    resultado = celsius
elif unidade_destino == 'F':
    resultado = celsius * 9/5 + 32
elif unidade_destino == 'K':
    resultado = celsius + 273.15

print("Resultado:", resultado,"°", unidade_destino)