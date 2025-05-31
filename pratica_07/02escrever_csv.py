# 2) Escrever arquivo CSV
import csv

pessoas = [
    ['Ana', 28, 'Rio de Janeiro'],
    ['Pedro', 34, 'São Paulo'],
    ['Maria', 30, 'Salvador']
]

nome_arquivo = input("Como quer chamar o arquivo? ")

try:
    arquivo = open(nome_arquivo, 'w', newline='', encoding='utf-8')
    
    escritor = csv.writer(arquivo)
    
    escritor.writerow(['Nome', 'Idade', 'Cidade'])
    
    for pessoa in pessoas:
        escritor.writerow(pessoa)
    
    arquivo.close()
    
    print("Arquivo salvo!")
    
except:
    print("Erro ao salvar!")
