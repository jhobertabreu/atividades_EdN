# 1) Processamento de logs de treinamento
import csv
import math

arquivo = input("Qual o nome do arquivo? ")

try:
    with open(arquivo, 'r', encoding='utf-8') as f:
        leitor = csv.DictReader(f)
        
        tempos = []
        
        for linha in leitor:
            tempo = float(linha['tempo_execucao'])
            tempos.append(tempo)
    
    media = sum(tempos) / len(tempos)
    
    # Primeiro calcula a variância
    variancia = sum((tempo - media) ** 2 for tempo in tempos) / len(tempos)
    # Depois a raiz quadrada da variância
    desvio = math.sqrt(variancia)
    
    print("Média do tempo:", round(media, 2))
    print("Desvio padrão:", round(desvio, 2))
    
except:
    print("Não consegui abrir o arquivo!")