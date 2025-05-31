# 4) Trabalhar com JSON
import json

info = {
    "nome": "João",
    "idade": 25,
    "cidade": "Recife"
}

arquivo_json = input("Nome do arquivo JSON: ")

try:
    arquivo = open(arquivo_json, 'w', encoding='utf-8')
    
    json.dump(info, arquivo, ensure_ascii=False, indent=4)
    
    arquivo.close()
    
    print("Dados salvos!")
    
except:
    print("Erro ao salvar!")

try:
    arquivo = open(arquivo_json, 'r', encoding='utf-8')
    
    dados_lidos = json.load(arquivo)
    
    print("Dados do arquivo:")
    print(dados_lidos)
    
    arquivo.close()
    
except:
    print("Não consegui ler o arquivo!")