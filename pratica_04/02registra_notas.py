# 2) REGISTRO DE NOTAS
print("--- REGISTRO DE NOTAS ---")

notas = []

print("Digite as notas dos alunos (digite 'fim' para parar)")

while True:
    entrada = input("Digite uma nota: ")
    
    if entrada == 'fim':
        break
    
    nota = float(entrada)
    
    if nota >= 0 and nota <= 10:
        notas.append(nota)
        print("Nota adicionada!")
    else:
        print("Nota inválida! Digite um valor entre 0 e 10.")

if len(notas) > 0:
    soma = 0
    for nota in notas:
        soma = soma + nota
    
    media = soma / len(notas)
    print("\nMédia da turma:", media)
    print("Total de notas:", len(notas))
else:
    print("\nNenhuma nota foi registrada.")

print("=" * 40)
