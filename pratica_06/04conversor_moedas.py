# CONSULTA DE COTAÇÃO DE MOEDAS

import requests
from datetime import datetime

def moedas_disponiveis():

    return {
        'USD': 'Dólar Americano',
        'EUR': 'Euro',
        'GBP': 'Libra Esterlina',
        'JPY': 'Iene Japonês',
        'ARS': 'Peso Argentino',
        'CAD': 'Dólar Canadense',
        'CHF': 'Franco Suíço',
        'AUD': 'Dólar Australiano'
    }

def obter_cotacao(moeda):
    
    # Convertendo tudo para maiúscula como padrão
    moeda = moeda.upper().strip()
    
    if not moeda:
        return "Por favor, informe o código da moeda!"
    
    url = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
    
    try:
        print(f"Buscando cotação de {moeda} para BRL...")
        
        response = requests.get(url)
        response.raise_for_status()
        
        dados = response.json()
        
        chave_moeda = f"{moeda}BRL"
        if chave_moeda not in dados:
            return f"Moeda '{moeda}' não encontrada ou não suportada!"
        
        cotacao = dados[chave_moeda]
        
        timestamp = int(cotacao['timestamp'])
        data_hora = datetime.fromtimestamp(timestamp)
        
        moedas_conhecidas = moedas_disponiveis()
        nome_moeda = moedas_conhecidas.get(moeda, moeda)
        
        return f"""
 COTAÇÃO ATUAL:
  Moeda: {nome_moeda} ({moeda})
 Valor Atual: R$ {float(cotacao['bid']):.4f}
 Máxima do Dia: R$ {float(cotacao['high']):.4f}
 Mínima do Dia: R$ {float(cotacao['low']):.4f}
 Variação: {float(cotacao['pctChange']):.2f}%
 Última Atualização: {data_hora.strftime('%d/%m/%Y às %H:%M:%S')}

 Para converter: 1 {moeda} = R$ {float(cotacao['bid']):.4f}
        """
        
    except requests.RequestException as e:
        return f"Erro na conexão: Verifique sua internet.\nDetalhes: {e}"
    
    except KeyError as e:
        return f"Moeda não encontrada ou dados incompletos.\nDetalhes: {e}"
    
    except ValueError as e:
        return f"Erro ao processar os dados da cotação.\nDetalhes: {e}"

def mostrar_moedas_disponiveis():
    
    print("\nPRINCIPAIS MOEDAS DISPONÍVEIS:")
    print("-" * 40)
    
    moedas = moedas_disponiveis()
    for codigo, nome in moedas.items():
        print(f"🔸 {codigo} - {nome}")
    
    print("-" * 40)
    print("💡 Digite o código de 3 letras da moeda (ex: USD, EUR)")

def main():
    
    print("--- CONSULTA DE COTAÇÃO DE MOEDAS ---")
    print("Descubra o valor atual das moedas estrangeiras em Reais!")
    
    while True:
        print("\n" + "="*50)
        print("1 - Ver moedas disponíveis")
        print("2 - Consultar cotação")
        print("3 - Sair")
        
        opcao = input("\nEscolha uma opção: ").strip()
        
        if opcao == "1":
            mostrar_moedas_disponiveis()
            
        elif opcao == "2":
            moeda = input("\nDigite o código da moeda (ex: USD, EUR): ").strip()
            
            if not moeda:
                print("⚠️  Por favor, digite um código válido!")
                continue
                
            resultado = obter_cotacao(moeda)
            print(resultado)
            
        elif opcao == "3":
            print("Programa encerrado!")
            break
            
        else:
            print("⚠️  Opção inválida! Escolha 1, 2 ou 3.")

if __name__ == "__main__":
    main()