# 4) ANALISA NÚMEROS
print("--- CONTADOR DE PARES E ÍMPARES ---")

numeros_pares = 0
numeros_impares = 0

print("Digite números inteiros (digite 'fim' para parar)")

while True:
    entrada = input("Digite um número: ")
    
    if entrada == 'fim':
        break
    
    numero = int(entrada)
    
    if numero % 2 == 0:
        print(numero, "é par!")
        numeros_pares = numeros_pares + 1
    else:
        print(numero, "é ímpar!")
        numeros_impares = numeros_impares + 1

print("\n--- RESULTADO FINAL ---")
print("Números pares encontrados:", numeros_pares)
print("Números ímpares encontrados:", numeros_impares)