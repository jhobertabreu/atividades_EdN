# GERADOR DE USUÁRIO ALEATÓRIO

# precisei instalar a biblioteca requests antes
import requests

def obter_usuario_aleatorio():
  
    # API que gera usuários aleatórios
    url = "https://randomuser.me/api/"
    
    try:
        print("Buscando usuário na internet...")
        
        response = requests.get(url)
        
        response.raise_for_status()
        
        dados = response.json()['results'][0]
        
        # Extraindo as informações desejadas
        nome_completo = f"{dados['name']['first']} {dados['name']['last']}"
        email = dados['email']
        pais = dados['location']['country']
        idade = dados['dob']['age']
        telefone = dados['phone']
        
        # Formatando e retornando as informações
        return f"""
INFORMAÇÕES DO USUÁRIO:
Nome: {nome_completo}
Email: {email}
País: {pais}
Idade: {idade} anos
Telefone: {telefone}
        """
        
    except requests.RequestException as e:
        # Caso haja erro na conexão
        return f"Erro ao buscar usuário: Verifique sua conexão com a internet.\nDetalhes: {e}"
    
    except KeyError as e:
        # Se os dados estiverem em formato diferente do esperado
        return f"Erro nos dados recebidos: {e}"

def main():    
    
    print("--- GERADOR DE USUÁRIO ALEATÓRIO ---")
    print("Este programa gera informações de uma pessoa fictícia!")
    print()
    
    resposta = input("Deseja gerar um usuário aleatório? (s/n): ").lower()
    
    if resposta in ['s', 'sim', 'y', 'yes']:
        # Obtendo e exibindo o usuário
        usuario = obter_usuario_aleatorio()
        print(usuario)
    else:
        print("Programa encerrado!")

if __name__ == "__main__":
    main()