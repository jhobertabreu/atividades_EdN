# Calculadora de Média Escolar
# Crie um programa que calcula a média escolar de um aluno. Use as seguintes notas:

# * Nota 1: 7.5
# * Nota 2: 8.0
# * Nota 3: 6.5
# O programa deve calcular a média e exibir todas as notas e o resultado final, arredondando para duas casas decimais.


nota1 = 7.5
nota2 = 8.0
nota3 = 6.5

media_escolar = (nota1 + nota2 + nota3) / 3

print("~~~~ Notas do aluno ~~~~")
print("Nota 1:", nota1)
print("Nota 2:", nota2)
print("Nota 3:", nota3)
print("~~~~~~~~~~~~~~~~~")
print("Média final:", round(media_escolar, 2))