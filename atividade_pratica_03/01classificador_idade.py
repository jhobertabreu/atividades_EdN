# Classificador de Idade

# Crie um programa que solicite a idade do usuário e classifique-o 
# em uma das seguintes categorias: 

# *Criança (0-12 anos), 
# *Adolescente (13-17 anos), 
# *Adulto (18-59 anos) ou 
# *Idoso (60 anos ou mais).


idade = int(input("Digite sua idade: "))

if idade < 0:
  categoria = "Idade inválida"
elif idade < 13:
    categoria = "Criança"
elif idade < 18:
    categoria = "Adolescente"
elif idade < 60:
    categoria = "Adulto"
else:
    categoria = "Idoso"

print("Sua classificação:", categoria)