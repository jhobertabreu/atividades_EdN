# CÓDIGO 3 - CONSULTA DE CEP

import requests
import re  # Valida o formato do CEP

def validar_cep(cep):
    
    # Remove espaços, traços e pontos
    cep_limpo = re.sub(r'[^0-9]', '', cep)
    
    # Verifica se tem exatamente oito dígitos
    if len(cep_limpo) == 8:
        return cep_limpo
    else:
        return None

def consultar_cep(cep):
        
    # Valida o CEP antes de consultar
    cep_validado = validar_cep(cep)
    
    if not cep_validado:
        return "CEP inválido! Digite um CEP com 8 números (ex: 01234567 ou 01234-567)"
    
    # URL da API ViaCEP com o CEP
    url = f"https://viacep.com.br/ws/{cep_validado}/json/"
    
    try:
        print("Consultando CEP na base dos Correios...")
        
        # Fazendo a requisição para a API
        response = requests.get(url)
        response.raise_for_status()
        
        # Converte a resposta para dicionário Python
        dados = response.json()
        
        # Verifica se o CEP foi encontrado
        # A API retorna {"erro": True} quando o CEP não existir
        if "erro" in dados:
            return "CEP não encontrado! Verifique se digitou corretamente."
        
        # Formatando as informações do endereço
        return f"""
 INFORMAÇÕES DO CEP:
 CEP: {dados['cep']}
  Logradouro: {dados['logradouro'] or 'Não informado'}
  Bairro: {dados['bairro'] or 'Não informado'}
  Cidade: {dados['localidade']}
  Estado: {dados['uf']} ({dados.get('estado', 'N/A')})
 Região: {dados.get('regiao', 'Não informado')}
 IBGE: {dados.get('ibge', 'Não informado')}
        """
        
    except requests.RequestException as e:
        return f"Erro na conexão: Verifique sua internet.\nDetalhes: {e}"
    
    except KeyError as e:
        return f"Erro nos dados recebidos: {e}"

def main():
   
    print("--- CONSULTA DE CEP ---")
    print("Digite um CEP para descobrir o endereço!")
    print()
    
    while True:
        cep = input("Digite um CEP (ou 'sair' para encerrar): ").strip()
        
        if cep.lower() in ['sair', 'exit', 'quit']:
            print("Programa encerrado!")
            break
        
        if not cep:
            print("Por favor, digite um CEP válido!")
            continue
        
        # Fazendo a consulta
        resultado = consultar_cep(cep)
        print(resultado)
        print("-" * 50)  

if __name__ == "__main__":
    main()