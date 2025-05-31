# 1) CALCULADORA 
print("--- CALCULADORA ---")

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

operacao = input("Digite a operação (+, -, *, /): ")

if operacao == '+':
    resultado = numero1 + numero2
    print("Resultado:", resultado)
elif operacao == '-':
    resultado = numero1 - numero2
    print("Resultado:", resultado)
elif operacao == '*':
    resultado = numero1 * numero2
    print("Resultado:", resultado)
elif operacao == '/':
    if numero2 != 0:
        resultado = numero1 / numero2
        print("Resultado:", resultado)
    else:
        print("Erro! Não é possível dividir por zero")
else:
    print("Operação inválida!")

print("=" * 40)