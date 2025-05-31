# 3) Ler arquivo CSV
import csv

arquivo_nome = input("Qual arquivo CSV quer ler? ")

try:
    arquivo = open(arquivo_nome, 'r', encoding='utf-8')
    
    leitor = csv.reader(arquivo)
    
    for linha in leitor:
        print(linha)
    
    arquivo.close()
    
except:
    print("Arquivo não encontrado!")